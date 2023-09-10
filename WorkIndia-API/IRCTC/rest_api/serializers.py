#Model serializers bcoz the response object cannot natively handle complex data types
#so we create Serializers for Item models to create instances from object
#to respective data types the response object that can understand

from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from irctcBase.models import *

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        abstract = True

        def create(self, validated_data):
            user = User.objects.create(username=validated_data['name'], email=validated_data['email'])
            user.set_password(validated_data['password'])
            user.save()
            print(user)
            print(user.email)
            return user
        
class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = '__all__'

class TrainSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = ['train_name', 'seat_capacity']