from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from location.models import Location

class LocationAPITest(APITestCase):

    def test_update_location(self):
        location = Location.objects.create(region_name='Test Region', installation_date='2023-09-08')

        data = {'region_name': 'Updated Region', 'other_attributes_here': '...'}

        url = reverse('location-detail', args=[location.id])
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        location.refresh_from_db()

        self.assertEqual(location.region_name, 'Updated Region')
