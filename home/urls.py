"""URL configuration for home app."""
from django.urls import path
from . import views

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
]
