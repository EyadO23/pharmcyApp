# قائمة لتخزين المستخدمين
users = []

def create_account(username, password):
    # تحقق إذا المستخدم موجود مسبقًا
    for user in users:
        if user["username"] == username:
            return "اسم المستخدم موجود مسبقًا!"
    
    # إنشاء الحساب
    user = {
        "username": username,
        "password": password  # ملاحظة: للواقع العملي لازم تشفر الباسورد
    }
    users.append(user)
    return f"تم إنشاء الحساب بنجاح للمستخدم: {username}"

# تجربة إنشاء حساب
print(create_account("eyad", "12345"))
print(create_account("mohamed", "abcdef"))
print(create_account("eyad", "67890"))  # محاولة إنشاء مستخدم موجود
