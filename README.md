# 🚀 Zentro - Professional Corporate Website

A **complete, production-ready Django website** for the Zentro startup with modern professional design, full authentication, comprehensive admin panel, and attractive UI.

## ✨ Features

### 🎨 Frontend Design
- **Dark Professional Theme** with golden accents (#F4C430)
- **Fully Responsive** - Works perfectly on all devices
- **Modern Animations** - Smooth scroll and hover effects
- **Professional Layout** - Clean, corporate design
- **Interactive Components** - Forms, dropdowns, modals
- **SEO Optimized** - Proper meta tags and structure
- **Fast Performance** - Optimized CSS and JavaScript

### 🔐 Authentication & Security
- ✅ User Registration with validation
- ✅ Secure Login with "Remember Me" feature
- ✅ User Logout functionality
- ✅ Password hashing with PBKDF2
- ✅ CSRF protection on all forms
- ✅ XSS protection (template escaping)
- ✅ SQL injection prevention (Django ORM)
- ✅ Protected admin panel
- ✅ Role-based access control
- ✅ User profile management

### 📊 Database & Content Management
- ✅ SQLite3 for development (easily switch to PostgreSQL for production)
- ✅ 8 Database Models with relationships
- ✅ Django ORM for database operations
- ✅ Fully customizable admin panel
- ✅ Image handling with Pillow

### 🌐 Pages & Features
- ✅ **Homepage** - Hero section, featured projects, team, testimonials
- ✅ **About Page** - Company info, team showcase, values
- ✅ **Projects** - Portfolio with search, project details
- ✅ **Team Page** - Team members with social links
- ✅ **Contact Page** - Contact form with email storage
- ✅ **User Profile** - User profile management
- ✅ **Login/Signup** - Complete authentication system
- ✅ **Search** - Global search functionality
- ✅ **404/500** - Custom error pages

### 📋 Admin Panel
- 👤 Team member management
- 🎨 Project/portfolio management
- 💼 Services/features management
- 💬 Contact form submissions
- ⭐ Testimonial management
- 📧 Newsletter subscriptions
- 📄 Static page content editor
- 👥 User profile management

---

## ⚡ Quick Start

### Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### Installation (2 Methods)

#### Method 1: Automatic Setup (Recommended)

**Windows:**
```bash
setup.bat
```

**Mac/Linux:**
```bash
chmod +x setup.sh
./setup.sh
```

#### Method 2: Manual Setup

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create superuser (admin account)
python manage.py createsuperuser

# 6. (Optional) Load sample data
python manage.py load_sample_data

# 7. Run development server
python manage.py runserver
```

### Access Your Website

| URL | Purpose |
|-----|---------|
| http://127.0.0.1:8000/ | Website |
| http://127.0.0.1:8000/admin/ | Admin Panel |
| http://127.0.0.1:8000/login/ | Login Page |
| http://127.0.0.1:8000/signup/ | Sign Up Page |

---

## 📁 Project Structure

```
zentro_project/
├── manage.py                 # Django CLI
├── requirements.txt          # Python dependencies
├── db.sqlite3               # Database (created after migration)
│
├── zentro_config/           # Project configuration
│   ├── settings.py          # Django settings
│   ├── urls.py              # URL routing
│   └── wsgi.py              # WSGI config
│
├── home/                    # Main app
│   ├── models.py            # Database models (8 models)
│   ├── views.py             # View logic (15+ views)
│   ├── forms.py             # Form definitions (4 forms)
│   ├── admin.py             # Admin configuration
│   ├── urls.py              # App URLs
│   ├── tests.py             # Test cases
│   └── management/commands/
│       └── load_sample_data.py  # Sample data loader
│
├── static/                  # Static files
│   ├── css/style.css        # Professional styling
│   ├── js/main.js           # Interactive features
│   └── images/
│
├── templates/               # HTML templates (11 templates)
│   ├── base.html            # Base template
│   ├── home.html            # Homepage
│   ├── about.html           # About page
│   ├── projects.html        # Projects list
│   ├── project_detail.html  # Project details
│   ├── team.html            # Team page
│   ├── contact.html         # Contact page
│   ├── login.html           # Login page
│   ├── signup.html          # Signup page
│   ├── profile.html         # User profile
│   ├── search.html          # Search results
│   ├── 404.html             # 404 error
│   └── 500.html             # 500 error
│
└── media/                   # User uploaded files
```

---

## 📚 Database Models

### 1. **TeamMember**
- Name, Role, Bio, Email, Phone
- Photo, Social Media Links
- Order for sorting

### 2. **Project**
- Title, Slug, Description, Image
- Technologies, Status, Featured
- Live URL, GitHub URL

### 3. **Service**
- Title, Description, Icon
- Order for sorting

### 4. **Testimonial**
- Author, Company, Content
- Rating (1-5 stars), Image

### 5. **ContactMessage**
- Name, Email, Phone, Subject, Message
- Read/Reply status tracking

### 6. **Newsletter**
- Email, Subscription status
- Track subscribers

### 7. **PageContent**
- Page identifier, Title, Content
- For About, Privacy, Terms pages

### 8. **UserProfile**
- Extended user info
- Avatar, Bio, Phone, Location
- Premium status flag

---

## 🎨 Customization

### Colors
Edit CSS variables in `static/css/style.css`:
```css
:root {
    --primary-color: #F4C430;        /* Golden */
    --primary-dark: #B8860B;         /* Dark gold */
    --bg-dark: #0f0f0f;              /* Background */
    --bg-card: #1a1a1a;              /* Card background */
    --text-primary: #ffffff;         /* Main text */
    --text-secondary: #b0b0b0;       /* Secondary text */
}
```

### Branding
1. Update logo in `templates/base.html` navigation
2. Add your logo in `static/images/`
3. Update site name in admin panel settings

### Content
Use the admin panel to:
- Add team members
- Create projects
- Add services
- Manage testimonials
- Handle contact messages

---

## 🧪 Testing

```bash
# Run all tests
python manage.py test

# Run specific test
python manage.py test home.tests.URLTests

# Verbose output
python manage.py test -v 2
```

---

## 📝 Admin Panel Usage

### Adding Team Members
1. Go to: Admin → Team Members → Add
2. Fill in name, role, bio, email
3. Upload photo
4. Add social media links
5. Save

### Creating Projects
1. Go to: Admin → Projects → Add
2. Fill in title, description, technologies
3. Upload project image
4. Set status and mark as featured if needed
5. Add live URL/GitHub URL
6. Save

### Managing Contact Messages
1. Go to: Admin → Contact Messages
2. View all submissions
3. Mark as read/replied
4. Filter by status

---

## 🚀 Deployment

### For Production (with Gunicorn + Nginx):

```bash
# Install production dependencies
pip install gunicorn psycopg2-binary

# Create .env file with production settings
DEBUG=False
SECRET_KEY=your-production-secret-key
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=postgresql://...

# Collect static files
python manage.py collectstatic --noinput

# Run with Gunicorn
gunicorn zentro_config.wsgi:application --bind 0.0.0.0:8000
```

---

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Use different port
python manage.py runserver 8001
```

### Database Issues
```bash
# Reset database (WARNING: Deletes all data)
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Import Errors
```bash
# Ensure virtual environment is activated
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate
```

---

## 📚 Django Commands Reference

| Command | Purpose |
|---------|---------|
| `python manage.py runserver` | Start dev server |
| `python manage.py migrate` | Apply database migrations |
| `python manage.py makemigrations` | Create migrations |
| `python manage.py createsuperuser` | Create admin account |
| `python manage.py test` | Run tests |
| `python manage.py shell` | Django interactive shell |
| `python manage.py load_sample_data` | Load sample data |
| `python manage.py collectstatic` | Collect  static files |

---

## 📄 License

This project is provided as-is for Zentro startup use.

---

## 🤝 Support

For issues or questions, contact: hello@zentro.com

---

**Created:** 2024  
**Version:** 1.0.0  
**Status:** ✅ Production Ready
