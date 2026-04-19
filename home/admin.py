"""Admin configuration for home app."""
from django.contrib import admin
from .models import (
    TeamMember, Project, Service, Testimonial,
    ContactMessage, Newsletter, PageContent, UserProfile
)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'email', 'order']
    search_fields = ['name', 'email']
    list_filter = ['role']
    ordering = ['order', 'name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'featured', 'order', 'created_at']
    search_fields = ['title', 'description']
    list_filter = ['status', 'featured', 'created_at']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-featured', 'order']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    ordering = ['order']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['author', 'company', 'rating', 'order']
    search_fields = ['author', 'company']
    ordering = ['order']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'is_replied', 'created_at']
    search_fields = ['name', 'email', 'subject']
    list_filter = ['is_read', 'is_replied', 'created_at']
    readonly_fields = ['created_at']


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed', 'created_at']
    search_fields = ['email']
    list_filter = ['subscribed', 'created_at']
    readonly_fields = ['created_at']


@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ['page', 'title', 'updated_at']
    readonly_fields = ['updated_at']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_premium', 'created_at']
    search_fields = ['user__username', 'user__email']
    list_filter = ['is_premium', 'created_at']
    readonly_fields = ['created_at', 'updated_at']


# Customize admin site
admin.site.site_header = "Zentro Administration"
admin.site.site_title = "Zentro Admin"
admin.site.index_title = "Welcome to Zentro Admin Panel"
