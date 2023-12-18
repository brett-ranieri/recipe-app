from django.shortcuts import render, redirect

# used to display lists
from django.views.generic import ListView, DetailView
from .models import Recipe

# used to protect class-based view (require authentication to display in browser)
from django.contrib.auth.mixins import LoginRequiredMixin

# import search form
from .forms import DifficultySearchForm, CreateRecipeForm

# import pandas for efficient data analysis
# convention to import as and refer to as "pd"
import pandas as pd

# import get_chart
from .utils import get_chart


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


def about_view(request):
    return render(request, "recipes/about.html")


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
        print("searched: ", recipe_diff)
        qs = Recipe.objects.all()
        matching_ids = []
        for obj in qs:
            diff = obj.calculate_difficulty()
            print(diff)
            if diff == recipe_diff:
                matching_ids.append(obj.id)
        print(matching_ids)

        qs = qs.filter(id__in=matching_ids)

        # if data found
        if qs:
            # convert the queryset values to pandas dataframe
            recipe_df = pd.DataFrame(qs.values("name", "cooking_time"))
            print(recipe_df)
            chart = get_chart(chart_type, recipe_df, labels=recipe_df["name"].values)
            # add hyperlink to cell containing name value for each row
            recipe_df = pd.DataFrame(
                qs.values("id", "name", "cooking_time"),
                columns=["id", "name", "cooking_time"],
            )
            links = []
            for e, nam in enumerate(recipe_df["name"]):
                nam = (
                    '<a href="/list/'
                    + str(recipe_df["id"][e])
                    + '">'
                    + str(nam)
                    + "</a>"
                )
                links.append(nam)
            recipe_df["name"] = links
            # convert data type to html
            recipe_df = recipe_df.to_html(index=False, escape=False)
    context = {
        "form": form,
        "recipe_df": recipe_df,
        "chart": chart,
        "qs": qs,
    }

    return render(request, "recipes/recipes_search.html", context)


def create_view(request):
    create_form = CreateRecipeForm(request.POST or None, request.FILES)
    name = None
    cooking_time = None
    ingredients = None
    difficulty = None

    if request.method == "POST":
        try:
            ingred = request.POST.get("ingredients")
            cook_t = int(request.POST.get("cooking_time"))
            print(ingred)
            print(cook_t)

            # need to circle back to this...
            # couldnt access calculate_difficulty from the model because recipe
            # didnt exist yet...this is duplicated code though so there must be
            # a better way to accomplish this.
            def calculate_difficulty(ingredients, cooking_time):
                ingreds = ingredients.split(", ")
                if cooking_time < 10 and len(ingreds) < 4:
                    difficulty = "Easy"
                elif cooking_time < 10 and len(ingreds) >= 4:
                    difficulty = "Medium"
                elif cooking_time >= 10 and len(ingreds) < 4:
                    difficulty = "Intermediate"
                elif cooking_time >= 10 and len(ingreds) >= 4:
                    difficulty = "Hard"
                return difficulty

            diff = calculate_difficulty(ingred, cook_t)
            print(diff)
            recipe = Recipe.objects.create(
                name=request.POST.get("name"),
                cooking_time=request.POST.get("cooking_time"),
                ingredients=request.POST.get("ingredients"),
                description=request.POST.get("description"),
                difficulty=diff,
            )
            recipe.save()
            # re-direct clears form on successful submission
            return redirect("recipes:create")

        except:
            print("Oops...something went wrong")

    context = {
        "create_form": create_form,
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients,
        "difficulty": difficulty,
    }

    return render(request, "recipes/recipes_create.html", context)
