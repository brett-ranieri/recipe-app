from django.db import models


class User(models.Model):
    # define attributes of the class
    name = models.CharField(max_length=50)

    # define string representation od the class
    def __str__(self):
        return str(self.name)
