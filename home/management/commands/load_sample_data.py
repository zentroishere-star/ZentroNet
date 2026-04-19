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
                'name': 'Gokul A',
                'role': 'Web Developer',
                'bio': 'Full-stack web developer with expertise in Django, React, and cloud deployment. Passionate about building scalable web applications.',
                'email': 'gokul@zentro.com',
                'phone': '+91 9876543210',
                'linkedin': 'https://linkedin.com/in/gokul',
                'github': 'https://github.com/gokul',
                'order': 1
            },
            {
                'name': 'Elumalai C',
                'role': 'AIML Developer',
                'bio': 'AI and Machine Learning specialist focused on building intelligent systems. Strong background in Python, TensorFlow, and data science.',
                'email': 'elumalai@zentro.com',
                'phone': '+91 9876543211',
                'linkedin': 'https://linkedin.com/in/elumalai',
                'github': 'https://github.com/elumalai',
                'order': 2
            },
            {
                'name': 'Gemeni S',
                'role': 'UI/UX Designer',
                'bio': 'Creative UI/UX designer crafting beautiful and intuitive user experiences. Skilled in Figma, Adobe XD, and design thinking.',
                'email': 'gemeni@zentro.com',
                'phone': '+91 9876543212',
                'linkedin': 'https://linkedin.com/in/gemeni',
                'github': 'https://github.com/gemeni',
                'order': 3
            },
            {
                'name': 'Arun Kumar',
                'role': 'Cloud Engineer',
                'bio': 'Cloud infrastructure expert specializing in AWS, Google Cloud, and DevOps. 5+ years experience in production deployments.',
                'email': 'arun@zentro.com',
                'phone': '+91 9876543213',
                'linkedin': 'https://linkedin.com/in/arunkumar',
                'github': 'https://github.com/arunkumar',
                'order': 4
            },
            {
                'name': 'Priya Sharma',
                'role': 'Project Manager',
                'bio': 'Experienced project manager ensuring timely delivery and client satisfaction. Expert in Agile and Scrum methodologies.',
                'email': 'priya@zentro.com',
                'phone': '+91 9876543214',
                'linkedin': 'https://linkedin.com/in/priya-sharma',
                'github': 'https://github.com/priya',
                'order': 5
            },
        ]
        
        for team_member_data in team_data:
            TeamMember.objects.get_or_create(
                email=team_member_data['email'],
                defaults=team_member_data
            )
        
        self.stdout.write(self.style.SUCCESS('✓ Team members loaded'))
        
        # Create projects
        projects_data = [
            {
                'title': 'E-Commerce Platform',
                'slug': 'ecommerce-platform',
                'description': 'Full-featured e-commerce solution with payment integration, inventory management, and real-time order tracking.',
                'technologies': 'Django, React, PostgreSQL, Stripe',
                'status': 'Completed',
                'featured': True,
                'order': 1
            },
            {
                'title': 'AI Chat Bot Assistant',
                'slug': 'ai-chatbot',
                'description': 'Intelligent chatbot powered by machine learning that handles customer support and queries 24/7 with natural language processing.',
                'technologies': 'Python, TensorFlow, NLP, REST API',
                'status': 'Completed',
                'featured': True,
                'order': 2
            },
            {
                'title': 'Cloud Analytics Dashboard',
                'slug': 'analytics-dashboard',
                'description': 'Real-time analytics dashboard for monitoring application metrics, user behavior, and system performance across cloud infrastructure.',
                'technologies': 'React, D3.js, Node.js, AWS',
                'status': 'Completed',
                'featured': True,
                'order': 3
            },
            {
                'title': 'Mobile Fitness App',
                'slug': 'mobile-fitness-app',
                'description': 'Cross-platform fitness tracking application with workout plans, nutrition tracking, and social features.',
                'technologies': 'React Native, Firebase, Node.js',
                'status': 'Completed',
                'featured': False,
                'order': 4
            },
            {
                'title': 'Project Management Tool',
                'slug': 'project-management-tool',
                'description': 'Team collaboration platform with task management, file sharing, real-time notifications, and progress tracking.',
                'technologies': 'Django, Vue.js, WebSocket, PostgreSQL',
                'status': 'Completed',
                'featured': False,
                'order': 5
            },
            {
                'title': 'IoT Device Monitor',
                'slug': 'iot-monitor',
                'description': 'Web-based monitoring system for IoT devices with real-time data visualization and automated alerts.',
                'technologies': 'Python, MQTT, React, InfluxDB',
                'status': 'In Progress',
                'featured': False,
                'order': 6
            },
        ]
        
        for project_data in projects_data:
            Project.objects.get_or_create(
                slug=project_data['slug'],
                defaults=project_data
            )
        
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
