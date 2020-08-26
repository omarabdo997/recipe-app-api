from rest_framework import serializers
from recipe import models


class BaseSerializer(serializers.ModelSerializer):
    model = None

    class Meta:
        abstract = True
    
    def create(self, validated_data):
        data_object = self.model(**validated_data)
        data_object.user = self.context.get('request').user
        data_object.save()
        return data_object

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance    


class TagSerializer(BaseSerializer):
    model = models.Tag

    class Meta:
        model = models.Tag
        fields = '__all__'
        read_only_fields = ('user',)


class IngredientSerializer(BaseSerializer):
    model = models.Ingredient

    class Meta:
        model = models.Ingredient
        fields = '__all__'
        read_only_fields = ('user',)


class RecipeCreateUpdateSerializer(BaseSerializer):
    model = models.Recipe
    

    class Meta:
        model = models.Recipe
        fields = '__all__'
        read_only_fields = ('user', )


    def create(self, validated_data):
        ingredients = validated_data.pop('ingredients')
        tags = validated_data.pop('tags')
        recipe = super().create(validated_data)
        recipe.ingredients.set(ingredients)
        recipe.tags.set(tags)
        return recipe

    def update(self, instance, validated_data):
        ingredients = validated_data.pop('ingredients', None)
        tags = validated_data.pop('tags', None)
        instance = super().update(instance, validated_data)
        if ingredients:
            instance.ingredients.set(ingredients)
        if tags:    
            instance.tags.set(tags)
        return instance





class RecipeSerializer(RecipeCreateUpdateSerializer):
    model = models.Recipe
    ingredients = IngredientSerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = models.Recipe
        fields = '__all__'
        read_only_fields = ('user', )  
