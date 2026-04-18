# 🚂 Railway.app Deployment Guide - Zentro Project

> Your Django Zentro project is ready to go live on Railway.app! Follow these simple steps.

---

## 📋 Step 1: Prepare Your Project

✅ Already Done:
- ✓ `Procfile` created
- ✓ `runtime.txt` configured  
- ✓ `requirements.txt` updated with production packages
- ✓ `settings.py` configured for production

---

## 🚀 Step 2: Deploy to Railway.app

### Option A: Via GitHub (Recommended - Easiest)

1. **Create GitHub Repo** (if not already done)
   ```bash
   cd "d:\Zentro 3\Zentro 3\zentro_project"
   git init
   git add .
   git commit -m "Deploy to Railway"
   git remote add origin https://github.com/YOUR_USERNAME/zentro.git
   git branch -M main
   git push -u origin main
   ```

2. **Go to [Railway.app](https://railway.app)**

3. **Sign Up / Log In** (free account)

4. **Create New Project**
   - Click "Create New Project"
   - Select "Deploy from GitHub"
   - Choose your `zentro` repository
   - Click "Deploy"

5. **Railway auto-deploys!** ✅

### Option B: Via Railway CLI (Alternative)

1. **Install Railway CLI**
   ```bash
   npm install -g @railway/cli
   ```
   (Or use `winget install Railway.cli` on Windows)

2. **Login to Railway**
   ```bash
   railway login
   ```

3. **Initialize Project**
   ```bash
   railway init
   ```

4. **Deploy**
   ```bash
   railway up
   ```

---

## 🔐 Step 3: Configure Environment Variables

After deployment, Railway shows your app URL. Now add these **Environment Variables**:

In Railway Dashboard → Your Project → Variables:

### Required Variables:

```
SECRET_KEY = (generate new one: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
DEBUG = False
ALLOWED_HOSTS = your-railway-domain.up.railway.app
```

### Generate Secret Key:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**Copy the output and paste in Railway Dashboard**

---

## 📊 Step 4: Set Up Database (Choose One)

### Option 1: PostgreSQL (Free on Railway) ⭐ RECOMMENDED
1. In Railway Dashboard → Add Service
2. Select "PostgreSQL"
3. Railway auto-generates `DATABASE_URL` env variable ✅
4. Deploy

### Option 2: Keep SQLite (Simpler, but limited)
- No extra setup needed
- Works for smaller projects
- Data resets if you redeploy

---

## ✅ Step 5: Run Migrations

Railway automatically runs migrations from your Procfile:
```
web: python manage.py migrate && gunicorn zentro_config.wsgi
```

If you need to manually run commands:
```bash
railway run python manage.py migrate
railway run python manage.py createsuperuser
```

---

## 🎉 Step 6: Access Your Live Project

After deployment completes:

- **Website**: `https://your-railway-domain.up.railway.app`
- **Admin Panel**: `https://your-railway-domain.up.railway.app/admin`

**That's it! You're live!** 🎊

---

## 🐛 Troubleshooting

### Problem: "Error: SECRET_KEY not set"
**Solution**: Add `SECRET_KEY` to Railway environment variables

### Problem: "Static files not loading"
**Solution**: Already configured with WhiteNoise. Redeploy if needed.

### Problem: "Database connection failed"
**Solution**: Add PostgreSQL service and set DATABASE_URL

### Problem: "Import errors"
**Solution**: Check requirements.txt is updated. Redeploy.

---

## 📝 Important Notes

- **Auto-scaling**: Railway automatically handles traffic 📈
- **SSL/HTTPS**: Enabled by default ✅
- **Free Tier**: $5 credit/month (usually covers small apps)
- **Custom Domain**: Add under project settings (paid feature)

---

## 🔄 Updating Your App

After making changes locally:

```bash
git add .
git commit -m "Update features"
git push origin main
```

Railway auto-deploys! No manual steps needed.

---

## 📞 Need Help?

- **Railway Docs**: https://docs.railway.app
- **Django Deployment**: https://docs.djangoproject.com/en/4.2/howto/deployment/
- **Status Page**: https://status.railway.app

---

**You're all set, anna! 🚀 Your Zentro project is ready to go global!**
