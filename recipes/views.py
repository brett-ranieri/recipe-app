from django.shortcuts import render

# used to display lists
from django.views.generic import ListView, DetailView
from .models import Recipe

# used to protect class-based view (require authentication to display in browser)
from django.contrib.auth.mixins import LoginRequiredMixin

# import search form
from .forms import DifficultySearchForm

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
            # add hyoerlink to cell containing name value for each row
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
