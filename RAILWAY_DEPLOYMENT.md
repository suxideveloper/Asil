# Railway Deployment Guide

## Step 1: Prepare Your Project

Your project is already configured for Railway deployment with:
- ✅ `Procfile` for Gunicorn
- ✅ `settings_production.py` for production
- ✅ `requirements.txt` with all dependencies
- ✅ Static files configuration

## Step 2: Deploy to Railway

### Option A: Deploy from GitHub (Recommended)

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Ready for Railway deployment"
   git push origin main
   ```

2. **Connect to Railway:**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Railway will automatically detect Django and deploy

3. **Set Environment Variables (Optional):**
   - Go to your project settings
   - Add `SECRET_KEY` environment variable with a secure key

### Option B: Deploy with Railway CLI

1. **Install Railway CLI:**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login and Deploy:**
   ```bash
   railway login
   railway init
   railway up
   ```

## Step 3: Access Your Application

After deployment, Railway will provide you with a URL like:
- **Website**: `https://your-app-name.up.railway.app`
- **Admin Panel**: `https://your-app-name.up.railway.app/admin/`
  - Username: `admin`
  - Password: `admin123`

## Step 4: Verify Deployment

1. **Check Website**: Visit your Railway URL
2. **Check Admin**: Go to `/admin/` and login with admin/admin123
3. **Check Data**: Verify all your teachers, students, and courses are loaded

## Troubleshooting

If you encounter issues:

1. **Check Logs**: Go to Railway dashboard → View Logs
2. **Common Issues**:
   - Static files not loading: Check `STATIC_ROOT` setting
   - Admin not accessible: Verify superuser creation in Procfile
   - Database errors: Check migration status

## Railway Free Tier Limits

- **$5 credit monthly** (usually enough for small Django apps)
- **512MB RAM**
- **1GB storage**
- **Automatic sleep** after 5 minutes of inactivity
- **Custom domains** supported

## Production Tips

1. **Set a strong SECRET_KEY** in environment variables
2. **Use Railway's PostgreSQL** for production (free tier available)
3. **Enable HTTPS** (automatic with Railway)
4. **Monitor usage** in Railway dashboard
