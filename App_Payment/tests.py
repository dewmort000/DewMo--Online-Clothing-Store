from django.test import TestCase

class BillingAddressTest(TestCase):
	def setUp(self) -> None:
		user= User(email='dewmort@gmail.com')
		user.save()
		profile=Profile(username='dewan')
		self.billingAddress=BillingAddress(user=user)
		self.billingAddress.user.profile=profile

	def test__str__(self):
		self.assertEqual(self.billingAddress.__str__(), "dewan's billing add")

    def is_fully_filled(self):
        self.assertIs(self.billingAddress.test_is_fully_filled(),False)


class BillingFormTests(TestCase):
    def test_meta_class(self):
        form= BillingForm(data={})
        self.assertTrue(form.is_valid())


class ViewsTest(TestCase):
    def test_checkout(self):
        response=self.client.get(reverse('App_Payment:checkout'))
        self.assertEqual(response.status_code, 382)

    def test_payment(self):
        response=self.client.get('GatewayPageURL')
        self.assertEqual(response.status_code, 404)

    def test_complete(self):
        response=self.client.get('App_payment: complete'))
        self.assertEqual(response.status_code, 200)


    def test_purchase(self):
        response=self.client.get('App_shop: home'))
        self.assertEqual(response.status_code, 200)

    def test_order_view(self):
        response=self.client.get('App_shop: home'))
        self.assertEqual(response.status_code, 200)
