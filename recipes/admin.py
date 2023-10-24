from django.contrib import admin

# import the Recipe class into file
from .models import Recipe

# register the class to Django admin - making it visible under Django site admin
admin.site.register(Recipe)
