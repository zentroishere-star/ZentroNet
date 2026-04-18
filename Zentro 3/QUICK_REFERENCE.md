# ⚡ Zentro - Quick Reference Card

## 🚀 Getting Started (Choose One)

### Windows - Automatic
```bash
setup.bat
```

### Mac/Linux - Automatic
```bash
chmod +x setup.sh
./setup.sh
```

### Manual Setup
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 🌐 Website Access

| URL | Purpose |
|-----|---------|
| http://127.0.0.1:8000/ | Website |
| http://127.0.0.1:8000/admin/ | Admin Panel |
| http://127.0.0.1:8000/login/ | Login |
| http://127.0.0.1:8000/signup/ | Sign Up |

---

## 📊 Admin Panel Tasks

### Add Team Member
```
Admin → Team Members → Add Team Member
→ Fill form → Upload photo → Save
```

### Create Project
```
Admin → Projects → Add Project
→ Fill details → Upload image → Mark featured → Save
```

### View Contact Messages
```
Admin → Contact Messages → View submissions
```

### Manage Newsletter
```
Admin → Newsletter → View subscribers
```

---

## 💻 Django Commands

### Essential
```bash
# Run development server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create admin account
python manage.py createsuperuser

# Load sample data
python manage.py load_sample_data
```

### Testing
```bash
# Run all tests
python manage.py test

# Run specific test
python manage.py test home.tests.ModelTestCase

# Verbose output
python manage.py test -v 2
```

### Database
```bash
# Django shell
python manage.py shell

# Backup data
python manage.py dumpdata > backup.json

# Restore data
python manage.py loaddata backup.json

# Check database
python manage.py dbshell
```

### Static Files
```bash
# Collect static files
python manage.py collectstatic

# Clear cache
python manage.py collectstatic --clear
```

---

## 🔐 Security Checklist

- [ ] Change SECRET_KEY (production)
- [ ] Set DEBUG = False (production)
- [ ] Update ALLOWED_HOSTS
- [ ] Configure email backend
- [ ] Enable HTTPS
- [ ] Set up SSL certificate
- [ ] Configure secure cookies
- [ ] Enable firewall
- [ ] Regular backups
- [ ] Monitor logs

---

## 📁 Key Files to Know

| File | Purpose |
|------|---------|
| settings.py | Configuration |
| models.py | Database models |
| views.py | View logic |
| forms.py | Form validation |
| admin.py | Admin interface |
| base.html | Master template |
| style.css | Styling |
| main.js | JavaScript |

---

## 🎨 Customization Quick Links

### Change Logo
```
static/images/zentro-logo.png
```

### Change Colors
```
static/css/style.css (line ~10)
:root { --primary-color: #F4C430; }
```

### Change Company Name
```
Search for "Zentro" in templates/
templates/base.html (navbar & footer)
```

### Add New Page
```
1. Create template in templates/
2. Create view in views.py
3. Add URL in urls.py
```

---

## 🧪 Testing Commands

```bash
# Test everything
python manage.py test

# Test models only
python manage.py test home.tests.ModelTestCase

# Test views only
python manage.py test home.tests.ViewTestCase

# Test auth
python manage.py test home.tests.AuthenticationTestCase

# Test forms
python manage.py test home.tests.FormTestCase

# With coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html
```

---

## 🚀 Deployment Commands

```bash
# Prepare for production
python manage.py check --deploy

# Collect static files
python manage.py collectstatic --noinput

# Compress static files (optional)
python manage.py compress

# Run with Gunicorn
pip install gunicorn
gunicorn zentro_config.wsgi:application --bind 0.0.0.0:8000

# Run with uWSGI
pip install uwsgi
uwsgi --http :8000 --wsgi-file zentro_config/wsgi.py --master --processes 4
```

---

## 📚 Documentation Files

| File | Content |
|------|---------|
| README.md | Start here! |
| INSTALLATION_GUIDE.md | Setup instructions |
| API_DOCUMENTATION.md | API reference |
| PROJECT_SUMMARY.md | File reference |
| DELIVERY_SUMMARY.md | Complete inventory |
| This file | Quick reference |

---

## ⚙️ Configuration Files

### Django Settings
- **DEBUG**: Set to False in production
- **SECRET_KEY**: Use strong random key
- **ALLOWED_HOSTS**: Add your domain
- **DATABASES**: Use PostgreSQL for production
- **STATIC_URL**: Location of static files
- **MEDIA_URL**: Location of uploads

### Environment Variables (.env)
```
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Port 8000 in use | `python manage.py runserver 8001` |
| Static files not loading | `python manage.py collectstatic` |
| Database error | `python manage.py migrate` |
| Permission denied | `chmod +x manage.py` |
| Module not found | `pip install -r requirements.txt` |

---

## 📞 Getting Help

### Check Documentation
1. README.md - Quick answers
2. INSTALLATION_GUIDE.md - Setup help
3. API_DOCUMENTATION.md - API details
4. PROJECT_SUMMARY.md - File reference
5. Code comments - Inline help

### Django Resources
- Django Docs: https://docs.djangoproject.com/
- Stack Overflow: Search your error
- GitHub Issues: Check project issues

---

## 🎯 Common Workflows

### Add New Feature
```
1. Create model in models.py
2. Create migration: python manage.py makemigrations
3. Apply migration: python manage.py migrate
4. Create view in views.py
5. Add URL in urls.py
6. Create template
7. Test the feature
```

### Add Team Member
```
1. Go to /admin/
2. Click "Team Members"
3. Click "Add Team Member"
4. Fill form
5. Upload photo
6. Save
```

### Create Project
```
1. Go to /admin/
2. Click "Projects"
3. Click "Add Project"
4. Fill form
5. Upload image
6. Save
```

---

## 💾 Database Commands

```bash
# Enter shell
python manage.py shell

# Create object
from home.models import Feature
Feature.objects.create(title="Test", description="Desc", icon="fa-star")

# Query objects
Feature.objects.all()
Feature.objects.filter(is_active=True)
Feature.objects.get(id=1)

# Update object
feature = Feature.objects.get(id=1)
feature.title = "New Title"
feature.save()

# Delete object
feature = Feature.objects.get(id=1)
feature.delete()

# Count objects
Feature.objects.count()
```

---

## 📊 Database Models Quick Reference

```python
# User Model
User.objects.create_user(username='john', email='john@test.com', password='pw123')

# Team Member
TeamMember.objects.create(name='John', role='ceo', email='john@zentro.com')

# Project
Project.objects.create(title='My Project', slug='my-project', description='Desc')

# Feature
Feature.objects.create(title='Feature', description='Desc', icon='fa-star')

# Contact
Contact.objects.create(name='John', email='john@test.com', subject='Subject', message='Msg')

# Newsletter
Newsletter.objects.create(email='john@test.com')

# Testimonial
Testimonial.objects.create(author_name='John', content='Great!', rating=5)
```

---

## 🔑 Important URLs

| URL | Function |
|-----|----------|
| / | Homepage |
| /about/ | About page |
| /projects/ | Projects list |
| /projects/slug/ | Project detail |
| /team/ | Team page |
| /contact/ | Contact form |
| /login/ | Login |
| /signup/ | Sign up |
| /profile/ | User profile |
| /logout/ | Logout |
| /search/ | Search |
| /admin/ | Admin panel |

---

## 🎨 CSS Colors

```css
--primary-color: #F4C430      /* Gold */
--primary-dark: #DAA520       /* Dark Gold */
--dark-bg: #0a0e27            /* Dark Blue */
--light-text: #ffffff         /* White */
--gray-text: #b0b0b0          /* Gray */
--border-color: #2a2f4a       /* Border Gray */
--success-color: #10b981      /* Green */
--error-color: #ef4444        /* Red */
```

---

## 🎓 Python/Django Tips

```python
# Check Django version
import django
print(django.get_version())

# Check Python version
import sys
print(sys.version)

# List all installed packages
pip list

# Upgrade pip
pip install --upgrade pip

# Create requirements file
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt
```

---

## 🚀 Performance Tips

```bash
# Use debug=False
# Use PostgreSQL instead of SQLite
# Enable caching
# Compress static files
# Use CDN for images
# Optimize database queries
# Use database indexing
# Enable gzip compression
# Minimize CSS/JS
```

---

## 📈 Monitoring

### Check Logs
```bash
tail -f logs/django.log
```

### Monitor Performance
```bash
# Use Django Debug Toolbar
pip install django-debug-toolbar

# Use django-extensions
pip install django-extensions
python manage.py shell_plus
```

### Error Tracking
```bash
# Use Sentry
pip install sentry-sdk
```

---

## 🎊 You're All Set!

Your Zentro website is:
- ✅ Installed
- ✅ Configured
- ✅ Ready to use
- ✅ Production-ready

**Start customizing now! 🚀**

---

**Last Updated**: March 25, 2024  
**Status**: ✅ Complete and Production Ready
