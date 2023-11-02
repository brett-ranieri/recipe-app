from django.shortcuts import render

# used to display lists
from django.views.generic import ListView
from .models import Recipe


# define function that will return view using built in render function
def home(request):
    return render(request, "recipes/recipes_home.html")


# class that inherits ListView props
class RecipeListView(ListView):
    # specify model
    model = Recipe
    # specify template
    template_name = "recipes/recipes_list.html"
