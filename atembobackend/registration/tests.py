from django.test import TestCase
from .models import Registration


# Create your tests here.
class RegistrationModelTest(TestCase):

    def test_create_registration(self):
        registration = Registration.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            password="password123",
        )

        self.assertEqual(registration.first_name, "John")
        self.assertEqual(registration.last_name, "Doe")
        self.assertEqual(registration.email, "johndoe@example.com")
        self.assertEqual(registration.password, "password123")

    def test_str_representation(self):
        registration = Registration.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            password="password123",
        )

        self.assertEqual(str(registration), "John")

if __name__ == "__main__":
    unittest.main()