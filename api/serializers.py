from rest_framework import serializers
from .models import *

class UserFollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowers
        fields = '__all__'


class ActivityCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityCategory
        fields = '__all__'


class SubActivityCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubActivityCategory
        fields = '__all__'


class SubActivityCategoryChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubActivityCategoryChoices
        fields = '__all__'


class ActivityPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPost
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventContribution
        fields = '__all__'


class EventPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPost
        fields = '__all__'


class EventParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventParticipant
        fields = '__all__'

class FollowingSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ['username']

class ImageClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageClassification
        fields = ['image']