import csv

data = [
    {"name": "张三", "age": 25, "city": "北京"},
    {"name": "李四", "age": 30, "city": "上海"},
    {"name": "王五", "age": 28, "city": "深圳"}
]

# 保存
with open('users.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
    writer.writeheader()
    writer.writerows(data)

# 读取
with open('users.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    loaded_data = list(reader)

print(loaded_data)

for index, values in enumerate(loaded_data):
        print(f"\t[ ✅ ] {index}, {values['city']}")