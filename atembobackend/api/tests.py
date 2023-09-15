from django.test import TestCase
from django.contrib.auth.models import Group, Permission
from registration.models import CustomUser

class CustomUserTestCase(TestCase):
    def setUp(self):
        self.group = Group.objects.create(name='Farmers Group')


        self.permission1 = Permission.objects.create(
            codename='view_profile',
            name='view profile',
            content_type=None, 
        )

    def test_create_user(self):
        user = CustomUser.objects.create_user(
            username='Becky',
            password='Becky',
            first_name='Becky',
            last_name='Nangila',
            email='becky@example.com',
        )

        self.assertEqual(user.username, 'Becky')
        self.assertEqual(user.first_name, 'Becky')
        self.assertEqual(user.last_name, 'Nangila')
        self.assertEqual(user.email, 'becky@example.com')

    def test_add_user_to_group(self):
        user = CustomUser.objects.create_user(
            username='Lado',
            password='6rwf2676eu',
            first_name='Lado',
            last_name='Gloria',
            email='lado@example.com',
        )

        user.groups.add(self.group)

        self.assertTrue(user.groups.filter(name='Users Group').exists())

    def test_user_permissions(self):
        user = CustomUser.objects.create_user(
            username='lado',
            password='password456',
            first_name='Lado',
            last_name='Gloria',
            email='lado@example.com',
        )

        user.user_permissions.add(self.permission1)

        self.assertTrue(user.has_perm('your_app_label.can_view_profile'))

    def test_user_str_method(self):
        user = CustomUser.objects.create_user(
            username='user3',
            password='password789',
            first_name='Eve',
            last_name='Brown',
            email='eve@example.com',
        )

        self.assertEqual(str(user), 'user3')
