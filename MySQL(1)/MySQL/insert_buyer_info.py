import pymysql
import random
from faker import Faker
import datetime

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

# 生成随机购书者数据
def generate_buyer_data(num_buyers):
    buyers = []
    for _ in range(num_buyers):
        # 随机姓名
        name = fake.name()

        # 随机性别（男、女、其他）
        gender = random.choices(['男', '女', '其他'], weights=[0.48, 0.48, 0.04])[0]

        # 随机年龄（18-70岁）
        age = random.randint(18, 70)

        # 随机联系方式（70%手机，20%邮箱，10%地址）
        contact_type = random.choices(['phone'])[0]

        if contact_type == 'phone':
            contact = fake.phone_number()

        buyers.append((name, gender, age, contact))
    return buyers

try:
    with connection.cursor() as cursor:
        # 生成20位随机购书者数据
        buyers = generate_buyer_data(20)

        # 插入数据到buyer_info表
        sql = """
        INSERT INTO buyer_info (name, gender, age, contact)
        VALUES (%s, %s, %s, %s)
        """

        cursor.executemany(sql, buyers)
        connection.commit()
        print(f"成功插入 {len(buyers)} 条购书者数据！")

        # 打印前5条数据预览
        cursor.execute("SELECT * FROM buyer_info ORDER BY purchase_id DESC LIMIT 5")
        print("\n最新5条购书者数据预览:")
        for buyer in cursor.fetchall():
            print(f"ID:{buyer['purchase_id']} {buyer['name']}({buyer['gender']}, {buyer['age']}岁) - {buyer['contact']}")

except Exception as e:
    print(f"操作出错: {e}")
    connection.rollback()

finally:
    connection.close()