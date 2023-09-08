from django.test import TestCase
from datetime import date
from .models import Location

class LocationTestCase(TestCase):
    def setUp(self):
        Location.objects.create(region_name="Test Region", installation_date=date.today())

    def test_location_str(self):
        location = Location.objects.get(region_name="Test Region")
        self.assertEqual(str(location), "Test Region")