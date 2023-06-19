

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
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .ai import classify_image
from .serializers import ImageClassificationSerializer

class classify_image_view(APIView):
    def get(self, request, *args, **kwargs):
        img = ImageClassification.objects.get(saved=False)
        serializer = ImageClassificationSerializer(img, many=False).data
        return Response(serializer, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            image_obj = ImageClassification.objects.get(saved=False)
            image_file = image_obj.image

            if image_file:
                predicted_labels = classify_image(image_file.path)
                serializer = ImageClassificationSerializer(data={
                    'image': image_file,
                    'predicted_labels': predicted_labels
                })
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=201)
                else:
                    return JsonResponse(serializer.errors, status=400)
            else:
                return JsonResponse({'error': 'No image file provided.'}, status=400)
        return JsonResponse({'error': 'Invalid request method.'}, status=405)

# @api_view(['POST'])
# def classify_image_view(request):
#     if request.method == 'POST':
#         img = ImageClassification.objects.get(saved=false)
#         image_file = img.image

#         if image_file:
#             predicted_labels = classify_image(image_file.path)
#             serializer = ImageClassificationSerializer(data={
#                 'image': image_file,
#                 'predicted_labels': predicted_labels
#             })
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse(serializer.data, status=201)
#             else:
#                 return JsonResponse(serializer.errors, status=400)
#         else:
#             return JsonResponse({'error': 'No image file provided.'}, status=400)
#     return JsonResponse({'error': 'Invalid request method.'}, status=405)

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

# def classify_image_view(request):
#     if request.method == 'POST':
#         image_file = request.FILES.get('image')

#         if image_file:
#             predicted_labels = classify_image(image_file.path)
#             # Do something with the predicted labels
#             # For example, you can return the predicted labels as a JSON response
#             return JsonResponse({'predicted_labels': predicted_labels.tolist()})
#         else:
#             # Handle case when no image file is provided
#             return JsonResponse({'error': 'No image file provided.'}, status=400)

#     # Handle GET or other HTTP methods
#     return JsonResponse({'error': 'Invalid request method.'}, status=405)


# class ItemClassificationView(APIView):
#     def post(self, request, format=None):
#         image = request.data.get('image')
#         if image:
#             openai_key = getattr(settings, 'OPENAI_API_KEY', None)
            
#             if not openai_key:
#                 return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#             openai.api_key = openai_key
#             response = openai.Classification.create(
#                 model='davinci',
#                 inputs={
#                     'image': image,
#                     'prompt': 'Classify this image as recyclable, garbage, or compostable.'
#                 }
#             )
#             category = response.choices[0].text.strip().lower()
#             item = Item.objects.create(category=category, image=image)
#             serializer = ItemSerializer(item)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response({'error': 'No image provided'}, status=status.HTTP_400_BAD_REQUEST)