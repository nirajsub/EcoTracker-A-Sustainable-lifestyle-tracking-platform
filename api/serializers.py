from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class FollowingSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ['username']

# class ItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ClassifyItem
#         fields = '__all__'

class ImageClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageClassification
        fields = ['image']