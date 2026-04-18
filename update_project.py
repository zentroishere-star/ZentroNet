import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zentro_config.settings')
django.setup()

from home.models import Project

# Get the first featured project
project = Project.objects.filter(featured=True).order_by('order').first()

if project:
    # Update the image
    project.image = 'projects/Ai-Retinal.png'
    project.save()
    print(f"Successfully updated {project.title} with image Ai-Retinal.png")
else:
    print("No featured project found")
