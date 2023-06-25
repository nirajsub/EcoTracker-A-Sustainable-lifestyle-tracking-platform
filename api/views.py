

from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
import openai
from django.conf import settings
from openai import api_key
from .image_classification import classify_image
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .ai import classify_image
from .serializers import ImageClassificationSerializer

class classify_image_view(APIView):
    def get(self, request, *args, **kwargs):
        img = ImageClassification.objects.get(saved=False)
        serializer = ImageClassificationSerializer(img, many=False).data
        return Response(serializer, status=status.HTTP_200_OK)
    def put(self, request, *args, **kwargs):
        if request.method == 'PUT':
            image_obj = ImageClassification.objects.get(saved=False)
            image_file = image_obj.image
            if image_file:
                predicted_labels = classify_image(image_file.path)
                serializer = ImageClassificationSerializer(instance=image_obj, data={
                    'predicted_labels': predicted_labels
                }, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=201)
                else:
                    return JsonResponse(serializer.errors, status=400)
            else:
                return JsonResponse({'error': 'No image file provided.'}, status=400)
        return JsonResponse({'error': 'Invalid request method.'}, status=405)


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

class FollowUser(APIView):
    def post(self, request, pk, *args, **kwargs):
        user = User.objects.get(id=pk)
        thisuser = self.request.user
        followuser = UserFollowers.objects.get_or_create(user = user)
        followuser = UserFollowers.objects.get(user=user)
        followuser.followers.add(thisuser)
        followuser.save()
        myfollowings = UserFollowers.objects.get_or_create(user=thisuser)
        myfollowings = UserFollowers.objects.get(user=thisuser)
        myfollowings.followings.add(user)
        myfollowings.save()
        serializer = UserFollowersSerializer(myfollowings).data
        return Response(serializer, status=status.HTTP_200_OK)

