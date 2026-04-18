"""Dashboard views for admin panel."""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
from django.db.models import Q
from .models import ContactMessage, TeamMember, Project, Testimonial, Newsletter
from .forms import ContactForm


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
