# Zentro - Professional Business Website

A complete, production-ready Django website for Zentro startup with authentication, admin panel, and modern design.

## 🎯 Project Overview

Zentro is a professional business website built with:
- **Backend**: Django 4.2 with SQLite3
- **Frontend**: HTML5, CSS3, JavaScript
- **Design**: Based on Chauncey.live with custom modifications
- **Authentication**: Django built-in authentication system
- **Authorization**: Role-based access control
- **Database**: SQLite3 with Django ORM
- **Admin Panel**: Beautiful, customizable admin interface

## 📁 Project Structure

```
zentro_project/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables example
├── db.sqlite3               # SQLite database (created after migration)
├── zentro_config/           # Project configuration
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # URL routing
│   └── wsgi.py              # WSGI configuration
├── home/                    # Main app
│   ├── migrations/          # Database migrations
│   ├── models.py            # Database models
│   ├── views.py             # View logic
│   ├── forms.py             # Form definitions
│   ├── urls.py              # App URLs
│   ├── admin.py             # Admin configuration
│   └── apps.py              # App configuration
├── static/                  # Static files
│   ├── css/
│   │   └── style.css        # Main stylesheet
│   ├── js/
│   │   └── main.js          # JavaScript functionality
│   └── images/
│       └── zentro-logo.png  # Logo
├── media/                   # User uploaded files
├── templates/               # HTML templates
│   ├── base.html            # Base template
│   ├── home.html            # Home page
│   ├── about.html           # About page
│   ├── projects.html        # Projects list
│   ├── project_detail.html  # Project details
│   ├── team.html            # Team page
│   ├── contact.html         # Contact page
│   ├── login.html           # Login page
│   ├── signup.html          # Signup page
│   ├── profile.html         # User profile
│   ├── 404.html             # 404 error page
│   └── 500.html             # 500 error page
└── README.md                # This file
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Clone/Extract Project
```bash
cd zentro_project
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Create .env File
```bash
# Copy the example
cp .env.example .env

# Edit .env if needed (for production)
```

### Step 5: Run Migrations
```bash
python manage.py migrate
```

### Step 6: Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account:
- Username: admin
- Email: admin@zentro.com
- Password: (secure password)

### Step 7: Collect Static Files (Optional for development)
```bash
python manage.py collectstatic --noinput
```

### Step 8: Run Development Server
```bash
python manage.py runserver
```

The website will be available at: `http://127.0.0.1:8000/`
Admin panel: `http://127.0.0.1:8000/admin/`

## 🎨 Admin Panel Features

The admin panel includes:

### 1. Team Management
- Add/edit team members
- Upload team photos
- Manage roles (CEO, CTO, Developer, Designer, etc.)
- Social media links
- Bio and contact information

### 2. Projects Management
- Create and manage projects
- Upload project images
- Track project status (Completed, In Progress, Upcoming)
- Add technologies used
- Links to live projects and GitHub repos
- Featured projects selection

### 3. Features Management
- Add service features
- Icon selection
- Order features for display

### 4. Contact Messages
- View all contact form submissions
- Mark as read/replied
- Filter by status

### 5. Testimonials
- Add client testimonials
- Star ratings
- Upload author images
- Display order management

### 6. Newsletter Subscriptions
- View all subscribers
- Export subscriber list
- Manage subscription status

### 7. User Profiles
- View user information
- Avatar management
- Premium membership status
- Profile completion tracking

### 8. Static Pages
- Manage About Us page
- Update Privacy Policy
- Update Terms of Service
- Edit contact page content

## 🔐 Authentication & Authorization

### Features Implemented:
1. **User Registration**
   - Custom signup form with validation
   - Email verification ready
   - Password strength requirements
   - Auto-login after signup

2. **User Login**
   - Secure authentication
   - "Remember me" functionality
   - Session management
   - Redirect to requested page after login

3. **Role-Based Access Control**
   - Superuser (Admin)
   - Staff users
   - Regular users
   - Anonymous users

4. **Protected Routes**
   - Profile page (login required)
   - Admin panel (superuser required)
   - Admin actions protected

5. **Security Features**
   - CSRF protection
   - Password hashing
   - SQL injection prevention (ORM)
   - XSS protection

## 📱 Pages & Routes

| Page | URL | Authentication |
|------|-----|-----------------|
| Home | / | Public |
| About | /about/ | Public |
| Projects | /projects/ | Public |
| Project Detail | /projects/<slug>/ | Public |
| Team | /team/ | Public |
| Contact | /contact/ | Public |
| Login | /login/ | Public |
| Signup | /signup/ | Public |
| Profile | /profile/ | Login Required |
| Admin | /admin/ | Superuser Only |

## 🗄️ Database Models

### User-Related Models
- **User** (Django built-in)
- **UserProfile** - Extended user information

### Content Models
- **TeamMember** - Team information
- **Project** - Project portfolio
- **Feature** - Service features
- **Page** - Static pages content
- **Testimonial** - Client testimonials

### Form & Contact Models
- **Contact** - Contact form submissions
- **Newsletter** - Newsletter subscriptions

### Model Features
- Automatic timestamps (created_at, updated_at)
- Slug generation for URLs
- Image handling with Pillow
- Soft delete support (is_active flags)
- Custom ordering
- Admin customization

## 🎬 Using the Admin Panel

### Login to Admin
1. Go to `http://127.0.0.1:8000/admin/`
2. Enter your superuser credentials
3. Start managing content

### Adding a Team Member
1. Click "Team Members" in the left sidebar
2. Click "Add Team Member"
3. Fill in the form:
   - Name
   - Role
   - Bio
   - Email
   - Upload image
   - Add social link
   - Set order
4. Click "Save"

### Creating a Project
1. Click "Projects" in the left sidebar
2. Click "Add Project"
3. Fill in:
   - Title (auto-generates slug)
   - Description
   - Short description
   - Upload image
   - Select status
   - Add technologies (comma-separated)
   - Add links (live & GitHub)
   - Set order
   - Mark as featured if desired
4. Click "Save"

### Managing Features
1. Click "Features"
2. Add features with icons and descriptions
3. Features appear on the homepage

### Viewing Contact Messages
1. Click "Contact Messages"
2. View all submissions
3. Mark as read/replied
4. Filter by status

## 🎨 Customization Guide

### Change Colors
Edit `static/css/style.css` root variables:
```css
:root {
    --primary-color: #F4C430;      /* Change this */
    --primary-dark: #DAA520;        /* And this */
    /* ... other colors ... */
}
```

### Update Logo
Replace the logo at: `static/images/zentro-logo.png`

### Change Company Name
Search and replace "Zentro" in templates and settings

### Modify Navigation
Edit `templates/base.html` navbar links

### Update Footer
Edit footer section in `templates/base.html`

### Change Domain Name
1. Update ALLOWED_HOSTS in `zentro_config/settings.py`
2. Update site information in Django admin

## 🚀 Deployment Guide

### For Production:

1. **Set DEBUG = False**
   ```python
   # settings.py
   DEBUG = False
   ```

2. **Update ALLOWED_HOSTS**
   ```python
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   ```

3. **Use Strong SECRET_KEY**
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

4. **Use Production Database**
   - PostgreSQL recommended
   - Update database settings in settings.py

5. **Configure Static Files**
   ```bash
   python manage.py collectstatic
   ```

6. **Use Gunicorn**
   ```bash
   pip install gunicorn
   gunicorn zentro_config.wsgi:application --bind 0.0.0.0:8000
   ```

7. **Use Nginx/Apache**
   - Configure reverse proxy
   - Serve static files

8. **Enable HTTPS**
   - Install SSL certificate
   - Update SECURE_SSL_REDIRECT = True

## 📊 Features Overview

### Frontend Features
- ✅ Responsive design
- ✅ Dark theme with golden accents
- ✅ Smooth animations
- ✅ Mobile-friendly
- ✅ Fast loading
- ✅ SEO optimized

### Backend Features
- ✅ Django ORM
- ✅ SQLite3 database
- ✅ User authentication
- ✅ Role-based access
- ✅ Contact forms
- ✅ Newsletter subscription
- ✅ Image uploads
- ✅ Comprehensive admin panel

### Content Management
- ✅ Projects management
- ✅ Team member profiles
- ✅ Feature descriptions
- ✅ Testimonial management
- ✅ Contact form submissions
- ✅ Newsletter subscribers
- ✅ Static page content

## 🔒 Security Considerations

### Implemented:
- CSRF protection
- SQL injection prevention (ORM)
- XSS protection
- Password hashing
- Secure session handling
- User authentication
- Role-based authorization

### To Add (Production):
- Email verification
- Two-factor authentication
- Rate limiting
- HTTPS enforced
- Security headers
- Monitoring & logging

## 📝 API Endpoints

### User Endpoints
- POST `/signup/` - Register new user
- POST `/login/` - Login
- GET `/logout/` - Logout
- GET `/profile/` - View profile (login required)

### Content Endpoints
- GET `/` - Home page
- GET `/about/` - About page
- GET `/projects/` - Projects list
- GET `/projects/<slug>/` - Project detail
- GET `/team/` - Team page
- GET `/contact/` - Contact page

### Form Endpoints
- POST `/contact/` - Submit contact form
- POST `/api/subscribe/` - Newsletter subscription

## 🛠️ Troubleshooting

### Database Issues
```bash
# Reset database (WARNING: Deletes all data)
python manage.py migrate home zero
python manage.py migrate
python manage.py createsuperuser
```

### Static Files Not Loading
```bash
python manage.py collectstatic --clear --noinput
```

### Port Already in Use
```bash
python manage.py runserver 8001
```

### Permission Denied on Linux/Mac
```bash
chmod +x manage.py
```

## 📚 Additional Resources

- Django Documentation: https://docs.djangoproject.com/
- Django ORM: https://docs.djangoproject.com/en/stable/topics/db/models/
- Django Admin: https://docs.djangoproject.com/en/stable/ref/contrib/admin/
- Pillow (Image handling): https://pillow.readthedocs.io/

## 📞 Support

For issues or questions, refer to:
- Django documentation
- Project README files
- Code comments

## 📄 License

This project is ready for commercial use.

## 🎉 Ready to Launch!

Your Zentro website is ready to go live. Follow the deployment guide and customize as needed.

Happy coding! 🚀
