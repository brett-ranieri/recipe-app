from django import forms

# specify choices as a tuple
# when user selects "Bar chart", it is stored as "#1"
CHART__CHOICES = (  # specify choices as a tuple
    ("#1", "Bar chart"),
    ("#2", "Pie chart"),
    ("#3", "Line chart"),
)

DIFFICULTY__CHOICES = (
    ("#1", "Easy"),
    ("#2", "Medium"),
    ("#3", "Intermediate"),
    ("#1", "Hard"),
)


# define class-based Form imported from Django forms
class DifficultySearchForm(forms.Form):
    recipe_diff = forms.ChoiceField(choices=DIFFICULTY__CHOICES)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)
