from django.test import TestCase

from .models import Recipe

from .forms import DifficultySearchForm


class RecipeModelTest(TestCase):
    # setting up non-modified objects used by test methods
    def setUpTestData():
        Recipe.objects.create(
            name="Spaghetti and Meatballs",
            cooking_time=30,
            ingredients=["Spaghetti", "Ground meat", "Tomato Sauce", "Cheese", "Bread"],
            description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        )

    def test_name_length(self):
        # get recipe to test
        recipe = Recipe.objects.get(id=1)
        # get metadata of name field and use to query its max_length
        max_length = recipe._meta.get_field("name").max_length
        # compare value to expected result
        self.assertEqual(max_length, 120)

    def test_name_label(self):
        recipe = Recipe.objects.get(id=1)
        # get metadata of name field and use to query its label
        recipe_name_label = recipe._meta.get_field("name").verbose_name
        # comparae value to expected result
        self.assertEqual(recipe_name_label, "name")

    def test_name(self):
        recipe = Recipe.objects.get(id=1)
        # compare name value to expected result
        self.assertEqual(recipe.name, "Spaghetti and Meatballs")

    def test_cooking_time(self):
        recipe = Recipe.objects.get(id=1)
        # compare cooking time value to expected result
        self.assertEqual(recipe.cooking_time, 30)

    def test_ingredients_help_text(self):
        recipe = Recipe.objects.get(id=1)
        # get metadata of ingredients field and use to query its help text
        ing_help_text = recipe._meta.get_field("ingredients").help_text
        # compare value to expected result
        self.assertEqual(ing_help_text, "Ingredients must be seperated by commas")

    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        # compare url value to expected result
        self.assertEqual(recipe.get_absolute_url(), "/list/1")


class RecipesSearchFormTest(TestCase):
    def test_form_renders_recipe_difficulty_input(self):
        form = DifficultySearchForm()
        self.assertIn("recipe_diff", form.as_p())

    def test_form_renders_chart_type_input(self):
        form = DifficultySearchForm()
        self.assertIn("chart_type", form.as_p())

    def test_form_valid_data(self):
        form = DifficultySearchForm(data={"recipe_diff": "Easy", "chart_type": "#2"})
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = DifficultySearchForm(data={"recipe_diff": "", "chart_type": ""})
        self.assertFalse(form.is_valid())
