import os

import django
from django.db.utils import IntegrityError

os.environ["DJANGO_SETTINGS_MODULE"] = "app.settings"
django.setup()

from core.models import User

try:
    user = User.objects.create_superuser(
        email="admin@blog.com", first_name="The", last_name="Admin", password="password"
    )
    user.save()
    print("User admin@blog.com created!")
except IntegrityError:
    print("The user admin@blog.com is already registered!")
