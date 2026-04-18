"""URL configuration for home app."""
from django.urls import path
from . import views
from . import views_dashboard

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    
    # Auth
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('reviews/', views.reviews, name='reviews'),
    
    # API
    path('newsletter/subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
    
    # Dashboard
    path('dashboard/', views_dashboard.dashboard, name='dashboard'),
    path('dashboard/messages/', views_dashboard.messages, name='dashboard_messages'),
    path('dashboard/message/<int:pk>/', views_dashboard.message_detail, name='dashboard_message_detail'),
    path('dashboard/message/<int:pk>/replied/', views_dashboard.mark_replied, name='dashboard_mark_replied'),
    path('dashboard/message/<int:pk>/delete/', views_dashboard.delete_message, name='dashboard_delete_message'),
    path('dashboard/team/', views_dashboard.team_management, name='dashboard_team'),
    path('dashboard/projects/', views_dashboard.projects_management, name='dashboard_projects'),
    path('dashboard/subscribers/', views_dashboard.subscribers, name='dashboard_subscribers'),
    path('dashboard/settings/', views_dashboard.dashboard_settings, name='dashboard_settings'),
    path('dashboard/logout/', views_dashboard.dashboard_logout, name='dashboard_logout'),
]
