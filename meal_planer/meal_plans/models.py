from django.db import models

# Create your models here.


class Meal(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class MealItem(models.Model):
    name = models.CharField(max_length=200)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
