from django.contrib import admin

# import the User class into file
from .models import User

# register the class to Django admin - making it visible under Django site admin
admin.site.register(User)
