from django.db import models

class MealGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    picture = models.ImageField(upload_to='ingredients_pics/', blank=True, null=True)

    def __str__(self):
        return self.name

class Action(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    meal_group = models.ForeignKey(MealGroup, on_delete=models.CASCADE, related_name='recipes')

    def __str__(self):
        return self.title

class MealIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='meal_ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ingredient.name} in {self.recipe.title}"

class MealAction(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='meal_actions')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.action.name} {self.ingredient.name} in {self.recipe.title}"