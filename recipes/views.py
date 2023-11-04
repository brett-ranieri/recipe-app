from django.shortcuts import render

# used to display lists
from django.views.generic import ListView, DetailView
from .models import Recipe

# used to protect class-based view (require authentication to display in browser)
from django.contrib.auth.mixins import LoginRequiredMixin

# import search form
from .forms import DifficultySearchForm


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


def records(request):
    # create instance of DifficultySearchForm
    form = DifficultySearchForm(request.POST or None)
    recipe_diff = None
    recipe_df = None
    chart = None
    qs = None

    if request.method == "POST":
        recipe_diff = request.POST.get("recipe_diff")
        chart_type = request.POST.get("chart_type")

        print(recipe_diff)
        print(chart_type)

        qs = Recipe.objects.all()
        print(qs)

    context = {
        "form": form,
    }

    return render(request, "recipes/recipes_search.html", context)
