
 
from django.test import TestCase
from django.urls import reverse
from App_Shop.models import Product, Category
from App_Order.models import Cart, Order
from App_Login.models import User


class CartTest(TestCase):
    def setUp(self) -> None:
        user = User(email="1235@gmail.com")
        user.save()
        category=Category(title="shirt")
        category.save()
        item = Product(name="Silk White Shirt", price=1200, category = category)
        item.save()
        self.cart = Cart(user=user, item =item, quantity=3)
        self.cart.save()

    def test__str__(self):
        self.assertEqual(self.cart.__str__(),"3 X Silk White Shirt")

    def test_get_total(self):
        self.assertEqual(self.cart.get_total(),'3600.00')





class OrderTest(TestCase):
    def setUp(self) -> None:
        user = User(email="dewmort@gmail.com")
        user.save()
        category=Category(title="Papercrafts")
        category.save()
        item1 = Product(name="Gift Cards", price=15.00, category = category)
        item1.save()
        item2 = Product(name="Gift Box", price=20.00, category = category)
        item2.save()
        cart1 = Cart(user=user, item =item1, quantity=3)
        cart1.save()
        cart2 = Cart(user=user, item =item2, quantity=2)
        cart2.save()
        self.order = Order(user=user)
        self.order.save()
        self.order.orderitems.add(cart1)
        self.order.orderitems.add(cart2)
                               
    def test_get_totals(self):
        self.assertEqual(self.order.get_totals(),85.0)

class ViewsTest(TestCase):
    def test_add_to_cart(self):
        response = self.client.get(reverse('App_Order:add', args=(1,)))
        self.assertEqual(response.status_code,302)

    def test_cart_view(self):
        response = self.client.get(reverse('App_Order:cart'))
        self.assertEqual(response.status_code,302)

    def test_remove_from_cart(self):
        response = self.client.get(reverse('App_Order:remove', args=(1,)))
        self.assertEqual(response.status_code,302)

    def test_increase_cart(self):
        response = self.client.get(reverse('App_Order:increase', args=(1,)))
        self.assertEqual(response.status_code,302)

    def test_decrease_cart(self):
        response = self.client.get(reverse('App_Order:decrease', args=(1,)))
        self.assertEqual(response.status_code,302)