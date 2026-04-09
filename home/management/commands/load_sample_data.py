"""Management command to load sample data."""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from home.models import TeamMember, Project, Service, Testimonial, Newsletter


class Command(BaseCommand):
    help = 'Load sample data into the database'

    def handle(self, *args, **options):
        # Create services
        services_data = [
            {
                'title': 'Web Development',
                'description': 'Custom web applications built with modern technologies',
                'icon': 'fas fa-code'
            },
            {
                'title': 'Mobile Apps',
                'description': 'Native and cross-platform mobile applications',
                'icon': 'fas fa-mobile-alt'
            },
            {
                'title': 'Cloud Solutions',
                'description': 'Scalable cloud infrastructure and deployment',
                'icon': 'fas fa-cloud'
            },
            {
                'title': 'API Development',
                'description': 'RESTful and GraphQL APIs for seamless integration',
                'icon': 'fas fa-plug'
            },
            {
                'title': 'Data Science',
                'description': 'Machine learning and data analytics solutions',
                'icon': 'fas fa-brain'
            },
            {
                'title': 'DevOps',
                'description': 'CI/CD pipelines and infrastructure automation',
                'icon': 'fas fa-cogs'
            },
        ]
        
        for service_data in services_data:
            Service.objects.get_or_create(**service_data)
        
        self.stdout.write(self.style.SUCCESS('✓ Services loaded'))
        
        # Create team members
        team_data = [
            {
                'name': 'Elumalai C',
                'role': 'AIML Developer',
                'bio': 'AIML Developer with 6 months in tech',
                'email': 'elumalaielumalai5025@gmail.com',
                'photo': 'team/Zentro 3/zentro_project/static/images/Elumalai.C images.png'
            },
            {
                'name': 'Bob Smith',
                'role': 'CTO',
                'bio': 'Tech architect specializing in scalable systems',
                'email': 'bob@zentro.com',
                'photo': 'team/bob.jpg'
            },
    

    
        ]
        
        for team_member_data in team_data:
            TeamMember.objects.get_or_create(**team_member_data)
        
        self.stdout.write(self.style.SUCCESS('✓ Team members loaded'))
        
        # Create projects
        projects_data = [
            {
                'title': 'E-Commerce Platform',
                'slug': 'ecommerce-platform',
                'description': 'Full-featured e-commerce solution with payment integration',
                'image': 'projects/ecommerce.jpg',
                'technologies': 'Django, React, PostgreSQL, Stripe',
                'status': 'Completed',
                'featured': True
            },
            {
                'title': 'Mobile Fitness App',
                'slug': 'mobile-fitness-app',
                'description': 'Cross-platform fitness tracking application',
                'image': 'projects/fitness.jpg',
                'technologies': 'React Native, Firebase, Node.js',
                'status': 'Completed',
                'featured': True
            },
    
        ]
        
        for project_data in projects_data:
            Project.objects.get_or_create(**project_data)
        
        self.stdout.write(self.style.SUCCESS('✓ Projects loaded'))
        
        # Create testimonials
        testimonials_data = [
            {
                'author': 'Sarah Mitchell',
                'company': 'Tech Innovations Inc',
                'content': 'Zentro transformed our business with their innovative solutions. Highly recommended!',
                'rating': 5
            },
            {
                'author': 'John Parker',
                'company': 'Digital Solutions Ltd',
                'content': 'Professional, reliable, and results-driven. Great team to work with!',
                'rating': 5
            },
            {
                'author': 'Maria Garcia',
                'company': 'Global Enterprises',
                'content': 'The best investment we made for our digital transformation.',
                'rating': 5
            },
        ]
        
        for testimonial_data in testimonials_data:
            Testimonial.objects.get_or_create(**testimonial_data)
        
        self.stdout.write(self.style.SUCCESS('✓ Testimonials loaded'))
        
        self.stdout.write(self.style.SUCCESS('All sample data loaded successfully!'))
