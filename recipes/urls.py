from django.urls import path
from .views import RecipeListView

# import home view
from .views import home

# specify app name
app_name = "recipes"

# establish url patterns
urlpatterns = [
    path("", home),
    path("list/", RecipeListView.as_view(), name="list"),
]
