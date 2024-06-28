from rest_framework import viewsets
from .models import MealGroup, Ingredient, Action, Recipe, MealIngredient, MealAction
from .serializers import MealGroupSerializer, IngredientSerializer, ActionSerializer, RecipeSerializer, MealIngredientSerializer, MealActionSerializer

class MealGroupViewSet(viewsets.ModelViewSet):
    queryset = MealGroup.objects.all()
    serializer_class = MealGroupSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class MealIngredientViewSet(viewsets.ModelViewSet):
    queryset = MealIngredient.objects.all()
    serializer_class = MealIngredientSerializer

class MealActionViewSet(viewsets.ModelViewSet):
    queryset = MealAction.objects.all()
    serializer_class = MealActionSerializer
