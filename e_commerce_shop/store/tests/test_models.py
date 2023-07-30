from django.contrib.auth.models import User
from django.test import TestCase

from e_commerce_shop.store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='test_name', slug='test_name')

    def test_Category_model_entry(self):
        """
        Test Category model data insertion /type/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_Category_model_entry(self):
        """
              Test Category model default name
              """
        data = self.data1
        self.assertEquals(str(data), 'test_name')

# class TestProductModel(TestCase):
#     def setUp(self):
#         Category.objects.create(name='test_name', slug='test_name')
#         User.objects.create(username='adminadmin')
#         self.data1 = Product.objects.create(
#             category_id=1,
#             title='test test',
#             created_by_id=1,
#             slug='test_test',
#             price='10.00',
#             image='test',
#         )
#
#     def test_Product_model_entry(self):
#         """
#         Test product model data insertion /type/field attributes
#         """
#         data = self.data1
#         self.assertTrue(isinstance(data, Product))
#         self.assertEquals(str(data), 'test_name')
