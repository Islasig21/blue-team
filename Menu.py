import xml.etree.ElementTree as ET

tree = ET.parse("simple.xml")
root = tree.getroot()
data = root.findall("food")

My_Menu = []

for food in data:
    name = food.findtext("name")
    price = food.findtext("price")
    description = food.findtext("description")
    calories = food.findtext("calories")

    My_Menu.append({
        "name": name,
        "price": price,
        "description": description,
        "calories": calories
    })

# طباعة المخرجات بشكل مرتب
print(f"{'Name':<30} {'Price':<10} {'Calories':<10} Description")
print("-" * 80)

for item in My_Menu:
    print(f"{item['name']:<30} {item['price']:<10} {item['calories']:<10} {item['description']}")
