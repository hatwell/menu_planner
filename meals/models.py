from django.db import models
from django.utils import timezone

# Create your models here.


class MealType(models.TextChoices):
    BREAKFAST = "BREAKFAST"
    LUNCH = "LUNCH"
    DINNER = "DINNER"
    SNACK = "SNACK"
    SIDE = "SIDE"
    MISC = "MISC"


class Meal(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    comments = models.TextField()
    meal_type = models.CharField(
        max_length=10,
        choices=MealType.choices,
        default=MealType.MISC
    )

    added_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
