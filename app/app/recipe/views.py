from rest_framework.views import APIView
from rest_framework import authentication, permissions, generics
from rest_framework.response import Response
from rest_framework.request import Request
from recipe import models, serializers
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404


class BaseListCreateAPIView(generics.ListCreateAPIView):
    model = None
    serializer_class = None
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    
    def get_queryset(self):
        filter_list = {'user': self.request.user}
        assigned_only = bool(self.request.query_params.get('assigned_only', None))
        if assigned_only:
            filter_list['recipe__isnull'] = assigned_only
        return self.model.objects.filter(**filter_list).order_by('-name')

    class Meta:
        abstract = True


class BaseManageAPIView(generics.RetrieveUpdateDestroyAPIView):
    model = None
    serializer_class = None
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return get_object_or_404(self.model, pk=self.kwargs['pk'])


class ListTags(BaseListCreateAPIView):
    model = models.Tag
    serializer_class = serializers.TagSerializer
    

class ManageTag(BaseManageAPIView):
    model = models.Tag
    serializer_class = serializers.TagSerializer


class ListIngredients(BaseListCreateAPIView):
    model = models.Ingredient
    serializer_class = serializers.IngredientSerializer


class ManageIngredient(BaseManageAPIView):
    model = models.Ingredient
    serializer_class = serializers.IngredientSerializer


class ListRecipes(BaseListCreateAPIView):
    model = models.Recipe
    serializer_class = serializers.RecipeSerializer

    def get_queryset(self):
        filter_list = {'user':self.request.user}
        tags = self.request.query_params.get('tags', None)
        if tags:
            filter_list['tags__in'] = tags.split(',')
        return self.model.objects.filter(**filter_list).order_by('-title')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.RecipeSerializer
        return serializers.RecipeCreateUpdateSerializer


class ManageRecipe(BaseManageAPIView):
    model = models.Recipe
    serializer_class = serializers.RecipeSerializer
    def get_object(self):
            return get_object_or_404(self.model, pk=self.kwargs['pk'])

    def get_serializer_class(self):
        if self.request.method == 'PATCH' or self.request.method == 'PUT':
            return serializers.RecipeCreateUpdateSerializer
        return serializers.RecipeSerializer    
    



