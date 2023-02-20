"""
ASGI config for django_10M_QS project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/

install:
    - pip install uvicorn gunicorn
    - docker-compose.yml: command: postgres -c 'max_connections=250'
    - PSQL: ALTER SYSTEM SET max_connections = 250;
    - !!! DRF DO NOT SUPPORT ASYNC !!!

run:
    gunicorn -w 4 --log-level warning -k uvicorn.workers.UvicornWorker dj_config.asgi:application
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_10M_QS.settings")

application = get_asgi_application()
