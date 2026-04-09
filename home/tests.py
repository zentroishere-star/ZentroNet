"""Tests for home app."""
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import TeamMember, Project, Service, Testimonial, ContactMessage


class URLTests(TestCase):
    """Test URL routing."""
    
    def setUp(self):
        self.client = Client()
    
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
    
    def test_projects_page(self):
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)
    
    def test_team_page(self):
        response = self.client.get(reverse('team'))
        self.assertEqual(response.status_code, 200)
    
    def test_contact_page(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
    
    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
    
    def test_signup_page(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)


class ModelTests(TestCase):
    """Test models."""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_team_member_creation(self):
        member = TeamMember.objects.create(
            name='John Doe',
            role='CEO',
            bio='Chief Executive Officer',
            email='john@example.com',
            photo='test.jpg'
        )
        self.assertEqual(str(member), 'John Doe - Chief Executive Officer')
    
    def test_project_creation(self):
        project = Project.objects.create(
            title='Test Project',
            slug='test-project',
            description='A test project',
            image='test.jpg',
            status='Completed'
        )
        self.assertEqual(str(project), 'Test Project')
    
    def test_service_creation(self):
        service = Service.objects.create(
            title='Test Service',
            description='A test service',
            icon='fas fa-code'
        )
        self.assertEqual(str(service), 'Test Service')
    
    def test_contact_message_creation(self):
        message = ContactMessage.objects.create(
            name='John Doe',
            email='john@example.com',
            subject='Test Subject',
            message='Test message content'
        )
        self.assertEqual(str(message), 'Message from John Doe')


class AuthenticationTests(TestCase):
    """Test authentication."""
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_user_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123',
            'remember_me': False
        })
        # After successful login, should be redirected
        self.assertEqual(response.status_code, 302)
    
    def test_user_signup(self):
        response = self.client.post(reverse('signup'), {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'jane@example.com',
            'password1': 'complexpass123',
            'password2': 'complexpass123'
        })
        # Should redirect after successful signup
        self.assertEqual(response.status_code, 302)


class ProfileTests(TestCase):
    """Test user profile."""
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_profile_requires_login(self):
        response = self.client.get(reverse('profile'))
        # Should redirect to login
        self.assertEqual(response.status_code, 302)
