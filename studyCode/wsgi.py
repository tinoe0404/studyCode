"""
WSGI config for studyCode project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studyCode.settings')

application = get_wsgi_application()

app = application # This line is for compatibility with some WSGI servers that expect the application to be named 'app'
