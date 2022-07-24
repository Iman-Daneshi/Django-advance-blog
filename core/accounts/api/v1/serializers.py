from rest_framework import serializers
from django.core import exceptions
import django.contrib.auth.password_validation as validators
from ...models import User

class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField()

    class Meta:
        model = User
        fields = ('email', 'password', 'password1')

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password1'):
            raise serializers.ValidationError({'detail': 'passwords do not match'})
        
        try:
            validators.validate_password(attrs.get('password'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'password':list(e.messages)})
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop('password1',None)
        return User.objects.create_user(**validated_data)