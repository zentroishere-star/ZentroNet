"""
WSGI config for zentro_config project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zentro_config.settings')

application = get_wsgi_application()
