from django.urls import path
from .views import RecipeListView, RecipeDetailView, records, create_view

# import home view
from .views import home

# specify app name
app_name = "recipes"

# establish url patterns
urlpatterns = [
    path("", home),
    path("list/", RecipeListView.as_view(), name="list"),
    path("list/<pk>", RecipeDetailView.as_view(), name="detail"),
    path("search/", records, name="search"),
    path("create/", create_view, name="create"),
]
