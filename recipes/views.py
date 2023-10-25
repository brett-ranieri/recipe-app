from django.shortcuts import render


# define function that will return view using built in render function
def home(request):
    return render(request, "recipes/recipes_home.html")
