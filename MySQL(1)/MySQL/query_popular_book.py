import pymysql

def query_popular_book():
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
            # 查询最受欢迎的图书
            cursor.execute("""
            SELECT 
                b.book_id,
                b.book_name,
                COUNT(*) AS purchase_count
            FROM purchase_method pm
            JOIN book_info b ON pm.book_id = b.book_id
            GROUP BY b.book_id
            ORDER BY purchase_count DESC
            LIMIT 5
            """)
            print("\n最受欢迎的图书:")
            for i, row in enumerate(cursor.fetchall(), 1):
                print(f"{i}. {row['book_name']} (ID:{row['book_id']}) - {row['purchase_count']}次购买")

    except Exception as e:
        print(f"操作出错: {e}")
        connection.rollback()

    finally:
        connection.close()
