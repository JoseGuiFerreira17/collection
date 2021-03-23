from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API - Collection",
      default_version='v1',
      description="Collection API ",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="joseguiferreira17@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

app_name = 'collection'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'
    ),
    url(
        r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    url(
        r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
    path('api/user/', include('collection.user.urls'), name='user'),
    path(
        'api/auth/',
        include('oauth2_provider.urls', namespace='oauth2_provider')
    ),
]
