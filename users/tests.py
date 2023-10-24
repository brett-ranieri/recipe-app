from django.test import TestCase

from .models import User


class RecipeModelTest(TestCase):
    # setting up non-modified objects used by test methods
    def setUpTestData():
        User.objects.create(
            name="Ferdinand_Magellan",
        )

    def test_name_length(self):
        # get recipe to test
        user = User.objects.get(id=1)
        # get metadata of name field and use to query its max_length
        max_length = user._meta.get_field("name").max_length
        # compare value to expected result
        self.assertEqual(max_length, 50)

    def test_name_label(self):
        user = User.objects.get(id=1)
        # get metadata of name field and use to query its label
        user_name_label = user._meta.get_field("name").verbose_name
        # comparae value to expected result
        self.assertEqual(user_name_label, "name")

    def test_name(self):
        user = User.objects.get(id=1)
        # compare name value to expected result
        self.assertEqual(user.name, "Ferdinand_Magellan")
