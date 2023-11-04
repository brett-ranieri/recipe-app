from django.db import models

# import reverse function
from django.shortcuts import reverse


class Recipe(models.Model):
    # define attributes of the class
    name = models.CharField(max_length=120)
    cooking_time = models.IntegerField(help_text="in minutes")
    ingredients = models.CharField(
        max_length=400, help_text="Ingredients must be seperated by commas"
    )
    difficulty = models.CharField(max_length=20)
    description = models.TextField(max_length=600, help_text="600 character limit")
    pic = models.ImageField(upload_to="recipes", default="empty_bowl.jpg")

    # define string representation od the class
    def __str__(self):
        return str(self.name)

    # function will return the primary key of the recipe
    def get_absolute_url(self):
        # reverse returns an absolute path reference matching a given view and optional parameters
        return reverse("recipes:detail", kwargs={"pk": self.pk})

    # function to calculate difficulty
    def calculate_difficulty(self):
        ingredients = self.ingredients.split(", ")
        if self.cooking_time < 10 and len(ingredients) < 4:
            difficulty = "Easy"
        elif self.cooking_time < 10 and len(ingredients) >= 4:
            difficulty = "Medium"
        elif self.cooking_time >= 10 and len(ingredients) < 4:
            difficulty = "Intermediate"
        elif self.cooking_time >= 10 and len(ingredients) >= 4:
            difficulty = "Hard"

        print("model: ", difficulty)
        return difficulty
