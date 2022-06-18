"""
WSGI config for boilerplate project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os, sys
# sys.path.append('TODO/MyProject')
# sys.path.append('TODO/MyProject/project_name')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "boilerplate.settings")

application = get_wsgi_application()
