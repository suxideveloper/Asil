# PythonAnywhere Deployment Guide

## Step 1: Create PythonAnywhere Account

1. **Go to [pythonanywhere.com](https://pythonanywhere.com)**
2. **Sign up for free account**
3. **Verify email address**

## Step 2: Upload Your Project

### Option A: Upload via Files Tab
1. **Go to Files tab**
2. **Create new directory**: `asliddin_education`
3. **Upload all your project files** (zip and extract, or upload individually)

### Option B: Clone from GitHub
1. **Go to Consoles tab**
2. **Start a Bash console**
3. **Clone your repository:**
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

## Step 3: Configure Web App

1. **Go to Web tab**
2. **Click "Add a new web app"**
3. **Choose "Manual configuration"**
4. **Select Python 3.12**
5. **Configure paths:**
   - **Source code**: `/home/yourusername/asliddin_education`
   - **Working directory**: `/home/yourusername/asliddin_education`

## Step 4: Configure WSGI

1. **Click on WSGI configuration file**
2. **Replace content with:**
```python
import os
import sys

# Add your project directory to the Python path
path = '/home/yourusername/asliddin_education'
if path not in sys.path:
    sys.path.append(path)

# Set Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'asliddin_education.settings_production'

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

## Step 5: Install Dependencies

1. **Go to Consoles tab**
2. **Start a Bash console**
3. **Navigate to your project:**
```bash
cd /home/yourusername/asliddin_education
```

4. **Install requirements:**
```bash
pip3.12 install --user -r requirements.txt
```

## Step 6: Setup Database and Admin

1. **Run migrations:**
```bash
python3.12 manage.py migrate --settings=asliddin_education.settings_production
```

2. **Create superuser:**
```bash
python3.12 manage.py shell --settings=asliddin_education.settings_production
```
3. **In Python shell:**
```python
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
exit()
```

4. **Collect static files:**
```bash
python3.12 manage.py collectstatic --noinput --settings=asliddin_education.settings_production
```

## Step 7: Access Your App

- **Website**: `https://yourusername.pythonanywhere.com`
- **Admin**: `https://yourusername.pythonanywhere.com/admin/`

## PythonAnywhere Free Tier

- **1 web app**
- **512MB disk space**
- **CPU seconds limited** (usually enough for small apps)
- **Custom domains** supported
- **SSL** included
- **Always online** (no sleep)
