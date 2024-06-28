from django.contrib import admin
from .models import MealGroup, Ingredient, Action, Recipe, MealIngredient, MealAction

admin.site.register(MealGroup)
admin.site.register(Ingredient)
admin.site.register(Action)
admin.site.register(Recipe)
admin.site.register(MealIngredient)
admin.site.register(MealAction)
