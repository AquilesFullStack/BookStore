from rest_framework.viewsets import ModelViewSet

from product.models import Category
from product.serializers import CategorySerializer

class Category_ViewSet(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all().order_by('id')