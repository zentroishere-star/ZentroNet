# 🚀 Zentro - Professional Business Website

A complete, production-ready Django website for the Zentro startup with modern design, full authentication, and comprehensive admin panel.

## 🎯 Features

### 🎨 Frontend
- ✅ Responsive, mobile-friendly design
- ✅ Dark theme with golden accents (#F4C430)
- ✅ Smooth animations and transitions
- ✅ Fast loading and SEO optimized
- ✅ Professional UI based on Chauncey.live
- ✅ Interactive forms and real-time validation

### 🔐 Authentication & Security
- ✅ User registration and login
- ✅ Role-based access control
- ✅ CSRF protection on all forms
- ✅ Password hashing with PBKDF2
- ✅ Session management
- ✅ Protected admin panel

### 💾 Database & ORM
- ✅ SQLite3 for development
- ✅ Django ORM for database operations
- ✅ 8+ data models with relationships
- ✅ Automatic timestamps
- ✅ Image handling with Pillow
- ✅ Full database migrations

### 📊 Admin Panel
- ✅ Beautiful customized admin interface
- ✅ Team member management
- ✅ Projects/portfolio management
- ✅ Features management
- ✅ Contact form submissions
- ✅ Testimonials management
- ✅ Newsletter subscriptions
- ✅ User profile management
- ✅ Static page management

### 📝 Content Management
- ✅ Dynamic team members with photos
- ✅ Project portfolio with images
- ✅ Feature cards with icons
- ✅ Testimonials with ratings
- ✅ Contact form with storage
- ✅ Newsletter subscriptions
- ✅ Static page content editor

### 🌐 Pages Included
- ✅ Homepage with hero and features
- ✅ About Us with team
- ✅ Projects/Portfolio
- ✅ Project Details
- ✅ Team Page
- ✅ Contact Page
- ✅ User Profile Page
- ✅ Login/Signup Pages
- ✅ Search Functionality
- ✅ 404 & 500 Error Pages

---

## ⚡ Quick Start

### Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### Installation (5 Minutes)

#### Windows
```bash
# 1. Clone/Extract project
cd zentro_project

# 2. Run setup script
setup.bat

# Follow prompts to create admin account
```

#### Mac/Linux
```bash
# 1. Clone/Extract project
cd zentro_project

# 2. Make setup script executable
chmod +x setup.sh

# 3. Run setup script
./setup.sh

# Follow prompts to create admin account
```

#### Manual Setup
```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run migrations
python manage.py migrate

# 4. Create admin account
python manage.py createsuperuser

# 5. Load sample data (optional)
python manage.py load_sample_data

# 6. Start server
python manage.py runserver
```

### Access the Website
- **Website**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **Username**: (your superuser username)
- **Password**: (your superuser password)

---

## 📁 Project Structure

```
zentro_project/
├── 📄 manage.py                 # Django CLI
├── 📄 requirements.txt          # Dependencies
├── 📄 README.md                 # This file
├── 📄 INSTALLATION_GUIDE.md     # Detailed setup
├── 📄 API_DOCUMENTATION.md      # API reference
├── 📦 zentro_config/            # Django settings
│   ├── settings.py              # Configuration
│   ├── urls.py                  # URL routing
│   └── wsgi.py                  # WSGI app
├── 📦 home/                     # Main app
│   ├── models.py                # Database models
│   ├── views.py                 # View logic
│   ├── forms.py                 # Form definitions
│   ├── admin.py                 # Admin config
│   ├── tests.py                 # Unit tests
│   └── management/
│       └── commands/
│           └── load_sample_data.py  # Sample data
├── 📦 static/                   # Static files
│   ├── css/style.css            # Main stylesheet
│   ├── js/main.js               # JavaScript
│   └── images/zentro-logo.png   # Logo
├── 📁 templates/                # HTML templates
│   ├── base.html                # Base template
│   ├── home.html                # Homepage
│   ├── about.html               # About page
│   ├── projects.html            # Projects list
│   ├── project_detail.html      # Project detail
│   ├── team.html                # Team page
│   ├── contact.html             # Contact page
│   ├── login.html               # Login
│   ├── signup.html              # Signup
│   ├── profile.html             # Profile
│   └── 404.html, 500.html       # Error pages
└── 📁 media/                    # User uploads

```

---

## 🎨 Design Customization

### Change Primary Color
Edit `static/css/style.css`:
```css
:root {
    --primary-color: #F4C430;      /* Change this */
    --primary-dark: #DAA520;        /* And this */
}
```

### Change Logo
Replace `static/images/zentro-logo.png` with your logo

### Update Navbar Links
Edit `templates/base.html` navbar section

### Modify Footer Content
Edit footer section in `templates/base.html`

### Custom CSS
Add your custom styles to `static/css/style.css` or create new files

---

## 🔐 Admin Panel Guide

### Login to Admin
1. Go to `http://localhost:8000/admin/`
2. Enter your superuser credentials
3. Start managing content

### Add Team Member
1. Click "Team Members"
2. Click "Add Team Member"
3. Fill in details (name, role, bio, email, photo)
4. Save

### Create a Project
1. Click "Projects"
2. Click "Add Project"
3. Fill in all fields (title, description, image, status, technologies)
4. Check "Featured" to show on homepage
5. Save

### Manage Features
1. Click "Features"
2. Add feature title, description, and Font Awesome icon
3. Reorder features
4. Save

### View Contact Submissions
1. Click "Contact Messages"
2. View all submissions
3. Mark as read/replied

---

## 👥 Default User Roles

### 1. **Superuser (Admin)**
- Full access to everything
- Can create users
- Can manage all content
- Access to admin panel

### 2. **Staff User**
- Limited admin access
- Can manage content
- Cannot delete users

### 3. **Regular User**
- View public content
- Submit contact forms
- Create user profile
- View their own profile

### 4. **Anonymous User**
- View public content only
- Cannot access protected pages

---

## 🗄️ Database Models

### User & Profile
- **User** - Django built-in user model
- **UserProfile** - Extended user information

### Content Models
- **TeamMember** - Team information
- **Project** - Projects/portfolio
- **Feature** - Service features
- **Page** - Static pages
- **Testimonial** - Client reviews

### Form Models
- **Contact** - Contact submissions
- **Newsletter** - Subscribers

---

## 🧪 Running Tests

```bash
# Run all tests
python manage.py test

# Run specific test class
python manage.py test home.tests.ModelTestCase

# Run with verbose output
python manage.py test -v 2

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

---

## 🚀 Deployment

### For Production

1. **Update Settings**
```python
# settings.py
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
SECRET_KEY = 'your-secret-key-here'  # Use strong key
```

2. **Use PostgreSQL** (recommended)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'zentro_db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

3. **Collect Static Files**
```bash
python manage.py collectstatic
```

4. **Use Gunicorn**
```bash
pip install gunicorn
gunicorn zentro_config.wsgi:application
```

5. **Configure Nginx/Apache**
```nginx
server {
    listen 80;
    server_name yourdomain.com;
    
    location / {
        proxy_pass http://localhost:8000;
    }
    
    location /static/ {
        alias /path/to/static/;
    }
    
    location /media/ {
        alias /path/to/media/;
    }
}
```

6. **Enable HTTPS**
```bash
pip install certbot-nginx
certbot --nginx -d yourdomain.com
```

---

## 📚 Documentation Files

1. **README.md** - This file
2. **INSTALLATION_GUIDE.md** - Detailed setup guide
3. **API_DOCUMENTATION.md** - API reference
4. **Code Comments** - Inline documentation

---

## 🔐 Security Features

### Implemented
- ✅ CSRF protection (CsrfViewMiddleware)
- ✅ SQL injection prevention (Django ORM)
- ✅ XSS protection (template escaping)
- ✅ Password hashing (PBKDF2)
- ✅ Session security
- ✅ User authentication
- ✅ Role-based authorization
- ✅ Secure headers

### Recommendations for Production
- Enable HTTPS (SSL/TLS)
- Use environment variables for secrets
- Enable rate limiting
- Set up monitoring & logging
- Use web application firewall
- Regular security audits

---

## 🐛 Troubleshooting

### Common Issues

**Issue: Port 8000 already in use**
```bash
python manage.py runserver 8001
```

**Issue: Static files not loading**
```bash
python manage.py collectstatic --clear --noinput
```

**Issue: Database migration error**
```bash
python manage.py migrate --fake-initial
```

**Issue: Permission denied (Mac/Linux)**
```bash
chmod +x manage.py
chmod +x setup.sh
```

**Issue: Virtual environment not activating**
```bash
# Windows
venv\Scripts\activate.bat

# Mac/Linux
source venv/bin/activate
```

---

## 📞 Support & Resources

### Documentation
- [Django Official Docs](https://docs.djangoproject.com/)
- [Django ORM Guide](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [Django Admin](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)

### Tools Used
- [Pillow](https://pillow.readthedocs.io/) - Image handling
- [Font Awesome](https://fontawesome.com/) - Icons
- [Google Fonts](https://fonts.google.com/) - Typography

---

## 📊 File Statistics

- **Lines of Code**: ~5,000+
- **Templates**: 11
- **Models**: 8
- **Views**: 15+
- **CSS Rules**: 300+
- **JavaScript Functions**: 20+

---

## 🎓 Learning Paths

### For Beginners
1. Understand Django structure
2. Explore models.py
3. Learn views.py
4. Customize templates
5. Run tests

### For Intermediate
1. Modify admin.py
2. Create custom forms
3. Add new models
4. Deploy to server
5. Write tests

### For Advanced
1. Add payment integration
2. Implement caching
3. Set up CDN
4. Database optimization
5. Performance monitoring

---

## 💡 Tips & Tricks

### Useful Django Commands
```bash
# Create app migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Check for issues
python manage.py check

# Shell access
python manage.py shell

# Dump data
python manage.py dumpdata > data.json

# Load data
python manage.py loaddata data.json
```

### Speed Up Development
```bash
# Use Django Debug Toolbar
pip install django-debug-toolbar

# Use sqlite3 for fast queries
python manage.py dbshell

# Use runserver with threading
python manage.py runserver --threads 4
```

---

## 🎉 What's Next?

1. ✅ Customize colors and branding
2. ✅ Add your team members
3. ✅ Upload your projects
4. ✅ Add features/services
5. ✅ Enable newsletter
6. ✅ Deploy to production
7. ✅ Set up analytics
8. ✅ Monitor performance

---

## 📄 License

This project is ready for commercial use.

---

## 🙏 Acknowledgments

- Design inspired by [Chauncey.live](https://www.chauncey.live/)
- Built with [Django](https://www.djangoproject.com/)
- Styled with modern CSS3
- Enhanced with vanilla JavaScript

---

## 📮 Contact

For questions or support regarding this project, refer to:
- Django Documentation
- Project README files
- Code comments and docstrings

---

## ✨ Version Info

- **Version**: 1.0
- **Last Updated**: March 25, 2024
- **Status**: Production Ready
- **Django Version**: 4.2
- **Python Version**: 3.8+

---

**Happy coding! 🚀 Your Zentro website is ready to launch!**

---

## 🚀 Next Steps

1. **Customize Content**
   - Add team members via admin
   - Upload your projects
   - Configure features

2. **Branding**
   - Replace logo
   - Customize colors
   - Update company information

3. **Deploy**
   - Follow deployment guide
   - Configure domain
   - Enable SSL/HTTPS

4. **Monitor**
   - Set up analytics
   - Check performance
   - Monitor user activity

---

Need help? Check the **INSTALLATION_GUIDE.md** for detailed instructions!
