import pymysql

# 连接本地MySQL服务器（请替换为你的实际凭据）
connection = pymysql.connect(
    host='localhost',
    user='root',        # 替换为你的MySQL用户名
    password='123098',  # 替换为你的MySQL密码
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        # 创建数据库
        cursor.execute("CREATE DATABASE IF NOT EXISTS bookstore DEFAULT CHARACTER SET utf8mb4")
        cursor.execute("USE bookstore")

        # 创建书籍信息表（保持不变）
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS book_info (
            book_id INT AUTO_INCREMENT PRIMARY KEY,
            book_category VARCHAR(50) NOT NULL,
            book_name VARCHAR(100) NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            introduction TEXT
        )
        """)

        # 创建购书者信息表（删除purchased_book字段）
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS buyer_info (
            purchase_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            gender ENUM('男', '女', '其他') NOT NULL,
            age INT,
            contact VARCHAR(100)
        )
        """)

        # 创建购买方式表（添加purchase_id和book_id字段）
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS purchase_method (
            method_id INT AUTO_INCREMENT PRIMARY KEY,
            purchase_id INT NOT NULL,
            book_id INT NOT NULL,
            payment_method VARCHAR(50) NOT NULL,
            delivery_method VARCHAR(50) NOT NULL,
            FOREIGN KEY (purchase_id) REFERENCES buyer_info(purchase_id),
            FOREIGN KEY (book_id) REFERENCES book_info(book_id)
        )
        """)

    # 提交执行
    connection.commit()
    print("三张表创建成功！表结构已更新：")
    print("1. buyer_info表删除了purchased_book字段")
    print("2. purchase_method表添加了purchase_id和book_id字段")

except Exception as e:
    print(f"操作出错: {e}")
    connection.rollback()

finally:
    connection.close()