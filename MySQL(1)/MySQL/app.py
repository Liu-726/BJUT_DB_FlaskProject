# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 用于flash消息

# 数据库配置
DB_CONFIG = {
    'host': 'localhost',
    'user': 'zxc',
    'password': 'zxc2004',
    'database': 'bookstore',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}


def get_db_connection():
    """创建数据库连接"""
    return pymysql.connect(**DB_CONFIG)


@app.route('/')
def index():
    """首页仪表盘"""
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            # 获取统计信息
            cursor.execute("SELECT COUNT(*) AS book_count FROM book_info")
            book_count = cursor.fetchone()['book_count']

            cursor.execute("SELECT COUNT(*) AS buyer_count FROM buyer_info")
            buyer_count = cursor.fetchone()['buyer_count']

            cursor.execute("SELECT COUNT(*) AS order_count FROM purchase_method")
            order_count = cursor.fetchone()['order_count']

            cursor.execute(
                "SELECT SUM(price) AS total_revenue FROM purchase_method pm JOIN book_info b ON pm.book_id = b.book_id")
            total_revenue = cursor.fetchone()['total_revenue'] or 0

            # 获取最新订单
            cursor.execute("""
                SELECT pm.method_id, b.book_name, bi.name, pm.payment_method, pm.delivery_method, pm.book_id, pm.purchase_id
                FROM purchase_method pm
                JOIN book_info b ON pm.book_id = b.book_id
                JOIN buyer_info bi ON pm.purchase_id = bi.purchase_id
                ORDER BY pm.method_id DESC LIMIT 5
            """)
            recent_orders = cursor.fetchall()

            # 获取热门图书
            cursor.execute("""
                SELECT b.book_id, b.book_name, COUNT(pm.method_id) AS order_count
                FROM purchase_method pm
                JOIN book_info b ON pm.book_id = b.book_id
                GROUP BY b.book_id
                ORDER BY order_count DESC, b.book_name ASC
                LIMIT 5
            """)
            popular_books = cursor.fetchall()

        return render_template('index.html',
                               book_count=book_count,
                               buyer_count=buyer_count,
                               order_count=order_count,
                               total_revenue=total_revenue,
                               recent_orders=recent_orders,
                               popular_books=popular_books)

    except Exception as e:
        flash(f"数据库错误: {str(e)}", 'danger')
        return render_template('index.html')
    finally:
        if conn:
            conn.close()


# 图书管理
@app.route('/books')
def books():
    """图书列表"""
    search = request.args.get('search', '')
    category = request.args.get('category', 'all')

    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            # 获取所有图书分类
            cursor.execute("SELECT DISTINCT book_category FROM book_info")
            categories = [row['book_category'] for row in cursor.fetchall()]

            # 构建查询
            query = "SELECT * FROM book_info WHERE 1=1"
            params = []

            if search:
                query += " AND (book_name LIKE %s OR introduction LIKE %s)"
                params.extend([f"%{search}%", f"%{search}%"])

            if category != 'all':
                query += " AND book_category = %s"
                params.append(category)

            query += " ORDER BY book_id DESC"
            cursor.execute(query, params)
            books1 = cursor.fetchall()

        return render_template('books/books.html',
                               books=books1,
                               categories=categories,
                               current_category=category,
                               search_term=search)

    except Exception as e:
        flash(f"数据库错误: {str(e)}", 'danger')
        return render_template('books/books.html', books=[])
    finally:
        if conn:
            conn.close()


@app.route('/books/add', methods=['GET', 'POST'])
def add_book():
    """添加图书"""
    if request.method == 'POST':
        book_name = request.form['book_name']
        book_category = request.form['book_category']
        price = request.form['price']
        introduction = request.form['introduction']

        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO book_info (book_name, book_category, price, introduction) "
                    "VALUES (%s, %s, %s, %s)",
                    (book_name, book_category, price, introduction)
                )
                conn.commit()
            flash('图书添加成功!', 'success')
            return redirect(url_for('books'))
        except Exception as e:
            flash(f"添加图书失败: {str(e)}", 'danger')
        finally:
            if conn:
                conn.close()

    # 获取现有分类
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT DISTINCT book_category FROM book_info")
            categories = [row['book_category'] for row in cursor.fetchall()]
    except:
        categories = []
    finally:
        if conn:
            conn.close()

    return render_template('books/add_book.html', categories=categories)


@app.route('/books/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    """编辑图书"""
    if request.method == 'POST':
        book_name = request.form['book_name']
        book_category = request.form['book_category']
        price = request.form['price']
        introduction = request.form['introduction']

        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE book_info SET book_name = %s, book_category = %s, "
                    "price = %s, introduction = %s WHERE book_id = %s",
                    (book_name, book_category, price, introduction, book_id)
                )
                conn.commit()
            flash('图书更新成功!', 'success')
            return redirect(url_for('books'))
        except Exception as e:
            flash(f"更新图书失败: {str(e)}", 'danger')
        finally:
            if conn:
                conn.close()

    # 获取图书详情
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM book_info WHERE book_id = %s", (book_id,))
            book = cursor.fetchone()

            if not book:
                flash('图书不存在', 'danger')
                return redirect(url_for('books'))

            # 获取所有分类
            cursor.execute("SELECT DISTINCT book_category FROM book_info")
            categories = [row['book_category'] for row in cursor.fetchall()]

            return render_template('books/edit_book.html', book=book, categories=categories)
    except Exception as e:
        flash(f"获取图书信息失败: {str(e)}", 'danger')
        return redirect(url_for('books'))
    finally:
        if conn:
            conn.close()


@app.route('/books/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    """删除图书"""
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            # 检查是否有关联订单
            cursor.execute("SELECT COUNT(*) FROM purchase_method WHERE book_id = %s", (book_id,))
            order_count = cursor.fetchone()['COUNT(*)']

            if order_count > 0:
                flash('该图书存在关联订单，无法删除', 'danger')
                return redirect(url_for('books'))

            # 删除图书
            cursor.execute("DELETE FROM book_info WHERE book_id = %s", (book_id,))
            conn.commit()
        flash('图书删除成功!', 'success')
    except Exception as e:
        flash(f"删除图书失败: {str(e)}", 'danger')
    finally:
        if conn:
            conn.close()

    return redirect(url_for('books'))


# 购书者管理
@app.route('/buyers')
def buyers():
    """购书者列表"""
    search = request.args.get('search', '')

    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            query = "SELECT * FROM buyer_info"
            params = []

            if search:
                query += " WHERE name LIKE %s OR contact LIKE %s"
                params.extend([f"%{search}%", f"%{search}%"])

            query += " ORDER BY purchase_id DESC"
            cursor.execute(query, params)
            buyers = cursor.fetchall()

        return render_template('buyers/buyers.html', buyers=buyers, search_term=search)

    except Exception as e:
        flash(f"数据库错误: {str(e)}", 'danger')
        return render_template('buyers/buyers.html', buyers=[])
    finally:
        if conn:
            conn.close()


@app.route('/buyers/add', methods=['GET', 'POST'])
def add_buyer():
    """添加购书者"""
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        age = request.form['age']
        contact = request.form['contact']

        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO buyer_info (name, gender, age, contact) "
                    "VALUES (%s, %s, %s, %s)",
                    (name, gender, age or None, contact)
                )
                conn.commit()
            flash('购书者添加成功!', 'success')
            return redirect(url_for('buyers'))
        except Exception as e:
            flash(f"添加购书者失败: {str(e)}", 'danger')
        finally:
            if conn:
                conn.close()

    return render_template('buyers/add_buyer.html')


@app.route('/buyers/edit/<int:purchase_id>', methods=['GET', 'POST'])
def edit_buyer(purchase_id):
    """编辑购书者"""
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        age = request.form['age']
        contact = request.form['contact']

        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE buyer_info SET name = %s, gender = %s, "
                    "age = %s, contact = %s WHERE purchase_id = %s",
                    (name, gender, age or None, contact, purchase_id)
                )
                conn.commit()
            flash('购书者更新成功!', 'success')
            return redirect(url_for('buyers'))
        except Exception as e:
            flash(f"更新购书者失败: {str(e)}", 'danger')
        finally:
            if conn:
                conn.close()

    # 获取购书者详情
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM buyer_info WHERE purchase_id = %s", (purchase_id,))
            buyer = cursor.fetchone()

            if not buyer:
                flash('购书者不存在', 'danger')
                return redirect(url_for('buyers'))

            return render_template('buyers/edit_buyer.html', buyer=buyer)
    except Exception as e:
        flash(f"获取购书者信息失败: {str(e)}", 'danger')
        return redirect(url_for('buyers'))
    finally:
        if conn:
            conn.close()


@app.route('/buyers/delete/<int:purchase_id>', methods=['POST'])
def delete_buyer(purchase_id):
    """删除购书者"""
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            # 检查是否有关联订单
            cursor.execute("SELECT COUNT(*) FROM purchase_method WHERE purchase_id = %s", (purchase_id,))
            order_count = cursor.fetchone()['COUNT(*)']

            if order_count > 0:
                flash('该购书者存在关联订单，无法删除', 'danger')
                return redirect(url_for('buyers'))

            # 删除购书者
            cursor.execute("DELETE FROM buyer_info WHERE purchase_id = %s", (purchase_id,))
            conn.commit()
        flash('购书者删除成功!', 'success')
    except Exception as e:
        flash(f"删除购书者失败: {str(e)}", 'danger')
    finally:
        if conn:
            conn.close()

    return redirect(url_for('buyers'))


# 订单管理
@app.route('/orders')
def orders():
    """订单列表"""
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            # 获取所有订单及其关联信息
            cursor.execute("""
                SELECT pm.method_id AS order_id, 
                       pm.payment_method, 
                       pm.delivery_method,
                       b.book_id, 
                       b.book_name,
                       bi.purchase_id,
                       bi.name AS buyer_name
                FROM purchase_method pm
                JOIN book_info b ON pm.book_id = b.book_id
                JOIN buyer_info bi ON pm.purchase_id = bi.purchase_id
                ORDER BY pm.method_id DESC
            """)
            orders = cursor.fetchall()

        return render_template('orders/orders.html', orders=orders)

    except Exception as e:
        flash(f"数据库错误: {str(e)}", 'danger')
        return render_template('orders/orders.html', orders=[])
    finally:
        if conn:
            conn.close()


@app.route('/orders/add', methods=['GET', 'POST'])
def add_order():
    """添加订单"""
    if request.method == 'POST':
        purchase_id = request.form['purchase_id']
        book_id = request.form['book_id']
        payment_method = request.form['payment_method']
        delivery_method = request.form['delivery_method']

        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                # 检查购书者和图书是否存在
                cursor.execute("SELECT COUNT(*) FROM buyer_info WHERE purchase_id = %s", (purchase_id,))
                if cursor.fetchone()['COUNT(*)'] == 0:
                    flash('购书者不存在', 'danger')
                    return redirect(url_for('add_order'))

                cursor.execute("SELECT COUNT(*) FROM book_info WHERE book_id = %s", (book_id,))
                if cursor.fetchone()['COUNT(*)'] == 0:
                    flash('图书不存在', 'danger')
                    return redirect(url_for('add_order'))

                # 添加订单
                cursor.execute(
                    "INSERT INTO purchase_method (purchase_id, book_id, payment_method, delivery_method) "
                    "VALUES (%s, %s, %s, %s)",
                    (purchase_id, book_id, payment_method, delivery_method)
                )
                conn.commit()
            flash('订单添加成功!', 'success')
            return redirect(url_for('orders'))
        except Exception as e:
            flash(f"添加订单失败: {str(e)}", 'danger')
        finally:
            if conn:
                conn.close()

    # 获取购书者和图书列表
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT purchase_id, name FROM buyer_info ORDER BY name")
            buyers = cursor.fetchall()

            cursor.execute("SELECT book_id, book_name FROM book_info ORDER BY book_name")
            books = cursor.fetchall()

            # 付款和配送方式
            payment_methods = ["支付宝", "微信支付", "银行卡", "信用卡", "货到付款", "PayPal"]
            delivery_methods = ["快递", "平邮", "自提", "电子书", "同城闪送"]

            return render_template('orders/add_order.html',
                                   buyers=buyers,
                                   books=books,
                                   payment_methods=payment_methods,
                                   delivery_methods=delivery_methods)
    except Exception as e:
        flash(f"获取数据失败: {str(e)}", 'danger')
        return redirect(url_for('orders'))
    finally:
        if conn:
            conn.close()


@app.route('/orders/edit/<int:order_id>', methods=['GET', 'POST'])
def edit_order(order_id):
    """编辑订单"""
    if request.method == 'POST':
        purchase_id = request.form['purchase_id']
        book_id = request.form['book_id']
        payment_method = request.form['payment_method']
        delivery_method = request.form['delivery_method']

        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                # 检查购书者和图书是否存在
                cursor.execute("SELECT COUNT(*) FROM buyer_info WHERE purchase_id = %s", (purchase_id,))
                if cursor.fetchone()['COUNT(*)'] == 0:
                    flash('购书者不存在', 'danger')
                    return redirect(url_for('edit_order', order_id=order_id))

                cursor.execute("SELECT COUNT(*) FROM book_info WHERE book_id = %s", (book_id,))
                if cursor.fetchone()['COUNT(*)'] == 0:
                    flash('图书不存在', 'danger')
                    return redirect(url_for('edit_order', order_id=order_id))

                # 更新订单
                cursor.execute(
                    "UPDATE purchase_method SET purchase_id = %s, book_id = %s, "
                    "payment_method = %s, delivery_method = %s WHERE method_id = %s",
                    (purchase_id, book_id, payment_method, delivery_method, order_id)
                )
                conn.commit()
            flash('订单更新成功!', 'success')
            return redirect(url_for('orders'))
        except Exception as e:
            flash(f"更新订单失败: {str(e)}", 'danger')
        finally:
            if conn:
                conn.close()

    # 获取订单详情
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT pm.*, 
                       b.book_name,
                       bi.name AS buyer_name
                FROM purchase_method pm
                JOIN book_info b ON pm.book_id = b.book_id
                JOIN buyer_info bi ON pm.purchase_id = bi.purchase_id
                WHERE pm.method_id = %s
            """, (order_id,))
            order = cursor.fetchone()

            if not order:
                flash('订单不存在', 'danger')
                return redirect(url_for('orders'))

            # 获取购书者和图书列表
            cursor.execute("SELECT purchase_id, name FROM buyer_info ORDER BY name")
            buyers = cursor.fetchall()

            cursor.execute("SELECT book_id, book_name FROM book_info ORDER BY book_name")
            books = cursor.fetchall()

            # 付款和配送方式
            payment_methods = ["支付宝", "微信支付", "银行卡", "信用卡", "货到付款", "PayPal"]
            delivery_methods = ["快递", "平邮", "自提", "电子书", "同城闪送"]

            return render_template('orders/edit_order.html',
                                   order=order,
                                   buyers=buyers,
                                   books=books,
                                   payment_methods=payment_methods,
                                   delivery_methods=delivery_methods)
    except Exception as e:
        flash(f"获取订单信息失败: {str(e)}", 'danger')
        return redirect(url_for('orders'))
    finally:
        if conn:
            conn.close()


@app.route('/orders/delete/<int:order_id>', methods=['POST'])
def delete_order(order_id):
    """删除订单"""
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM purchase_method WHERE method_id = %s", (order_id,))
            conn.commit()
        flash('订单删除成功!', 'success')
    except Exception as e:
        flash(f"删除订单失败: {str(e)}", 'danger')
    finally:
        if conn:
            conn.close()

    return redirect(url_for('orders'))


# 报表功能
@app.route('/reports')
def reports():
    """统计报表"""
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            # 图书销售统计
            cursor.execute("""
                SELECT b.book_category, 
                       COUNT(pm.method_id) AS sales_count,
                       SUM(b.price) AS total_revenue
                FROM purchase_method pm
                JOIN book_info b ON pm.book_id = b.book_id
                GROUP BY b.book_category
                ORDER BY total_revenue DESC
            """)
            category_stats = cursor.fetchall()
            revenue_sum=0;
            for stat in category_stats:
                revenue_sum+=stat['total_revenue']

            # 付款方式统计
            cursor.execute("""
                SELECT payment_method, 
                       COUNT(*) AS order_count,
                       ROUND(COUNT(*)*100.0/(SELECT COUNT(*) FROM purchase_method), 1) AS percentage
                FROM purchase_method
                GROUP BY payment_method
                ORDER BY order_count DESC
            """)
            payment_stats = cursor.fetchall()

            # 配送方式统计
            cursor.execute("""
                SELECT delivery_method, 
                       COUNT(*) AS order_count,
                       ROUND(COUNT(*)*100.0/(SELECT COUNT(*) FROM purchase_method), 1) AS percentage
                FROM purchase_method
                GROUP BY delivery_method
                ORDER BY order_count DESC
            """)
            delivery_stats = cursor.fetchall()

            # 购书者统计
            cursor.execute("""
                SELECT bi.name, 
                       COUNT(pm.method_id) AS order_count,
                       SUM(b.price) AS total_spent
                FROM purchase_method pm
                JOIN buyer_info bi ON pm.purchase_id = bi.purchase_id
                JOIN book_info b ON pm.book_id = b.book_id
                GROUP BY bi.purchase_id
                ORDER BY total_spent DESC
                LIMIT 10
            """)
            buyer_stats = cursor.fetchall()

        return render_template('reports.html',
                               category_stats=category_stats,
                               payment_stats=payment_stats,
                               delivery_stats=delivery_stats,
                               buyer_stats=buyer_stats,
                               revenue_sum=revenue_sum)

    except Exception as e:
        flash(f"获取报表数据失败: {str(e)}", 'danger')
        return render_template('reports.html')
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    app.run(debug=True)