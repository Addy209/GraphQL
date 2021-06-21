from rest_framework import serializers
from .models import *

class CategorySer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class IngredientSer(serializers.ModelSerializer):
    class Meta:
        model=Ingredient
        fields='__all__'