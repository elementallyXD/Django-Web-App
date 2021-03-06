import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
# this is also used in manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')

# Get the base REDIS URL, default to redis' default

app = Celery('webapp')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.broker_url = 'redis://localhost:6379/5'
app.conf.result_backend = 'redis://localhost:6379/6'
