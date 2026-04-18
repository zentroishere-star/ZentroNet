# ⚡ QUICK COMMANDS - Copy & Paste

## BEFORE YOU START
1. Create GitHub account: https://github.com
2. Create repository on GitHub named `zentro-portfolio`
3. Have your GitHub username ready

---

## COMMAND 1: Configure Git (One-time, if new to Git)
Run in PowerShell:
```powershell
git config --global user.name "Your Name"
git config --global user.email "your-email@gmail.com"
```

Example:
```powershell
git config --global user.name "Gokul"
git config --global user.email "gokul@example.com"
```

---

## COMMAND 2: Add GitHub Remote
Navigate to project and run:
```powershell
cd "d:\Zentro 3\Zentro 3\zentro_project"
git remote add origin https://github.com/YOUR-USERNAME/zentro-portfolio.git
```

**REPLACE `YOUR-USERNAME` with your actual GitHub username!**

Example (not your real username):
```powershell
git remote add origin https://github.com/johndoe/zentro-portfolio.git
```

---

## COMMAND 3: Push to GitHub
Run these commands in order:
```powershell
git branch -M main
git push -u origin main
```

This will upload your code to GitHub.

---

## COMMAND 4: Generate Secure SECRET_KEY
Go to: https://miniwebtool.com/django-secret-key-generator/
Copy the generated key (looks like a long random string)

---

## GITHUB + RENDER DEPLOYMENT STEPS

### On GitHub:
1. ✅ Create repository
2. ✅ Run Command 2 (add remote)
3. ✅ Run Command 3 (push code)
4. ✅ Verify code is on GitHub (https://github.com/YOUR-USERNAME/zentro-portfolio)

### On Render:
1. Create account at https://render.com (use GitHub login)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Fill in:
   - **Name:** `zentro-portfolio`
   - **Build Command:** 
     ```
     pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
     ```
   - **Start Command:** 
     ```
     gunicorn zentro_config.wsgi:application
     ```

5. Add Environment Variables (one by one):
   ```
   SECRET_KEY = [paste your generated key]
   DEBUG = False
   ALLOWED_HOSTS = [your-app-name].onrender.com
   DATABASE_URL = sqlite:///db.sqlite3
   RAILWAY_PUBLIC_DOMAIN = [your-app-name].onrender.com
   ```

6. Click "Create Web Service"
7. Wait for deployment (2-3 minutes)
8. Visit your live site at `https://[your-app-name].onrender.com`

---

## NEED HELP?
- Git issue? Check: https://docs.github.com
- Render issue? Check Render logs: https://render.com/docs
- Django issue? Check: https://docs.djangoproject.com
