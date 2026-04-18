"""Management command to ensure admin user exists."""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Ensure admin superuser exists'

    def handle(self, *args, **options):
        admin_exists = User.objects.filter(username='admin').exists()
        
        if not admin_exists:
            User.objects.create_superuser(
                username='admin',
                email='admin@zentro.com',
                password='admin'
            )
            self.stdout.write(
                self.style.SUCCESS('✓ Admin user created: admin/admin')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Admin user already exists')
            )
