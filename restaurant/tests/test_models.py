from django.test import TestCase
from restaurant.models import Menu


class MenuItemTest(TestCase):
    def setUp(self):
        Menu.objects.create(title = "dummy_1", price = 0, inventory = 0)
        Menu.objects.create(title = "dummy_2", price = 0, inventory = 0)

    def test_getall(self):
        item_1 = Menu.objects.get(title = "dummy_1")
        item_2 = Menu.objects.get(title = "dummy_2")

        self.assertEqual(str(item_1), "dummy_1 : 0.00") # Check the itemstr is same as __str__ of the model object
        self.assertEqual(str(item_2), "dummy_2 : 0.00") 