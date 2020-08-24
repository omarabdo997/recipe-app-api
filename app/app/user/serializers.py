from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from django.http import request
from rest_framework.request import Request


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
        min_length = 5,
        write_only = True
    )
    # success = serializers.SerializerMethodField('success_method')

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name')
        # extra_kwargs = {'password':{'write_only': True, 'min_length': 5, }}

    # def success_method(self, a):
    #     return True
        

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user    

          


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        print(Request.data)
        user = authenticate(
            username = email,
            password = password,
        )
        if not user:
            msg = 'unable to authenticate with provided credintials'
            raise serializers.ValidationError(msg, code='authentication')

        validated_data['user'] = user    

        return validated_data    


