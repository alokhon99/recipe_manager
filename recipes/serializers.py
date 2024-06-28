from rest_framework import serializers
from .models import MealGroup, Ingredient, Action, Recipe, MealIngredient, MealAction

class MealGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealGroup
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class MealIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealIngredient
        fields = '__all__'

class MealActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealAction
        fields = '__all__'
