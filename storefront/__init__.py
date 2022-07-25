# should import celery in init otherwise python doesn't know about celery.py
from .celery import celery
