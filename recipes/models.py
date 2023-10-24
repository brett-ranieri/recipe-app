from django.db import models


class Recipe(models.Model):
    # define attributes of the class
    name = models.CharField(max_length=120)
    cooking_time = models.IntegerField(help_text="in minutes")
    ingredients = models.CharField(
        max_length=400, help_text="Ingredients must be seperated by commas"
    )
    difficulty = models.CharField(max_length=20)
    description = models.TextField()

    # define string representation od the class
    def __str__(self):
        return str(self.name)
