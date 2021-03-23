from django.urls import path, include

from rest_framework import routers

from collection.book import views

app_name = 'book'

router = routers.DefaultRouter()

router.register('book', views.BookViewSet, basename='book')
router.register('category', views.CategoryViewSet, basename='category')

urlpatterns = [path('', include(router.urls))]