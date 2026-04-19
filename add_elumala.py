"""Add Elumalai C to the team."""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zentro_config.settings')
django.setup()

from home.models import TeamMember

# Create team member
team_member, created = TeamMember.objects.update_or_create(
    name='Elumalai C',
    defaults={
        'role': 'Developer',
        'bio': 'AIML Developer with 6 months in tech',
        'email': 'elumalaielumalai5025@gmail.com',
        'phone': '',
        'twitter': '',
        'linkedin': '',
        'github': '',
        'order': 4,
    }
)

if created:
    print("✓ New team member 'Elumalai C' added successfully!")
else:
    print("✓ Team member 'Elumalai C' updated successfully!")
    
print(f"  ID: {team_member.id}")
print(f"  Name: {team_member.name}")
print(f"  Email: {team_member.email}")
print(f"  Role: {team_member.get_role_display()}")
print(f"  Bio: {team_member.bio}")
