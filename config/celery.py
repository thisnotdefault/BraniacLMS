import os

from django.conf import settings

from celery import Celery

if settings.DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

celery_app = Celery("braniac")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()
