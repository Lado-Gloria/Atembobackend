# from django.test import TestCase
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APIClient
# from registration.models import Farmer


# class FarmerAPITest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.farmer1 = Farmer.objects.create_user(
#             username='morine',
#             first_name='morine',
#             last_name='jebet',
#             email='jebet@gmail.com',
#             password='12345'
#         )
#         self.farmer2 = Farmer.objects.create_user(
#             username='mercy',
#             first_name='chia',
#             last_name='mercy',
#             email='chia@example.com',
#             password='456123'
#         )

#     def test_list_farmers(self):
#         url = reverse('farmers-list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 2)

#     def test_create_farmer(self):
#         url = reverse('farmers-list')
#         data = {
#             'username': 'testuser',
#             'first_name': 'Test',
#             'last_name': 'User',
#             'email': 'testuser@example.com',
#             'password': 'testpassword',
#         }
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Farmer.objects.count(), 3)

#     def test_retrieve_farmer(self):
#         url = reverse('farmers-detail', args=[self.farmer1.id])
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['username'], 'morine')

#     def test_update_farmer(self):
#         url = reverse('farmers-detail', args=[self.farmer1.id])
#         data = {
#             'first_name': 'Updated',
#             'last_name': 'Name',
#         }
#         response = self.client.patch(url, data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.farmer1.refresh_from_db()
#         self.assertEqual(self.farmer1.first_name, 'Updated')

#     def test_delete_farmer(self):
#         url = reverse('farmers-detail', args=[self.farmer1.id])
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertFalse(Farmer.objects.filter(id=self.farmer1.id).exists())