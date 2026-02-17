"""
WSGI config for task_manager_api project.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager_api.settings')
application = get_wsgi_application()
