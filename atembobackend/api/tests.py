from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from flowrate.models import Device, FlowRate
from api.serializers import DeviceSerializer, FlowRateSerializer

class DeviceAPITestCase(APITestCase):
    def test_device_list_api(self):
        device1 = Device.objects.create(device_owner="John Doe")
        device2 = Device.objects.create(device_owner="Jane Smith")

        response = self.client.get(reverse('device-list'))

        serializer = DeviceSerializer([device1, device2], many=True)
        expected_data = serializer.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_device_detail_api(self):
        device = Device.objects.create(device_owner="Test Device")

        response = self.client.get(reverse('device-detail', args=[device.pk]))

        serializer = DeviceSerializer(device)
        expected_data = serializer.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_device_create_api(self):
        data = {'device_owner': 'New Device Owner'}

        response = self.client.post(reverse('device-list'), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Device.objects.count(), 1)
        self.assertEqual(Device.objects.get().device_owner, 'New Device Owner')

    def test_device_update_api(self):
        device = Device.objects.create(device_owner="Old Owner")
        data = {'device_owner': 'New Owner'}

        response = self.client.put(reverse('device-detail', args=[device.pk]), data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Device.objects.get().device_owner, 'New Owner')

    def test_device_delete_api(self):
        device = Device.objects.create(device_owner="To be deleted")

        response = self.client.delete(reverse('device-detail', args=[device.pk]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Device.objects.count(), 0)


class FlowRateAPITestCase(APITestCase):
    def test_flowrate_list_api(self):
        device1 = Device.objects.create(device_owner="Ann Aketch")
        device2 = Device.objects.create(device_owner="Rose Kivuva")

        flow1 = FlowRate.objects.create(device=device1, flow_rate=0.0014)
        flow2 = FlowRate.objects.create(device=device2, flow_rate=0.0136)

        response = self.client.get(reverse('flowrate-list'))

        serializer = FlowRateSerializer([flow1, flow2], many=True)
        expected_data = serializer.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_flowrate_detail_api(self):
        device = Device.objects.create(device_owner="Test Device")
        flow = FlowRate.objects.create(device=device, flow_rate=0.2542)

        response = self.client.get(reverse('flowrate-detail', args=[flow.pk]))

        serializer = FlowRateSerializer(flow)
        expected_data = serializer.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_flowrate_create_api(self):
        device = Device.objects.create(device_owner="Test Device")
        data = {'device': device.pk, 'flow_rate': 0.1234}

        response = self.client.post(reverse('flowrate-list'), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FlowRate.objects.count(), 1)
        self.assertEqual(FlowRate.objects.get().flow_rate, 0.1234)

    def test_flowrate_update_api(self):
        device = Device.objects.create(device_owner="Test Device")
        flow = FlowRate.objects.create(device=device, flow_rate=0.1234)
        data = {'device': device.pk, 'flow_rate': 0.5678}

        response = self.client.put(reverse('flowrate-detail', args=[flow.pk]), data)


    def test_flowrate_delete_api(self):
        device = Device.objects.create(device_owner="Test Device")
        flow = FlowRate.objects.create(device=device, flow_rate=0.1234)

        response = self.client.delete(reverse('flowrate-detail', args=[flow.pk]))

