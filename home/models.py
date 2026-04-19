"""Database models for Zentro website."""
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class TeamMember(models.Model):
    """Team member model."""
    ROLE_CHOICES = [
        ('CEO', 'Chief Executive Officer'),
        ('Web Developer', 'Web Developer'),
        ('Developer', 'Developer'),
        ('Project Designer', 'Project Designer'),
        ('Manager', 'Project Manager'),
        ('Logo Designer', 'Logo Designer'),
        ('AIML Developer', 'AIML Developer'),
        ('Python Developer', 'Python Developer'),
        ('Cloud Engineer', 'Cloud Engineer'),
        ('UI/UX Designer', 'UI/UX Designer'),
        ('Code Developer', 'Code Developer'),
        ('Project Coordinator', 'Project Coordinator'),
        ('Other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='team/')
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'

    def __str__(self):
        return f"{self.name} - {self.get_role_display()}"


class Project(models.Model):
    """Project/Portfolio model."""
    STATUS_CHOICES = [
        ('Completed', 'Completed'),
        ('In Progress', 'In Progress'),
        ('Upcoming', 'Upcoming'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    technologies = models.CharField(max_length=500, help_text="Comma-separated list of technologies")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Completed')
    live_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-featured', '-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title


class Service(models.Model):
    """Service/Feature model."""
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class (e.g., 'fas fa-code')")
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    """Client testimonial model."""
    author = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=5
    )
    image = models.ImageField(upload_to='testimonials/', blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return f"Testimonial from {self.author}"


class ContactMessage(models.Model):
    """Contact form submission model."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    is_replied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f"Message from {self.name}"


class Newsletter(models.Model):
    """Newsletter subscription model."""
    email = models.EmailField(unique=True)
    subscribed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Newsletter Subscription'
        verbose_name_plural = 'Newsletter Subscriptions'

    def __str__(self):
        return self.email


class PageContent(models.Model):
    """Static page content model."""
    PAGES = [
        ('about', 'About Us'),
        ('privacy', 'Privacy Policy'),
        ('terms', 'Terms of Service'),
    ]
    
    page = models.CharField(max_length=50, choices=PAGES, unique=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Page Content'
        verbose_name_plural = 'Page Contents'

    def __str__(self):
        return self.get_page_display()


class UserProfile(models.Model):
    """Extended user profile model."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    is_premium = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
