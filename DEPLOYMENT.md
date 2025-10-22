# Asliddin Kurbanov Education Center - Deployment Guide

Bu loyihani tekin serverga qo'yish uchun bir nechta variant mavjud. Eng oson va mashhur variantlarni ko'rib chiqamiz:

## 🚀 Tekin Hosting Variantlari

### 1. **Railway** (Tavsiya etiladi)
- **URL**: https://railway.app
- **Tezlik**: Juda tez
- **Qulaylik**: Git bilan avtomatik deployment
- **Tezlik**: 500MB RAM, 1GB storage

### 2. **Render**
- **URL**: https://render.com
- **Tezlik**: Tez
- **Qulaylik**: GitHub bilan integratsiya
- **Tezlik**: 512MB RAM

### 3. **Heroku** (Murakkab)
- **URL**: https://heroku.com
- **Eslatma**: Endi tekin tier yo'q, lekin $5/oy

### 4. **PythonAnywhere**
- **URL**: https://pythonanywhere.com
- **Qulaylik**: Python uchun maxsus
- **Tezlik**: 512MB RAM

## 📋 Deployment Qadamlari

### Railway orqali (Tavsiya etiladi)

1. **GitHub'ga yuklash**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/asliddin-education.git
   git push -u origin main
   ```

2. **Railway'da loyiha yaratish**:
   - https://railway.app saytiga kiring
   - GitHub bilan login qiling
   - "New Project" > "Deploy from GitHub repo"
   - Repositoryingizni tanlang

3. **Environment Variables**:
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=False
   ```

4. **Deploy**:
   - Railway avtomatik ravishda deploy qiladi
   - URL beriladi: https://your-app.railway.app

### Render orqali

1. **GitHub'ga yuklash** (yuqoridagi qadamlarni bajaring)

2. **Render'da loyiha yaratish**:
   - https://render.com saytiga kiring
   - GitHub bilan login qiling
   - "New" > "Web Service"
   - Repositoryingizni tanlang

3. **Settings**:
   ```
   Build Command: pip install -r requirements.txt
   Start Command: python manage.py collectstatic --noinput && python manage.py migrate && python manage.py runserver 0.0.0.0:$PORT
   ```

4. **Environment Variables**:
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=False
   ```

### PythonAnywhere orqali

1. **PythonAnywhere'da account yaratish**:
   - https://pythonanywhere.com saytiga kiring
   - Tekin account yarating

2. **Files tab'da loyihani yuklash**:
   - ZIP fayl sifatida yuklang
   - Yoki Git orqali clone qiling

3. **Web tab'da web app yaratish**:
   - "Add a new web app"
   - "Manual configuration"
   - Python 3.10 tanlang

4. **WSGI file'ni sozlash**:
   ```python
   import os
   import sys

   path = '/home/yourusername/asliddin-education'
   if path not in sys.path:
       sys.path.append(path)

   os.environ['DJANGO_SETTINGS_MODULE'] = 'asliddin_education.settings_production'

   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

## 🔧 Mahalliy Tayyorgarlik

### 1. Static files'ni collect qilish
```bash
python manage.py collectstatic --noinput
```

### 2. Database migration
```bash
python manage.py migrate
```

### 3. Superuser yaratish (ixtiyoriy)
```bash
python manage.py createsuperuser
```

## 📝 Muhim Eslatmalar

1. **SECRET_KEY**: Har doim yangi secret key yarating
2. **DEBUG**: Production'da har doim False qiling
3. **ALLOWED_HOSTS**: Domain nomingizni qo'shing
4. **Database**: SQLite ishlatilmoqda, production uchun PostgreSQL tavsiya etiladi

## 🌐 Domain Qo'shish

Agar o'z domainingizni qo'shmoqchi bo'lsangiz:

1. **Domain sotib oling** (Namecheap, GoDaddy, va boshqalar)
2. **DNS sozlamalari**:
   - A record: @ -> server IP
   - CNAME: www -> your-domain.com
3. **ALLOWED_HOSTS**'ga domain qo'shing

## 📞 Yordam

Agar muammo bo'lsa:
1. Log fayllarini tekshiring
2. Django documentation'ni o'qing
3. Hosting provider'ning support'iga murojaat qiling

---

**Asliddin Kurbanov Education Center** - Muvaffaqiyatli deployment! 🎓
