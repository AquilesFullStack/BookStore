from django.urls import path, include 
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from product import viewset

router = routers.SimpleRouter()
router.register(r'product', viewset.Product_ViewSet, basename='product'),
router.register(r'category', viewset.Category_ViewSet, basename='category')


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]