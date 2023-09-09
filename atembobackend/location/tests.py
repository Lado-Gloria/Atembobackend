from django.test import TestCase
from datetime import date
from .models import Location

class LocationTestCase(TestCase):
    def setUp(self):
        Location.objects.create(region_name="Test Region", installation_date="2023-09-08")

    def test_location_creation(self):
        location = Location.objects.get(region_name="Test Region")
        self.assertEqual(location.region_name, "Test Region")
        self.assertEqual(location.installation_date, "2023-09-08")
