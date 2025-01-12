from django.test import TestCase
from restaurant.models import Menu


class MenuViewTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title = "IceCream", price = 30, inventory = 20)

        self.assertEqual(str(item), "IceCream : 30") # Check the itemstr is same as __str__ of the model object