from django.shortcuts import render

# used to display lists
from django.views.generic import ListView, DetailView
from .models import Recipe

# used to protect class-based view (require authentication to display in browser)
from django.contrib.auth.mixins import LoginRequiredMixin


# define function that will return view using built in render function
def home(request):
    return render(request, "recipes/recipes_home.html")


# class that inherits ListView props
class RecipeListView(LoginRequiredMixin, ListView):
    # specify model
    model = Recipe
    # specify template
    template_name = "recipes/recipes_list.html"


# class that inherits DetailView props
class RecipeDetailView(LoginRequiredMixin, DetailView):
    # specify model
    model = Recipe
    # specify template
    template_name = "recipes/recipes_detail.html"
