from rest_framework.views import APIView
from rest_framework import authentication, permissions, generics
from rest_framework.response import Response
from rest_framework.request import Request
from recipe import models, serializers
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404


# Create your views here.

class ListTags(generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.TagSerializer
    
    def get_queryset(self):
        return models.Tag.objects.filter(user=self.request.user).order_by('-name')

class CreateTag(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.TagSerializer

    def get_object(self):
        return get_object_or_404(models.Tag, pk=self.kwargs['pk'])       

