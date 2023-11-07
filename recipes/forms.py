from django import forms

# specify choices as a tuple
# when user selects "Bar chart", it is stored as "#1"
CHART__CHOICES = (  # specify choices as a tuple
    ("#1", "Bar chart"),
    ("#2", "Pie chart"),
    ("#3", "Line chart"),
)

DIFFICULTY__CHOICES = (
    ("Easy", "Easy"),
    ("Medium", "Medium"),
    ("Intermediate", "Intermediate"),
    ("Hard", "Hard"),
)


# define class-based Form imported from Django forms
class DifficultySearchForm(forms.Form):
    recipe_diff = forms.ChoiceField(choices=DIFFICULTY__CHOICES)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)


class CreateRecipeForm(forms.Form):
    name = forms.CharField(max_length=50, required=False)
    cooking_time = forms.IntegerField(help_text="in minutes", required=False)
    ingredients = forms.CharField(
        max_length=300, help_text="seperated by commas", required=False
    )
    description = forms.CharField(max_length=300, required=False)
    # pic = forms.ImageField(required=False)
