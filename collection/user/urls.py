from django.urls import path, include

from rest_framework import routers

from collection.user import views

app_name = 'user'

router = routers.DefaultRouter()

router.register('', views.UserViewSet, basename='user')

urlpatterns = [path('', include(router.urls))]
