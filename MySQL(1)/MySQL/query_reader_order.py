import pymysql
from prettytable import PrettyTable
import textwrap
import query_popular_book
import query_active_buyer

# 数据库连接配置
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '123098',  # 替换为你的MySQL密码
    'database': 'bookstore',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

def get_reader_purchase_stats():
    """获取所有读者的购书统计信息"""
    try:
        connection = pymysql.connect(**DB_CONFIG)
        with connection.cursor() as cursor:
            # 查询所有读者的购书统计
            cursor.execute("""
            SELECT 
                bi.purchase_id,
                bi.name,
                bi.gender,
                bi.age,
                bi.contact,
                COUNT(pm.method_id) AS total_orders,
                COUNT(DISTINCT pm.book_id) AS unique_books,
                GROUP_CONCAT(DISTINCT b.book_category SEPARATOR ', ') AS categories,
                SUM(b.price) AS total_spent,
                AVG(b.price) AS avg_price,
                (SELECT payment_method 
                 FROM purchase_method 
                 WHERE purchase_id = bi.purchase_id 
                 GROUP BY payment_method 
                 ORDER BY COUNT(*) DESC 
                 LIMIT 1) AS top_payment,
                (SELECT delivery_method 
                 FROM purchase_method 
                 WHERE purchase_id = bi.purchase_id 
                 GROUP BY delivery_method 
                 ORDER BY COUNT(*) DESC 
                 LIMIT 1) AS top_delivery,
                MAX(pm.method_id) AS latest_order_id
            FROM buyer_info bi
            LEFT JOIN purchase_method pm ON bi.purchase_id = pm.purchase_id
            LEFT JOIN book_info b ON pm.book_id = b.book_id
            GROUP BY bi.purchase_id
            ORDER BY total_spent DESC
            """)
            return cursor.fetchall()

    except Exception as e:
        print(f"数据库查询出错: {e}")
        return []
    finally:
        if connection:
            connection.close()

def get_reader_book_details(reader_id):
    """获取指定读者的详细购书清单"""
    try:
        connection = pymysql.connect(**DB_CONFIG)
        with connection.cursor() as cursor:
            # 查询读者的详细购书记录
            cursor.execute("""
            SELECT 
                b.book_id,
                b.book_name,
                b.book_category,
                b.price,
                pm.payment_method,
                pm.delivery_method,
                pm.method_id AS order_id
            FROM purchase_method pm
            JOIN book_info b ON pm.book_id = b.book_id
            WHERE pm.purchase_id = %s
            ORDER BY pm.method_id DESC
            """, (reader_id,))
            return cursor.fetchall()

    except Exception as e:
        print(f"数据库查询出错: {e}")
        return []
    finally:
        if connection:
            connection.close()

def format_contact(contact):
    """格式化联系方式以适应表格显示"""
    if '@' in contact:  # 邮箱
        return contact[:15] + '...' if len(contact) > 18 else contact
    elif len(contact) > 15:  # 长地址
        return contact[:12] + '...'
    return contact

def print_reader_stats_report():
    """打印读者购书统计报表"""
    print("\n" + "="*80)
    print("读者购书情况统计报表".center(80))
    print("="*80)

    # 获取读者统计数据
    reader_stats = get_reader_purchase_stats()

    if not reader_stats:
        print("未找到读者购书数据")
        return

    # 创建主表格
    main_table = PrettyTable()
    main_table.field_names = [
        "ID", "姓名", "性别", "年龄", "联系方式", "订单数",
        "购书数", "花费总额", "均价", "主要支付", "主要配送"
    ]

    # 设置表格对齐方式
    main_table.align["ID"] = "r"
    main_table.align["姓名"] = "l"
    main_table.align["花费总额"] = "r"
    main_table.align["均价"] = "r"
    main_table.align["订单数"] = "r"
    main_table.align["购书数"] = "r"

    # 添加数据到主表格
    for reader in reader_stats:
        main_table.add_row([
            reader['purchase_id'],
            reader['name'],
            reader['gender'],
            reader['age'] if reader['age'] else "未知",
            format_contact(reader['contact']),
            reader['total_orders'] or 0,
            reader['unique_books'] or 0,
            f"¥{reader['total_spent']:.2f}" if reader['total_spent'] else "¥0.00",
            f"¥{reader['avg_price']:.2f}" if reader['avg_price'] else "-",
            reader['top_payment'] or "无",
            reader['top_delivery'] or "无"
        ])

    # 打印主表格
    print(main_table)

    # 计算整体统计
    total_readers = len(reader_stats)
    active_readers = sum(1 for r in reader_stats if r['total_orders'] > 0)
    total_orders = sum(r['total_orders'] or 0 for r in reader_stats)
    total_spent = sum(r['total_spent'] or 0 for r in reader_stats)

    print(f"\n统计摘要:".ljust(25) +
          f"读者总数: {total_readers}人 | " +
          f"活跃读者: {active_readers}人 | " +
          f"总订单数: {total_orders}笔 | " +
          f"总收入: ¥{total_spent:.2f}")

    # 打印流行书目信息
    query_popular_book.query_popular_book()

    # 打印活跃客户信息
    query_active_buyer.query_active_buyer()

    # 打印读者详情选项
    print("\n输入读者ID查看详细购书清单 (输入0退出)")
    try:
        while True:
            reader_id = input("请输入读者ID: ").strip()
            if not reader_id or reader_id == '0':
                break

            if not reader_id.isdigit():
                print("请输入有效的数字ID")
                continue

            reader_id = int(reader_id)
            if not any(r['purchase_id'] == reader_id for r in reader_stats):
                print(f"未找到ID为 {reader_id} 的读者")
                continue

            print_reader_book_details(reader_id)

    except KeyboardInterrupt:
        print("\n程序已终止")

def print_reader_book_details(reader_id):
    """打印指定读者的详细购书清单"""
    # 获取读者基本信息
    connection = pymysql.connect(**DB_CONFIG)
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM buyer_info WHERE purchase_id = %s", (reader_id,))
        reader_info = cursor.fetchone()

    if not reader_info:
        print(f"未找到ID为 {reader_id} 的读者信息")
        return

    # 获取购书详情
    book_details = get_reader_book_details(reader_id)

    # 打印读者信息标题
    print("\n" + "="*80)
    print(f"读者购书详情 - {reader_info['name']} (ID: {reader_id})".center(80))
    print("="*80)
    print(f"性别: {reader_info['gender']} | 年龄: {reader_info.get('age', '未知')} | 联系方式: {reader_info['contact']}")

    if not book_details:
        print("\n该读者暂无购书记录")
        return

    # 创建详情表格
    detail_table = PrettyTable()
    detail_table.field_names = ["订单ID", "图书ID", "图书名称", "类别", "价格", "支付方式", "配送方式"]

    # 设置表格对齐方式
    detail_table.align["订单ID"] = "r"
    detail_table.align["图书ID"] = "r"
    detail_table.align["价格"] = "r"
    detail_table.align["类别"] = "l"

    # 添加数据到详情表格
    total_spent = 0
    for book in book_details:
        # 处理长书名 - 每30字符换行
        book_name = textwrap.fill(book['book_name'], width=30)
        detail_table.add_row([
            book['order_id'],
            book['book_id'],
            book_name,
            book['book_category'],
            f"¥{book['price']:.2f}",
            book['payment_method'],
            book['delivery_method']
        ])
        total_spent += book['price']

    # 打印详情表格
    print(detail_table)

    # 打印统计信息
    print(f"\n购书统计: ".ljust(15) +
          f"总购书数: {len(book_details)}本 | " +
          f"总花费: ¥{total_spent:.2f} | " +
          f"平均每本: ¥{total_spent/len(book_details):.2f}")

    # 分类统计
    category_count = {}
    for book in book_details:
        category = book['book_category']
        category_count[category] = category_count.get(category, 0) + 1

    print("图书类别分布: " + ", ".join([f"{cat}({count})" for cat, count in category_count.items()]))

    # 支付方式统计
    payment_count = {}
    for book in book_details:
        payment = book['payment_method']
        payment_count[payment] = payment_count.get(payment, 0) + 1

    print("支付方式分布: " + ", ".join([f"{pay}({count})" for pay, count in payment_count.items()]))

if __name__ == "__main__":
    print_reader_stats_report()