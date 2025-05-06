from django.urls import path, include 
from rest_framework import routers

from product import viewset

router = routers.SimpleRouter()
router.register(r'product', viewset.Product_ViewSet, basename='product'),
router.register(r'category', viewset.Category_ViewSet, basename='category')


urlpatterns = [
    path('', include(router.urls))
]