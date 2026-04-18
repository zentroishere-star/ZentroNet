# Complete Deployment Guide: GitHub + Render

## ✅ PROJECT STATUS
- ✓ Django checks: PASSED
- ✓ Development server: WORKING on http://127.0.0.1:8000/
- ✓ All migrations: APPLIED
- ✓ Static files: READY
- ✓ Production-ready security: CONFIGURED

---

## 📋 TABLE OF CONTENTS
1. [GitHub Setup (NEW USER)](#github-setup)
2. [Push to GitHub](#push-to-github)
3. [Render Deployment](#render-deployment)
4. [Troubleshooting](#troubleshooting)

---

## GITHUB SETUP

### Step 1: Create GitHub Account (if you don't have one)
1. Go to https://github.com
2. Click "Sign up"
3. Enter email, password, username
4. Verify email
5. Complete setup

### Step 2: Create a New Repository on GitHub
1. Go to https://github.com/new
2. **Repository name:** `zentro-portfolio` (or any name you like)
3. **Description:** `Professional Portfolio Website with WhatsApp Integration`
4. **Visibility:** Choose `Public` (required for free Render deployment)
5. Click **"Create repository"**
6. **COPY the repository URL** (looks like: `https://github.com/YOUR-USERNAME/zentro-portfolio.git`)

### Step 3: Configure Git Locally (One-time setup)
Run these commands in PowerShell:

```powershell
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Example:
```powershell
git config --global user.name "Gokul"
git config --global user.email "gokul@example.com"
```

---

## PUSH TO GITHUB

### Step 1: Add Remote Repository
Navigate to project directory and run:

```powershell
cd "d:\Zentro 3\Zentro 3\zentro_project"
git remote add origin https://github.com/YOUR-USERNAME/zentro-portfolio.git
```

Replace `YOUR-USERNAME` with your actual GitHub username!

### Step 2: Verify Remote Added
```powershell
git remote -v
```

You should see:
```
origin  https://github.com/YOUR-USERNAME/zentro-portfolio.git (fetch)
origin  https://github.com/YOUR-USERNAME/zentro-portfolio.git (push)
```

### Step 3: Push to GitHub
```powershell
git branch -M main
git push -u origin main
```

This will:
- Rename your branch to `main`
- Upload all your code to GitHub
- You might see a prompt to authenticate - follow the instructions

---

## RENDER DEPLOYMENT

### Step 1: Create Render Account
1. Go to https://render.com
2. Click **"Sign up"**
3. Choose **"Sign up with GitHub"**
4. Authorize Render to access your GitHub
5. Verify email

### Step 2: Connect GitHub Repository
1. Go to https://dashboard.render.com
2. Click **"New +"** button
3. Select **"Web Service"**
4. Click **"Connect a repository"**
5. Search for `zentro-portfolio` (or your repo name)
6. Click **"Connect"**

### Step 3: Configure Web Service

**Fill in these fields:**

| Field | Value |
|-------|-------|
| Name | `zentro-portfolio` |
| Environment | `Python 3` |
| Region | `Oregon` (or closest to you) |
| Branch | `main` |
| Build Command | `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate` |
| Start Command | `gunicorn zentro_config.wsgi:application` |
| Instance Type | `Free` |

### Step 4: Add Environment Variables
1. Scroll down to **"Environment"** section
2. Click **"Add Environment Variable"**
3. Add these variables (copy-paste each one):

```
SECRET_KEY = django-insecure-zentro-production-key-change-me-12345
DEBUG = False
ALLOWED_HOSTS = your-app-name.onrender.com,www.your-app-name.onrender.com
DATABASE_URL = sqlite:///db.sqlite3
RAILWAY_PUBLIC_DOMAIN = your-app-name.onrender.com
```

**Important for SECRET_KEY:**
- Generate a proper key at: https://miniwebtool.com/django-secret-key-generator/
- Copy the generated key and paste it as `SECRET_KEY` value

### Step 5: Deploy
1. Click **"Create Web Service"**
2. Wait for deployment (takes 2-3 minutes)
3. You'll see logs in real-time
4. Once complete, you get a URL like: `https://zentro-portfolio.onrender.com`

---

## VERIFY DEPLOYMENT

### Check If Live
1. Go to your Render URL (shown in dashboard)
2. Should see your Zentro portfolio website
3. Check http://your-app-name.onrender.com/admin (should show login)

### View Logs
1. In Render dashboard, click your service
2. Click **"Logs"** tab
3. Check for any errors

---

## TROUBLESHOOTING

### Problem: Build Failed
**Solution:**
1. Check Render logs for exact error
2. Common issues:
   - Missing environment variables
   - Wrong SECRET_KEY format
   - Database connection issue

### Problem: Site Shows Error 503
**Solution:**
- Wait 5 minutes (Render might still be starting)
- Check logs for errors
- Restart service: Click "Manual Deploy" in Render

### Problem: Static Files Not Loading
**Solution:**
- Run manual deploy
- Check if `collectstatic` command succeeded in logs

### Problem: Admin Login Doesn't Work
**Solution:**
- Create new superuser via Render console:
  ```
  python manage.py createsuperuser
  ```

---

## FINAL CHECKLIST

- [ ] GitHub account created
- [ ] Repository created on GitHub
- [ ] Code pushed to GitHub (all files visible)
- [ ] Render account created
- [ ] GitHub connected to Render
- [ ] Web Service configured
- [ ] Environment variables added
- [ ] Deployment started
- [ ] Website is live at Render URL
- [ ] Admin panel accessible
- [ ] All pages loading correctly

---

## NEXT STEPS (Optional)

1. **Custom Domain** (if you own a domain):
   - Go to Render > Settings > Custom Domain
   - Add your domain
   - Update DNS settings (Render provides instructions)

2. **Auto-Deploy on Git Push** (already enabled):
   - Every time you push to GitHub, Render auto-deploys

3. **Email Configuration** (for contact form):
   - Update EMAIL settings in settings.py
   - Add email environment variables

4. **PostgreSQL Database** (for production):
   - In Render, create PostgreSQL database
   - Use DATABASE_URL from database credentials

---

## SUPPORT RESOURCES

- Render Docs: https://render.com/docs
- Django Docs: https://docs.djangoproject.com
- GitHub Help: https://docs.github.com
- WhiteNoise: https://whitenoise.readthedocs.io/

---

**Good luck with your deployment! 🚀**
