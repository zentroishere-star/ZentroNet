"""Views for Zentro website."""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.db.models import Q, Case, When, Value, IntegerField
from django.http import JsonResponse
from django.urls import reverse
from functools import wraps
from .models import (
    TeamMember, Project, Service, Testimonial, 
    ContactMessage, Newsletter, PageContent, UserProfile
)
from .forms import (
    ContactForm, NewsletterForm, SignUpForm, 
    LoginForm, UserProfileForm
)

# Custom decorator for views that require login but show limited content to non-authenticated users
def login_required_or_limited(view_func):
    """
    Decorator that allows users to view limited content without login,
    but requires login for full access. Redirects to login page if user tries to access restricted data.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        response = view_func(request, *args, **kwargs)
        return response
    return wrapper

def reviews(request):
    """Reviews page view."""
    reviews_list = Testimonial.objects.all()
    
    # Add authentication status to context
    is_authenticated = request.user.is_authenticated
    
    context = {
        'reviews': reviews_list,
        'is_authenticated': is_authenticated,
    }
    return render(request, 'reviews.html', context)

def home(request):
    """Home page view."""
    featured_projects = Project.objects.filter(featured=True)[:3]
    services = Service.objects.all()
    # Show only specific team members on home page in custom order
    team = TeamMember.objects.filter(
        name__in=['Gokul A', 'Elumalai C','Gemeni S']
    ).annotate(
        display_order=Case(
            When(name='Gokul A', then=Value(1)),
            When(name='Elumalai C', then=Value(2)),
            When(name='Gemeni S', then=Value(3)),
            default=Value(99),
            output_field=IntegerField(),
        )
    ).order_by('display_order')
    testimonials = Testimonial.objects.all()[:3]
    
    context = {
        'featured_projects': featured_projects,
        'services': services,
        'team': team,
        'testimonials': testimonials,
    }
    return render(request, 'home.html', context)


def about(request):
    """About us page - Limited team info without login."""
    team = TeamMember.objects.filter(
        name__in=['Gokul A', 'Elumalai C', 'Gemeni S']
    ).annotate(
        display_order=Case(
            When(name='Gokul A', then=Value(1)),
            When(name='Elumalai C', then=Value(2)),
            When(name='Gemeni S', then=Value(3)),
            default=Value(99),
            output_field=IntegerField(),
        )
    ).order_by('display_order')
    try:
        about_content = PageContent.objects.get(page='about')
    except PageContent.DoesNotExist:
        about_content = None
    
    # Add authentication status to context
    is_authenticated = request.user.is_authenticated
    
    context = {
        'team': team,
        'about_content': about_content,
        'is_authenticated': is_authenticated,
    }
    return render(request, 'about.html', context)


def projects(request):
    """Projects list view - Limited info without login."""
    projects_list = Project.objects.all()
    
    # Filter by search
    search = request.GET.get('search', '')
    if search:
        projects_list = projects_list.filter(
            Q(title__icontains=search) | 
            Q(description__icontains=search)
        )
    
    # Split technologies for each project
    for project in projects_list:
        project.tech_list = [tech.strip() for tech in project.technologies.split(',')]
    
    # Add authentication status to context
    is_authenticated = request.user.is_authenticated
    
    context = {
        'projects': projects_list,
        'search': search,
        'is_authenticated': is_authenticated,
    }
    return render(request, 'projects.html', context)


def project_detail(request, slug):
    """Project detail view - Login required."""
    if not request.user.is_authenticated:
        return redirect(f"{reverse('home:login')}?next={request.path}")
    
    project = get_object_or_404(Project, slug=slug)
    project.tech_list = [tech.strip() for tech in project.technologies.split(',')]
    related_projects = Project.objects.exclude(id=project.id)[:3]
    
    # Split technologies for related projects
    for proj in related_projects:
        proj.tech_list = [tech.strip() for tech in proj.technologies.split(',')]
    
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'project_detail.html', context)


def team(request):
    """Team page view - Login required."""
    if not request.user.is_authenticated:
        return redirect(f"{reverse('home:login')}?next={request.path}")
    
    # Display all team members ordered by order field, then by name
    team_members = TeamMember.objects.all().order_by('order', 'name')
    
    context = {
        'team': team_members,
    }
    return render(request, 'team.html', context)


@require_http_methods(["GET", "POST"])
def contact(request):
    """Contact page view."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'status': 'success',
                'message': 'Thank you! Your message has been sent successfully.'
            })
        else:
            return JsonResponse({
                'status': 'error',
                'message': 'Please check your form and try again.'
            })
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)


@require_http_methods(["POST"])
def newsletter_subscribe(request):
    """Newsletter subscription."""
    form = NewsletterForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({
            'status': 'success',
            'message': 'You have been subscribed to our newsletter!'
        })
    else:
        return JsonResponse({
            'status': 'error',
            'message': 'This email is already subscribed or invalid.'
        }, status=400)


def search(request):
    """Search view."""
    query = request.GET.get('q', '')
    projects_results = Project.objects.filter(
        Q(title__icontains=query) | 
        Q(description__icontains=query)
    )
    team_results = TeamMember.objects.filter(
        Q(name__icontains=query) | 
        Q(bio__icontains=query)
    )
    
    context = {
        'query': query,
        'projects': projects_results,
        'team': team_results,
    }
    return render(request, 'search.html', context)


def signup(request):
    """User signup view."""
    if request.user.is_authenticated:
        return redirect('home:home')
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                # Create user profile
                UserProfile.objects.create(user=user)
                # Auto-login
                login(request, user)
                return redirect('home:profile')
            except Exception as e:
                # Handle any database errors
                form.add_error(None, f'Registration failed: {str(e)}. Please try with different credentials.')
    else:
        form = SignUpForm()
    
    context = {'form': form}
    return render(request, 'signup.html', context)


def user_login(request):
    """User login view."""
    if request.user.is_authenticated:
        return redirect('home:home')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            if user is None:
                # Try with email
                try:
                    user_obj = User.objects.get(email=username)
                    user = authenticate(request, username=user_obj.username, password=password)
                except User.DoesNotExist:
                    user = None
            
            if user is not None:
                login(request, user)
                if form.cleaned_data.get('remember_me'):
                    request.session.set_expiry(1209600)  # 2 weeks
                next_page = request.GET.get('next')
                if next_page:
                    return redirect(next_page)
                return redirect('home:profile')
    else:
        form = LoginForm()
    
    context = {'form': form}
    return render(request, 'login.html', context)


def user_logout(request):
    """User logout view."""
    logout(request)
    return redirect('home:home')


@login_required
def profile(request):
    """User profile view."""
    try:
        user_profile = request.user.profile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            # Update user fields
            request.user.first_name = form.cleaned_data.get('first_name', '')
            request.user.last_name = form.cleaned_data.get('last_name', '')
            request.user.email = form.cleaned_data['email']
            request.user.save()
            # Save profile
            form.save()
            return redirect('home:profile')
    else:
        form = UserProfileForm(instance=user_profile, initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        })
    
    context = {
        'form': form,
        'user_profile': user_profile,
    }
    return render(request, 'profile.html', context)


def handler404(request, exception=None):
    """404 error handler."""
    return render(request, '404.html', status=404)


def handler500(request):
    """500 error handler."""
    return render(request, '500.html', status=500)
