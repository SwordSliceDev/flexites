from django.test import TestCase
from .models import User, Organization

class UserModelTest(TestCase):
    def setUp(self):
        self.org = Organization.objects.create(name='Test Organization', description='Description')
        self.user = User.objects.create_user(
            email='test@example.com',
            password='password',
            first_name='Test',
            last_name='User',
            phone='123456789'
        )
        self.user.organizations.add(self.org)

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.organizations.count(), 1)