import graphene
from graphene_django import DjangoObjectType, DjangoListField
from graphene_django.rest_framework.mutation import SerializerMutation
import http

from .models import Category, Ingredient
from .serializer import *

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")

class Query(graphene.ObjectType):
    allingredients = DjangoListField(IngredientType)
    categorybyname = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_allingredients(root, info):
        # We can easily optimize query count in the resolve method
        print(info.context)
        return Ingredient.objects.all()

    def resolve_categorybyname(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None


class CategoryPostPut(SerializerMutation):
    class Meta:
        serializer_class = CategorySer
        model_operations = ['create', 'update']
        lookup_field = 'id'

    @classmethod
    def get_serializer_kwargs(cls, root, info, **input):
        if 'id' in input:
            instance=Category.objects.get(id=input['id'])
            if instance:
                return {'instance':instance, 'data':input, 'partial':True}
            else:
                raise http.Http404
        return {'data':input, 'partial':True}

class IngredientPostPut(SerializerMutation):
    class Meta:
        serializer_class=IngredientSer
        lookup_field='id'

    @classmethod
    def get_serializer_kwargs(cls, root, info, **input):
        if 'id' in input:
            instance=Ingredient.objects.get(id=input['id'])
            if instance:
                return {'instance':instance, 'data':input, 'partial':True}
            else:
                raise http.Http404
        return {'data':input, 'partial':True}

class Mutation(graphene.ObjectType):
    category_mutate=CategoryPostPut.Field()
    ingredient_mutate=IngredientPostPut.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)