import pymysql


def query_active_buyer():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='123098',  # 替换为你的MySQL密码
        database='bookstore',      # 确保使用之前创建的数据库
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            # 查询最活跃的购书者
            cursor.execute("""
            SELECT 
                bi.purchase_id,
                bi.name,
                COUNT(*) AS order_count
            FROM purchase_method pm
            JOIN buyer_info bi ON pm.purchase_id = bi.purchase_id
            GROUP BY bi.purchase_id
            ORDER BY order_count DESC
            LIMIT 5
            """)
            print("\n最活跃的购书者:")
            for i, row in enumerate(cursor.fetchall(), 1):
                print(f"{i}. {row['name']} (ID:{row['purchase_id']}) - {row['order_count']}笔订单")
    except Exception as e:
        print(f"操作出错: {e}")
        connection.rollback()

    finally:
        connection.close()
