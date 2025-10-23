# Render Deployment Guide

## Step 1: Prepare for Render

1. **Create `render.yaml` file:**
```yaml
services:
  - type: web
    name: asliddin-education
    env: python
    buildCommand: pip install -r requirements.txt && python manage.py collectstatic --noinput --settings=asliddin_education.settings_production && python manage.py migrate --settings=asliddin_education.settings_production
    startCommand: gunicorn asliddin_education.wsgi:application --bind 0.0.0.0:$PORT
    envVars:
      - key: DJANGO_SETTINGS_MODULE
        value: asliddin_education.settings_production
      - key: SECRET_KEY
        generateValue: true
```

2. **Update `requirements.txt`** (already done):
```
asgiref==3.10.0
Django==5.2.7
django-jazzmin==3.0.1
gunicorn==23.0.0
packaging==25.0
pillow==12.0.0
sqlparse==0.5.3
```

## Step 2: Deploy to Render

1. **Go to [render.com](https://render.com)**
2. **Sign up with GitHub**
3. **Click "New" → "Web Service"**
4. **Connect your GitHub repository**
5. **Configure:**
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput --settings=asliddin_education.settings_production && python manage.py migrate --settings=asliddin_education.settings_production`
   - **Start Command**: `gunicorn asliddin_education.wsgi:application --bind 0.0.0.0:$PORT`
   - **Environment**: `DJANGO_SETTINGS_MODULE=asliddin_education.settings_production`

## Step 3: Create Admin User

After deployment, create admin user via Render shell:
1. Go to your service dashboard
2. Click "Shell"
3. Run:
```bash
python manage.py shell --settings=asliddin_education.settings_production
```
4. In Python shell:
```python
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
exit()
```

## Step 4: Access Your App

- **Website**: `https://your-app-name.onrender.com`
- **Admin**: `https://your-app-name.onrender.com/admin/`

## Render Free Tier

- **750 hours/month** (enough for 24/7 if you're the only user)
- **512MB RAM**
- **Automatic sleep** after 15 minutes of inactivity
- **Custom domains** supported
- **SSL certificates** included
