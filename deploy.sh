#!/bin/bash

# Django Education Center Deployment Script
# This script prepares your project for deployment

echo "🚀 Preparing Django Education Center for deployment..."

# Check if virtual environment is activated
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "⚠️  Please activate your virtual environment first:"
    echo "   source venv/bin/activate"
    exit 1
fi

# Collect static files
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput --settings=asliddin_education.settings_production

# Run migrations
echo "🗄️  Running database migrations..."
python manage.py migrate --settings=asliddin_education.settings_production

# Create admin user
echo "👤 Creating admin user..."
python manage.py shell --settings=asliddin_education.settings_production -c "
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.filter(username='admin').delete()
User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
print('✅ Admin user created successfully!')
"

# Check deployment readiness
echo "🔍 Checking deployment configuration..."
python manage.py check --settings=asliddin_education.settings_production

echo ""
echo "✅ Your Django Education Center is ready for deployment!"
echo ""
echo "📋 Next steps:"
echo "1. Choose a hosting platform (Railway, Render, Heroku, or PythonAnywhere)"
echo "2. Follow the deployment guide for your chosen platform"
echo "3. Your admin credentials:"
echo "   - Username: admin"
echo "   - Password: admin123"
echo ""
echo "🌐 Deployment guides created:"
echo "   - RAILWAY_DEPLOYMENT.md"
echo "   - RENDER_DEPLOYMENT.md" 
echo "   - HEROKU_DEPLOYMENT.md"
echo "   - PYTHONANYWHERE_DEPLOYMENT.md"
echo ""
echo "🎯 Recommended: Railway (easiest) or Render (most reliable)"
