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

# 图书种类列表
categories = [
    "文学小说", "科幻奇幻", "悬疑推理", "历史传记",
    "经济管理", "计算机科学", "心理学", "教育学习",
    "艺术设计", "旅游地理", "健康养生", "儿童读物"
]

# 生成随机图书数据
def generate_book_data(num_books):
    books = []
    for _ in range(num_books):
        category = random.choice(categories)

        # 根据不同种类生成相应名称
        if category == "文学小说":
            name = f"{fake.last_name()}的{random.choice(['故事', '人生', '回忆', '旅程'])}"
        elif category == "科幻奇幻":
            name = f"{random.choice(['星际', '时间', '量子', '未来'])}{random.choice(['漫游', '战争', '传奇', '之谜'])}"
        elif category == "计算机科学":
            name = f"{random.choice(['Python', 'Java', 'C++', 'JavaScript'])}{random.choice(['编程', '实战', '入门', '高级'])}"
        elif category == "心理学":
            name = f"{random.choice(['认知', '情绪', '社会', '发展'])}心理学{random.choice(['导论', '研究', '应用', '手册'])}"
        else:
            name = f"{fake.bs().split()[0]}{random.choice(['导论', '研究', '艺术', '之旅', '手册'])}"

        # 生成价格和简介
        price = round(random.uniform(25.0, 150.0), 2)
        introduction = fake.paragraph(nb_sentences=3)

        books.append((category, name, price, introduction))
    return books

try:
    with connection.cursor() as cursor:
        # 生成20本随机图书数据
        books = generate_book_data(30)

        # 插入数据到book_info表
        sql = """
        INSERT INTO book_info (book_category, book_name, price, introduction)
        VALUES (%s, %s, %s, %s)
        """

        cursor.executemany(sql, books)
        connection.commit()
        print(f"成功插入 {len(books)} 条图书数据！")

except Exception as e:
    print(f"操作出错: {e}")
    connection.rollback()

finally:
    connection.close()