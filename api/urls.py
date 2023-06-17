from django.urls import path
from .views import *

urlpatterns = [
    path('following/', FollowingListAPIView.as_view(), name='following-list'),
]
