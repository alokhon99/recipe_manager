from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MealGroupViewSet, IngredientViewSet, ActionViewSet, RecipeViewSet, MealIngredientViewSet, MealActionViewSet

router = DefaultRouter()
router.register(r'meal_groups', MealGroupViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'actions', ActionViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'meal_ingredients', MealIngredientViewSet)
router.register(r'meal_actions', MealActionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
