from rest_framework import serializers
from recipe import models


class BaseSerializer(serializers.ModelSerializer):
    model = None

    class Meta:
        abstract = True
    
    user = serializers.CharField(read_only=True)
    
    def create(self, validated_data):
        return self.model.objects.create(
            name = validated_data.get('name'),
            user = self.context.get('request').user
        )

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.save()
        return instance    


class TagSerializer(BaseSerializer):
    model = models.Tag

    class Meta:
        model = models.Tag
        fields = '__all__'


class IngredientSerializer(BaseSerializer):
    model = models.Ingredient

    class Meta:
        model = models.Ingredient
        fields = '__all__'
