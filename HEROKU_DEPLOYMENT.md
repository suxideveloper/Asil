# Heroku Deployment Guide

## Step 1: Install Heroku CLI

```bash
# Ubuntu/Debian
curl https://cli-assets.heroku.com/install.sh | sh

# Or download from https://devcenter.heroku.com/articles/heroku-cli
```

## Step 2: Prepare for Heroku

1. **Create `runtime.txt`:**
```
python-3.12.0
```

2. **Update `Procfile` (already done):**
```
web: python manage.py collectstatic --noinput --settings=asliddin_education.settings_production && python manage.py migrate --settings=asliddin_education.settings_production && python manage.py shell --settings=asliddin_education.settings_production -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').delete(); User.objects.create_superuser('admin', 'admin@example.com', 'admin123'); print('✅ Admin user created');" && gunicorn asliddin_education.wsgi:application --bind 0.0.0.0:\$PORT --workers 2 --timeout 120
```

## Step 3: Deploy to Heroku

1. **Login to Heroku:**
```bash
heroku login
```

2. **Create Heroku App:**
```bash
heroku create your-app-name
```

3. **Set Environment Variables:**
```bash
heroku config:set DJANGO_SETTINGS_MODULE=asliddin_education.settings_production
heroku config:set SECRET_KEY=your-secret-key-here
```

4. **Deploy:**
```bash
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

5. **Create Admin User:**
```bash
heroku run python manage.py shell --settings=asliddin_education.settings_production -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin123')"
```

## Step 4: Access Your App

- **Website**: `https://your-app-name.herokuapp.com`
- **Admin**: `https://your-app-name.herokuapp.com/admin/`

## Heroku Free Tier (Limited)

- **550-1000 dyno hours/month**
- **512MB RAM**
- **Sleeps after 30 minutes** of inactivity
- **Custom domains** supported
- **SSL** included
