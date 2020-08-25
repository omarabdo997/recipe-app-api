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
        return self.model.objects.filter(user=self.request.user).order_by('-name')

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

    



