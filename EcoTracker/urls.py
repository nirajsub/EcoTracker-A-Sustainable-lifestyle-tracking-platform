from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Presu's Skin Care API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('account/', include('account.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('auth', include("django.contrib.auth.urls")),
    path('', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0)),
]
