# قائمة الأدوية كمثال
pharmacy = [
    {"name": "باراسيتامول", "price": 1500, "quantity": 200},
    {"name": "أموكسيسيللين", "price": 2500, "quantity": 10},
    {"name": "إيبوبروفين", "price": 1800, "quantity": 15}
]

def search_medicine(name):
    for med in pharmacy:
        if med["name"] == name:
            return f"تم العثور على الدواء: {med['name']} | السعر: {med['price']} | الكمية: {med['quantity']}"
    return "الدواء غير موجودة."

# تجربة البحث
print(search_medicine("باراسيتامول"))
print(search_medicine("فينيل"))


