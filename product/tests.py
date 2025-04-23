from django.test import TestCase

# Create your tests here.
from  .models import Product
from .models import Category

class ProductTestCase(TestCase):
    def setUp(self):
        self.p = Product.objects.create(title="tênis", description="usado para calçar", price=38, active= True)
        categoria = Category.objects.create(title="calçados")
        self.p.category.set([categoria])


    def testCriacaoTenis(self):
        product = Product.objects.get(title="tênis")
        self.assertEqual(product.description, "usado para calçar")