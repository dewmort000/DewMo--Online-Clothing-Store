from django.test import TestCase
from django.urls import reverse
from App_Login.models import Profile, User, UserManager
from App_Login.forms import ProfileForm ,SignUpForm


class UserManagerTests(TestCase):
    def test_create_user(self):
        user=User.objects._create_user('dewmort@gmail.com','qwerty12')
        self.assertTrue(isinstance(user, User))

    def test_create_superuser(self):
        user= User.objects._create_superuser('is staff', 'is superuser') 
        self.assertTrue(isinstance(user, User))
    
class UserTests(TestCase):
    def setUp(self):
        self.user= User(email='dewmort@gmail.com')

    def test__str__(self):
        self.assertEqual(self.user.__str__(), 'dewmort@gmail.com')

    def test_get_full_name(self):
        self.assertEqual(self.user.get_full_name(), 'dewmort@gmail.com')

    def test_get_short_name(self):
        self.assertEqual(self.user.get_short_name(), 'dewmort@gmail.com')

class ProfileTests(TestCase):
    def setUp(self):
        self.profile= Profile(username='dewan', address_1='mdpur',zipcode='1207', city='dhaka', country='Bangladesh')
    
    def test__str__(self):
        self.assertEqual(self.profile.__str__(), "dewan's Profile")
    
    def test_is_fully_filled(self):
        self.assertIs(self.profile.is_fully_filled(),False)

class ProfileFormTests(TestCase):
    def test_meta_class(self):
        form = UserProfileForm(data={})
        self.assertTrue(form.is_valid())


class SignUpFormTests(TestCase):
    def test_meta_class(self):
        form = SignUpForm(data={})
        self.assertFalse(form.is_valid())


class ViewsTest(TestCase):
    def test_sign_up(self):
        response = self.client.get(reverse('App_Login:signup'))
        self.assertEqual(response.status_code, 200)

    def test_user_login(self):
        response = self.client.get(reverse('App_Login:login'))
        self.assertEqual(response.status_code, 200)

    def test_user_logout(self):
        response = self.client.get(reverse('App_Login:logout'))
        self.assertEqual(response.status_code, 302)

    def test_user_profile(self):
        response = self.client.get(reverse('App_Login:profile'))
        self.assertEqual(response.status_code, 302)