# 🚀 Railway ga Deploy Qilish - To'liq Qo'llanma

## 1-QADAM: Railway Account Yaratish

### 1.1 Railway Website ga Kiring
```
1. Brauzer oching
2. https://railway.app ga kiring
3. "Get Started" tugmasini bosing
```

### 1.2 GitHub bilan Ro'yxatdan O'ting
```
1. "Sign up with GitHub" tugmasini bosing
2. GitHub sahifasida "Authorize Railway" tugmasini bosing
3. Railway ga qaytib keladi
4. Email tasdiqlang (agar so'rasa)
```

## 2-QADAM: Loyihangizni Deploy Qilish

### 2.1 Yangi Project Yaratish
```
1. Railway dashboard da "New Project" tugmasini bosing
2. "Deploy from GitHub repo" ni tanlang
3. GitHub repositorylaringiz ro'yxati ko'rinadi
```

### 2.2 Repository ni Tanlash
```
1. "suxideveloper/Asil" repository ni toping
2. Uning ustiga bosing
3. "Deploy" tugmasini bosing
```

### 2.3 Railway Avtomatik Sozlash
```
Railway avtomatik ravishda:
✅ Django project ekanligini aniqlaydi
✅ requirements.txt ni o'qiydi
✅ Procfile ni o'qiydi
✅ Gunicorn ni sozlaydi
✅ Environment variables ni o'rnatadi
```

## 3-QADAM: Deployment Jarayoni

### 3.1 Build Jarayoni
```
Railway quyidagilarni bajaradi:
🔄 Dependencies o'rnatadi (pip install)
🔄 Database migration ishlatadi
🔄 Static files yig'adi
🔄 Admin user yaratadi (admin/admin123)
🔄 Gunicorn server ishga tushiradi
```

### 3.2 Deployment Muvaffaqiyatli
```
✅ "Deployment successful" xabari ko'rinadi
✅ App URL beriladi: https://your-app.up.railway.app
✅ "View Logs" tugmasi ko'rinadi
```

## 4-QADAM: Admin User Yaratish

### 4.1 Railway Shell ga Kiring
```
1. Railway dashboard da loyihangiz ustiga bosing
2. "Shell" tab ni bosing
3. "Connect" tugmasini bosing
```

### 4.2 Admin User Yaratish
```
Shell da quyidagi buyruqni kiriting:
python manage.py shell --settings=asliddin_education.settings_production
```

### 4.3 Python Shell da
```python
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
print('✅ Admin user yaratildi!')
exit()
```

## 5-QADAM: Loyihangizni Test Qilish

### 5.1 Website ni Tekshiring
```
1. Railway dan berilgan URL ga kiring
2. "Asliddin Kurbanov Education Center" sahifasi ko'rinishi kerak
3. Barcha sahifalar ishlashi kerak (About, Teachers, Courses, etc.)
```

### 5.2 Admin Panel ni Tekshiring
```
1. URL oxiriga /admin/ qo'shing
2. Login sahifasi ko'rinishi kerak
3. Username: admin
4. Password: admin123
5. Admin panel ochilishi kerak
```

### 5.3 Admin Panel da Tekshiring
```
✅ Teachers - 6 ta teacher ko'rinishi kerak
✅ Students - 15 ta student ko'rinishi kerak
✅ Courses - 9 ta course ko'rinishi kerak
✅ Graduates - 12 ta graduate ko'rinishi kerak
✅ Achievements - 12 ta achievement ko'rinishi kerak
```

## 6-QADAM: Muammolar Hal Qilish

### 6.1 Agar Build Xatosi Bo'lsa
```
1. Railway dashboard da "View Logs" ni bosing
2. Xatolarni o'qing
3. Ko'pincha requirements.txt da muammo bo'ladi
```

### 6.2 Agar Admin Panel Ishlamasa
```
1. Admin user yaratilganini tekshiring
2. Qayta admin user yarating
3. Django logs ni tekshiring
```

### 6.3 Agar Static Files Yuklanmasa
```
1. collectstatic ishlaganini tekshiring
2. STATIC_ROOT sozlamasini tekshiring
3. staticfiles/ papkasini tekshiring
```

## 7-QADAM: Muvaffaqiyat!

### 7.1 Sizning Appingiz
```
🌐 Website: https://your-app.up.railway.app
🔐 Admin: https://your-app.up.railway.app/admin/
👤 Login: admin / admin123
```

### 7.2 Railway Dashboard
```
- Logs ko'rish
- Usage monitoring
- Auto-deploy (GitHub push = auto-deploy)
- Custom domains
- Environment variables
```

## 🎯 Railway Free Tier
- ✅ $5 credit oyiga (kichik applar uchun yetadi)
- ✅ 512MB RAM
- ✅ Avtomatik uyqu (5 daqiqa ishlatmasa)
- ✅ Custom domains
- ✅ SSL sertifikatlar

## 🆘 Yordam
Agar muammo bo'lsa:
1. Railway logs ni tekshiring
2. GitHub repository ni tekshiring
3. Django settings ni tekshiring

**Jami vaqt: 5-10 daqiqa! 🚀**
