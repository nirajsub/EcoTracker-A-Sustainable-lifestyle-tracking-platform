from django.urls import path
from .views import *

urlpatterns = [
    path('following/', FollowingListAPIView.as_view(), name='following-list'),
    path('classify-image/', classify_image_view.as_view(), name='classify_image'),
]
