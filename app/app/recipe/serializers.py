from rest_framework import serializers
from recipe import models

class TagSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    name = serializers.CharField(required=False)

    class Meta:
        model = models.Tag
        fields = '__all__'
        

    def create(self, validated_data):        
        return models.Tag.objects.create(
            name = validated_data.get('name',""),
            user = self.context['request'].user
        )
        
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.save()
        return instance    