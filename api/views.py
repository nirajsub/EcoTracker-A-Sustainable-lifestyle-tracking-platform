

from .serializers import FollowingSerializer
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

class FollowingListAPIView(APIView):
    def get(self, request):
        user_profile = UserFollowers.objects.get(user=request.user)
        followers = user_profile.followers.all()
        following = user_profile.followings.all()
        followers_serializer = FollowingSerializer(followers, many=True).data
        following_serializer = FollowingSerializer(following, many=True).data
        context = {
            'followers':followers_serializer,
            'following':following_serializer,
        }
        return Response(context, status=status.HTTP_200_OK)
