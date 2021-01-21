from django.test import TestCase
from django.urls import reverse

from accounts.models import CustomUser
from accounts.views import SignupView


class DefaultHomePageTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='mytestpassword',
        )

    def test_guest_user_status_code_redirect(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            '{}?next={}'.format(reverse('login'), reverse('home'))
        )

    def test_logged_user_and_status_code(self):
        response = self.client.login(
            username='testuser',
            password='mytestpassword',
        )
        access_home_page_url = self.client.get('/')
        self.assertEqual(access_home_page_url.status_code, 200)
        self.assertTrue(response)


class SignUpTests(TestCase):

    def setUp(self):
        self.username = 'testuser'
        self.password = 'mytestpassword'
        self.privacy_check = True

    def test_get_signup_status_code(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_post_create_user_redirect_login(self):
        response = self.client.post(reverse('signup'), {
            'username': self.username,
            'password1': self.password,
            'password2': self.password,
            'privacy_check': self.privacy_check,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))


class LoginTests(TestCase):

    def setUp(self):
        CustomUser.objects.create_user(
            username='testuser',
            password='mytestpassword',
        )

    def test_get_login_page_status_code(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_post_logged_in_redirect_home(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'mytestpassword',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))


class LogoutTests(TestCase):

    def test_logout_status_codee(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)


class PrivecyPolicyTests(TestCase):

    def test_get_page_status_code(self):
        response = self.client.get(reverse('privacy_policy'))
        self.assertEqual(response.status_code, 200)
