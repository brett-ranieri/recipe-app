from django.urls import path

# import home view
from .views import home

# specify app name
app_name = "recipes"

# establish url patterns
urlpatterns = [path("", home)]
