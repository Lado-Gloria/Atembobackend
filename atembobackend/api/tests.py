from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from location.models import Location
from api.serializers import LocationSerializer

class LocationAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def create_location(self, region_name="Test Region", installation_date="2023-09-08"):
        return Location.objects.create(region_name=region_name, installation_date=installation_date)

    def test_create_location(self):
        url = reverse('location-list-create')
        data = {
            'region_name': 'New Test Region',
            'installation_date': '2023-09-09'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Location.objects.count(), 1)
        self.assertEqual(Location.objects.get().region_name, 'New Test Region')

    def test_list_locations(self):
        self.create_location()
        url = reverse('location-list-create')
        response = self.client.get(url)
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_location(self):
        location = self.create_location()
        url = reverse('location-detail', args=[location.id])
        response = self.client.get(url)
        serializer = LocationSerializer(location)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_update_location(self):
      location = self.create_location()
      url = reverse('location-detail', args=[location.id])
      updated_data = {'region_name': 'Updated Region'}
      response = self.client.put(url, updated_data, format='json')
      location.refresh_from_db()
   

    def test_delete_location(self):
        location = self.create_location()
        url = reverse('location-detail', args=[location.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Location.objects.count(), 0)