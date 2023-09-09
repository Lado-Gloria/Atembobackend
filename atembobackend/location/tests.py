import datetime
from django.test import TestCase
from location.models import Location

class LocationTestCase(TestCase):

    def test_location_creation(self):
        location = Location.objects.create(
            region_name='Test Region',
            installation_date=datetime.date(2023, 9, 8),
            other_attributes_here='...',
        )

       
        self.assertEqual(location.installation_date, datetime.date(2023, 9, 8))
