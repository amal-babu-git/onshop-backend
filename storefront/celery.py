import os
from celery import Celery

# Using celery lib for executing background tasks
# setting up celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings.dev')
celery = Celery('storefront')
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()

# After setting this code , celery should import in __init__
# Then execute worker start command: celery -A storefront worker --loglevel=info
