# Zentro - Production Deployment Guide

## 🚀 Deployment on Render

### Prerequisites
- Render account (https://render.com)
- GitHub repository with this project
- Environment variables configured

### Environment Variables Required

Set these in your Render dashboard:

```
SECRET_KEY=your-secret-django-key-here
DEBUG=False
DATABASE_URL=your-database-url-here
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
RAILWAY_PUBLIC_DOMAIN=your-domain.com
```

### Deployment Steps

1. **Connect Repository**
   - Go to Render Dashboard
   - Create New → Web Service
   - Connect your GitHub repository

2. **Configure Build Command**
   - Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - Start Command: `gunicorn zentro_config.wsgi:application`

3. **Environment Setup**
   - Add environment variables from "Environment Variables Required" section
   - Use PostgreSQL for production database (recommended)

4. **Deploy**
   - Click Deploy
   - Monitor logs for any errors

### Database Migration

Render will run migrations automatically based on the build command. If you need to manually run migrations:

```bash
python manage.py migrate
```

### Static Files

Static files are automatically handled by WhiteNoise middleware. No additional configuration needed.

### Monitoring

- Check Render logs for errors
- Monitor application performance
- Set up error alerts if available

## 🔧 Local Development

### Setup
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate
# Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### Access Points
- Website: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/

## 📋 Production Checklist

- [ ] SECRET_KEY is set in environment (not hardcoded)
- [ ] DEBUG=False in production
- [ ] ALLOWED_HOSTS configured correctly
- [ ] CSRF_TRUSTED_ORIGINS set for your domain
- [ ] Database credentials in environment variables
- [ ] Static files collected (`python manage.py collectstatic`)
- [ ] HTTPS enforced (configured in settings.py)
- [ ] HSTS headers enabled
- [ ] XSS protection enabled
- [ ] Email configured for password resets
- [ ] Backups configured for database

## 🔐 Security Notes

- Never commit `.env` files
- Use strong SECRET_KEY in production
- Enable HTTPS/SSL certificate
- Regular security updates for dependencies
- Monitor logs for suspicious activity

## 📦 Dependencies

Core dependencies for production:
- Django 4.2.0
- gunicorn 21.2.0
- whitenoise 6.5.0
- psycopg2-binary (for PostgreSQL)
- python-decouple (for environment management)
- dj-database-url (for DATABASE_URL parsing)
- Pillow (for image handling)

## 🐛 Troubleshooting

### Static files not loading
- Run: `python manage.py collectstatic --noinput`
- Check STATIC_ROOT and STATIC_URL in settings

### Database connection fails
- Verify DATABASE_URL format
- Check database credentials
- Ensure database server is running

### 502 Bad Gateway
- Check application logs
- Verify gunicorn is running
- Check Python version compatibility

## 📞 Support

For issues, check:
1. Django documentation: https://docs.djangoproject.com
2. Render documentation: https://render.com/docs
3. Application logs in Render dashboard
