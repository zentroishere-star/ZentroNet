"""Dashboard views for admin panel."""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.models import User
from .models import ContactMessage, TeamMember, Project, Testimonial, Newsletter
from .forms import ContactForm


def admin_login(request):
    """Admin login view - dedicated admin login page."""
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('home:dashboard')
    
    error = None
    success = None
    
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        remember_me = request.POST.get('remember_me')
        
        if not username or not password:
            error = 'Please enter both username and password.'
        else:
            # Try authenticate with username first
            user = authenticate(request, username=username, password=password)
            
            # If not found, try with email
            if user is None:
                try:
                    user_obj = User.objects.get(email=username)
                    user = authenticate(request, username=user_obj.username, password=password)
                except User.DoesNotExist:
                    user = None
            
            if user is not None:
                if not user.is_staff:
                    error = 'Access denied. Admin privileges required.'
                else:
                    login(request, user)
                    if remember_me:
                        request.session.set_expiry(1209600)  # 2 weeks
                    return redirect('home:dashboard')
            else:
                error = 'Invalid username/email or password.'
    
    context = {
        'error': error,
        'success': success,
    }
    return render(request, 'admin_login.html', context)


@login_required(login_url='home:login')
def dashboard(request):
    """Main dashboard view."""
    if not request.user.is_staff:
        return redirect('home:home')
    
    # Get statistics
    total_messages = ContactMessage.objects.count()
    unread_messages = ContactMessage.objects.filter(is_read=False).count()
    total_team = TeamMember.objects.count()
    total_projects = Project.objects.count()
    total_subscribers = Newsletter.objects.filter(subscribed=True).count()
    
    # Recent messages
    recent_messages = ContactMessage.objects.all().order_by('-created_at')[:5]
    
    # Recent contacts
    recent_contacts = ContactMessage.objects.filter(is_read=False).order_by('-created_at')[:3]
    
    context = {
        'total_messages': total_messages,
        'unread_messages': unread_messages,
        'total_team': total_team,
        'total_projects': total_projects,
        'total_subscribers': total_subscribers,
        'recent_messages': recent_messages,
        'recent_contacts': recent_contacts,
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required(login_url='home:login')
def messages(request):
    """Messages/Contacts management view."""
    if not request.user.is_staff:
        return redirect('home:home')
    
    # Get all messages
    all_messages = ContactMessage.objects.all().order_by('-created_at')
    
    # Filter by status
    filter_type = request.GET.get('filter', 'all')
    if filter_type == 'unread':
        all_messages = all_messages.filter(is_read=False)
    elif filter_type == 'replied':
        all_messages = all_messages.filter(is_replied=True)
    elif filter_type == 'pending':
        all_messages = all_messages.filter(is_replied=False, is_read=True)
    
    # Search
    search = request.GET.get('search', '')
    if search:
        all_messages = all_messages.filter(
            Q(name__icontains=search) |
            Q(email__icontains=search) |
            Q(subject__icontains=search)
        )
    
    context = {
        'messages': all_messages,
        'filter_type': filter_type,
        'search': search,
        'unread_count': ContactMessage.objects.filter(is_read=False).count(),
    }
    return render(request, 'dashboard/messages.html', context)


@login_required(login_url='home:login')
def message_detail(request, pk):
    """View single message."""
    if not request.user.is_staff:
        return redirect('home:home')
    
    message = get_object_or_404(ContactMessage, pk=pk)
    message.is_read = True
    message.save()
    
    if request.method == 'POST':
        message.is_replied = True
        message.save()
        return redirect('home:dashboard_messages')
    
    context = {'message': message}
    return render(request, 'dashboard/message_detail.html', context)


@login_required(login_url='home:login')
def mark_replied(request, pk):
    """Mark message as replied."""
    if not request.user.is_staff:
        return redirect('home:home')
    
    message = get_object_or_404(ContactMessage, pk=pk)
    message.is_replied = True
    message.save()
    
    return redirect('home:dashboard_messages')


@login_required(login_url='home:login')
def delete_message(request, pk):
    """Delete a message."""
    if not request.user.is_staff:
        return redirect('home:home')
    
    message = get_object_or_404(ContactMessage, pk=pk)
    message.delete()
    
    return redirect('home:dashboard_messages')


@login_required(login_url='home:login')
def team_management(request):
    """Team members management view."""
    if not request.user.is_staff:
        return redirect('home:home')
    
    team_members = TeamMember.objects.all().order_by('order', 'name')
    
    search = request.GET.get('search', '')
    if search:
        team_members = team_members.filter(
            Q(name__icontains=search) |
            Q(role__icontains=search) |
            Q(email__icontains=search)
        )
    
    context = {
        'team_members': team_members,
        'search': search,
    }
    return render(request, 'dashboard/team_management.html', context)


@login_required(login_url='home:login')
def add_team_member(request):
    """Add new team member."""
    if not request.user.is_staff:
        return redirect('home:home')
    
    if request.method == 'POST':
        try:
            team = TeamMember()
            team.name = request.POST.get('name')
            team.role = request.POST.get('role')
            team.bio = request.POST.get('bio')
            team.email = request.POST.get('email')
            team.phone = request.POST.get('phone', '')
            team.linkedin = request.POST.get('linkedin', '')
            team.github = request.POST.get('github', '')
            team.order = int(request.POST.get('order', 0))
            
            if 'photo' in request.FILES:
                team.photo = request.FILES['photo']
            
            team.save()
            return redirect('home:dashboard_team')
        except Exception as e:
            context = {'error': str(e)}
            return render(request, 'dashboard/add_team_member.html', context)
    
    roles = TeamMember.ROLE_CHOICES
    context = {'roles': roles}
    return render(request, 'dashboard/add_team_member.html', context)


@login_required(login_url='home:login')
def edit_team_member(request, pk):
    """Edit team member."""
    if not request.user.is_staff:
        return redirect('home:home')
    
    team = get_object_or_404(TeamMember, pk=pk)
    
    if request.method == 'POST':
        team.name = request.POST.get('name')
        team.role = request.POST.get('role')
        team.bio = request.POST.get('bio')
        team.email = request.POST.get('email')
        team.phone = request.POST.get('phone', '')
        team.linkedin = request.POST.get('linkedin', '')
        team.github = request.POST.get('github', '')
        team.order = int(request.POST.get('order', 0))
        
        if 'photo' in request.FILES:
            team.photo = request.FILES['photo']
        
        team.save()
        return redirect('home:dashboard_team')
    
    roles = TeamMember.ROLE_CHOICES
    context = {'team': team, 'roles': roles}
    return render(request, 'dashboard/edit_team_member.html', context)


@login_required(login_url='home:login')
def delete_team_member(request, pk):
    """Delete team member."""
    if not request.user.is_staff:
        return redirect('home:home')
    
    team = get_object_or_404(TeamMember, pk=pk)
    team.delete()
    return redirect('home:dashboard_team')


@login_required(login_url='home:login')
def projects_management(request):
    """Projects management view."""
    if not request.user.is_staff:
        return redirect('home:home')
    
    projects = Project.objects.all().order_by('-featured', 'order')
    
    # Filter by status
    status_filter = request.GET.get('status', '')
    if status_filter:
        projects = projects.filter(status=status_filter)
    
    search = request.GET.get('search', '')
    if search:
        projects = projects.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search)
        )
    
    context = {
        'projects': projects,
        'status_filter': status_filter,
        'search': search,
    }
    return render(request, 'dashboard/projects_management.html', context)


@login_required(login_url='home:login')
def add_project(request):
    """Add new project."""
    if not request.user.is_staff:
        return redirect('home:home')
    
    if request.method == 'POST':
        try:
            from django.utils.text import slugify
            
            project = Project()
            project.title = request.POST.get('title')
            project.slug = slugify(project.title)
            project.description = request.POST.get('description')
            project.technologies = request.POST.get('technologies')
            project.status = request.POST.get('status', 'Completed')
            project.live_url = request.POST.get('live_url', '')
            project.github_url = request.POST.get('github_url', '')
            project.featured = request.POST.get('featured') in ['on', 'true']
            project.order = int(request.POST.get('order', 0))
            
            if 'image' in request.FILES:
                project.image = request.FILES['image']
            
            project.save()
            return redirect('home:dashboard_projects')
        except Exception as e:
            context = {'error': str(e)}
            return render(request, 'dashboard/add_project.html', context)
    
    statuses = Project.STATUS_CHOICES
    context = {'statuses': statuses}
    return render(request, 'dashboard/add_project.html', context)


@login_required(login_url='home:login')
def edit_project(request, pk):
    """Edit project."""
    if not request.user.is_staff:
        return redirect('home:home')
    
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        project.title = request.POST.get('title')
        project.description = request.POST.get('description')
        project.technologies = request.POST.get('technologies')
        project.status = request.POST.get('status', 'Completed')
        project.live_url = request.POST.get('live_url', '')
        project.github_url = request.POST.get('github_url', '')
        project.featured = request.POST.get('featured') in ['on', 'true']
        project.order = int(request.POST.get('order', 0))
        
        if 'image' in request.FILES:
            project.image = request.FILES['image']
        
        project.save()
        return redirect('home:dashboard_projects')
    
    statuses = Project.STATUS_CHOICES
    context = {'project': project, 'statuses': statuses}
    return render(request, 'dashboard/edit_project.html', context)


@login_required(login_url='home:login')
def delete_project(request, pk):
    """Delete project."""
    if not request.user.is_staff:
        return redirect('home:home')
    
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('home:dashboard_projects')


@login_required(login_url='home:login')
def subscribers(request):
    """Newsletter subscribers view."""
    if not request.user.is_staff:
        return redirect('home:home')
    
    subscribers_list = Newsletter.objects.filter(subscribed=True).order_by('-created_at')
    
    search = request.GET.get('search', '')
    if search:
        subscribers_list = subscribers_list.filter(email__icontains=search)
    
    context = {
        'subscribers': subscribers_list,
        'total': subscribers_list.count(),
        'search': search,
    }
    return render(request, 'dashboard/subscribers.html', context)


@login_required(login_url='home:login')
def dashboard_settings(request):
    """Dashboard settings view."""
    if not request.user.is_staff:
        return redirect('home:home')
    
    user = request.user
    
    if request.method == 'POST':
        user.email = request.POST.get('email', user.email)
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.save()
        
        return redirect('home:dashboard_settings')
    
    context = {'user': user}
    return render(request, 'dashboard/settings.html', context)


@login_required(login_url='home:login')
def dashboard_logout(request):
    """Logout from dashboard."""
    logout(request)
    return redirect('home:home')
