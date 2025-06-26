import pymysql
import random
from faker import Faker

# 初始化Faker生成中文随机数据
fake = Faker('zh_CN')

# 连接本地MySQL服务器
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='123098',  # 替换为你的MySQL密码
    database='bookstore',      # 确保使用之前创建的数据库
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# 付款方式选项
payment_methods = ["支付宝", "微信支付", "银行卡", "信用卡", "货到付款", "PayPal"]
delivery_methods = ["快递", "平邮", "自提", "电子书", "同城闪送"]

def generate_purchase_data(num_orders, book_ids, buyer_ids):
    purchases = []

    # 确保至少为每个购买者和每本书生成一条记录
    for buyer_id in buyer_ids:
        book_id = random.choice(book_ids)
        payment = random.choice(payment_methods)
        delivery = random.choice(delivery_methods)
        purchases.append((buyer_id, book_id, payment, delivery))

    # 生成额外的随机订单
    for _ in range(num_orders - len(buyer_ids)):
        buyer_id = random.choice(buyer_ids)
        book_id = random.choice(book_ids)
        payment = random.choice(payment_methods)
        delivery = random.choice(delivery_methods)
        purchases.append((buyer_id, book_id, payment, delivery))

    return purchases

try:
    with connection.cursor() as cursor:
        # 获取所有图书ID
        cursor.execute("SELECT book_id FROM book_info")
        book_ids = [row['book_id'] for row in cursor.fetchall()]
        print(f"获取到 {len(book_ids)} 本书籍ID")

        # 获取所有购书者ID
        cursor.execute("SELECT purchase_id FROM buyer_info")
        buyer_ids = [row['purchase_id'] for row in cursor.fetchall()]
        print(f"获取到 {len(buyer_ids)} 位购书者ID")

        # 生成100条随机订单数据
        purchases = generate_purchase_data(100, book_ids, buyer_ids)

        # 插入数据到purchase_method表
        sql = """
        INSERT INTO purchase_method (purchase_id, book_id, payment_method, delivery_method)
        VALUES (%s, %s, %s, %s)
        """

        cursor.executemany(sql, purchases)
        connection.commit()
        print(f"成功插入 {len(purchases)} 条订单数据！")

        # 打印订单统计信息
        cursor.execute("""
        SELECT 
            COUNT(*) AS total_orders,
            COUNT(DISTINCT purchase_id) AS unique_buyers,
            COUNT(DISTINCT book_id) AS unique_books
        FROM purchase_method
        """)
        stats = cursor.fetchone()
        print(f"\n订单统计:")
        print(f"总订单数: {stats['total_orders']}")
        print(f"涉及购书者: {stats['unique_buyers']}人")
        print(f"涉及图书: {stats['unique_books']}本")

        # 打印最受欢迎的付款方式和发货方式
        cursor.execute("""
        SELECT 
            payment_method, 
            COUNT(*) AS count,
            ROUND(COUNT(*)*100.0/(SELECT COUNT(*) FROM purchase_method), 1) AS percentage
        FROM purchase_method
        GROUP BY payment_method
        ORDER BY count DESC
        """)
        print("\n付款方式分布:")
        for row in cursor.fetchall():
            print(f"{row['payment_method']}: {row['count']}单 ({row['percentage']}%)")

        cursor.execute("""
        SELECT 
            delivery_method, 
            COUNT(*) AS count,
            ROUND(COUNT(*)*100.0/(SELECT COUNT(*) FROM purchase_method), 1) AS percentage
        FROM purchase_method
        GROUP BY delivery_method
        ORDER BY count DESC
        """)
        print("\n发货方式分布:")
        for row in cursor.fetchall():
            print(f"{row['delivery_method']}: {row['count']}单 ({row['percentage']}%)")

except Exception as e:
    print(f"操作出错: {e}")
    connection.rollback()

finally:
    connection.close()