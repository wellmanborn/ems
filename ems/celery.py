import os

from celery import Celery
from celery.schedules import crontab

# from app.tasks import read_from_plc

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ems.settings')

app = Celery('ems')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'every-5-second': {
        'task': 'app.tasks.read_from_plc',
        'schedule': 5.0
    },
    'every-62-seconds': {
        'task': 'app.tasks.read_from_plc_and_insert_to_database',
        'schedule': 62.5
    },
    'every-mid-night': {
        'task': 'app.tasks.remove_old_data_log_from_database',
        'schedule': crontab(minute=0, hour=0)
    }
}

# CELERY_BEAT_SCHEDULE = {
#     "sample_task": {
#         "task": "app.tasks.sample_task",
#         "schedule": 5,
#     },
# }

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#    # Calls read_from_plc() every 1 seconds.
#    sender.add_periodic_task(1.0, read_from_plc.s(), name='add every 1')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {self.request!r}')
