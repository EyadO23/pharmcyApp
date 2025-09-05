# قائمة الأدوية (مبدئياً فارغة)
pharmacy = []

def add_medicine(name, price, quantity):
    medicine = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    pharmacy.append(medicine)
    print(f" تمت إضافة الدواء: {name}")

# تجربة الإضافة
add_medicine("Paracetamol", 5.0, 20)
add_medicine("Amoxicillin", 12.5, 10)

# عرض كل الأدوية
print("\n قائمة الأدوية في الصيدلية:")
for med in pharmacy:
    print(med)
