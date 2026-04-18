# 🚀 Railway Deployment Checklist

## Before Deployment

- [ ] **GitHub Repository Setup**
  - [ ] Create GitHub account (if needed)
  - [ ] Initialize git: `git init`
  - [ ] Create repo on GitHub
  - [ ] Push your code: `git push -u origin main`

- [ ] **Files Ready** (Already done! ✅)
  - [x] `Procfile` created
  - [x] `runtime.txt` created
  - [x] `requirements.txt` updated
  - [x] `settings.py` configured

- [ ] **Generate Secret Key**
  ```bash
  python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
  ```
  Copy this output!

## During Deployment

- [ ] Create Railway.app account (free)
- [ ] Create new project
- [ ] Connect GitHub repo
- [ ] Railway auto-deploys
- [ ] Add Environment Variables in Railway Dashboard:
  - [ ] `SECRET_KEY` = (paste your generated key)
  - [ ] `DEBUG` = False
  - [ ] `ALLOWED_HOSTS` = (Railway will auto-set)

- [ ] (Optional) Add PostgreSQL database
  - [ ] Click "Add Service" → PostgreSQL
  - [ ] Railway auto-generates DATABASE_URL

## After Deployment

- [ ] Check build logs (green checkmark = success)
- [ ] Visit your live URL
- [ ] Test homepage loads
- [ ] Test admin panel login
- [ ] Create superuser: `railway run python manage.py createsuperuser`

---

## 📊 Current Status

| Component | Status |
|-----------|--------|
| **Procfile** | ✅ Ready |
| **runtime.txt** | ✅ Ready |
| **requirements.txt** | ✅ Updated |
| **settings.py** | ✅ Configured |
| **GitHub** | ⏳ Need to push |
| **Railway.app** | ⏳ Need to deploy |

---

## Quick Commands Reference

### Generate Secret Key
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Push to GitHub
```bash
git add .
git commit -m "Ready for Railway deployment"
git push -u origin main
```

### Create Local .env for testing (optional)
```bash
cp .env.example .env
# Edit .env with your values
```

---

**Next Steps:**
1. Push code to GitHub
2. Go to https://railway.app
3. Follow "Option A: Via GitHub" in RAILWAY_DEPLOYMENT_GUIDE.md
4. Add environment variables
5. Deploy! 🚀
