# 📸 Cloudinary Setup Guide - For Image Persistence

## ❓ Why Cloudinary?

Render has an **ephemeral file system** - any files you upload get deleted when the app restarts. Cloudinary solves this by hosting your images in the cloud.

---

## 🚀 Step 1: Create Free Cloudinary Account

1. Go to: https://cloudinary.com/users/register/free
2. Sign up with your email
3. Verify your email
4. Log in to your dashboard

---

## 🔑 Step 2: Get Your API Credentials

1. After login, go to **Dashboard** (https://console.cloudinary.com/console)
2. You'll see your **Cloud Name** (looks like: `your_cloud_name`)
3. Click on the gear icon (Settings) in top right
4. Go to **API Keys** tab
5. Copy these three values:
   - **Cloud Name**
   - **API Key**
   - **API Secret**

---

## 🔧 Step 3: Configure Render Environment Variables

1. Go to your Render dashboard: https://dashboard.render.com/
2. Click on your **zentro-portfolio** service
3. Click **Environment** tab
4. Add these variables:

```
CLOUDINARY_CLOUD_NAME = your_cloud_name
CLOUDINARY_API_KEY = your_api_key
CLOUDINARY_API_SECRET = your_api_secret
```

5. Click **Save**

---

## ✅ Step 4: Redeploy

1. Click **Manual Deploy** button
2. Click **Deploy latest commit**
3. Wait 2-5 minutes for deployment

---

## 🎉 Done!

After deployment, when you upload images in the admin dashboard, they will:
- ✅ Be stored in Cloudinary (not locally)
- ✅ Persist across app restarts
- ✅ Be available forever
- ✅ Load faster with CDN

---

## 📝 Local Testing (Optional)

If you want to test Cloudinary locally:

1. Create a `.env` file in your project root:
```
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

2. Restart Django server: `python manage.py runserver`
3. Upload images - they'll go to Cloudinary!

---

## 🆓 Free Tier Limits

Cloudinary's free tier includes:
- ✅ 25 GB total storage
- ✅ 25 GB monthly transformations
- ✅ 300,000 total transformations/month
- ✅ Enough for most portfolio sites!

More info: https://cloudinary.com/pricing
