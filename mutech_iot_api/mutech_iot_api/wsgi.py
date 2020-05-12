"""
WSGI config for mutech_iot_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os, sys 

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mutech_iot_api.settings')
sys.path.append('/var/www')
sys.path.append('/var/www/html')

application = get_wsgi_application()
