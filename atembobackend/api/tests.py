from django.test import TestCase, Client
from flowrate.models import Device, FlowRate
from api.serializers import DeviceSerializer, FlowRateSerializer
from rest_framework import status
from django.test import TestCase
from .models import Device, FlowRate

from django.test import TestCase
from flowrate.models import Device, FlowRate
from .serializers import DeviceSerializer, FlowRateSerializer


class DeviceSerializerTestCase(TestCase):
    def test_device_serializer(self):
        device = Device.objects.create(device_owner="Moses Makau")

        serializer = DeviceSerializer(device)

        expected_data = {
            'id': device.id,
            'device_owner': 'Moses Makau',
        }


class FlowRateSerializerTestCase(TestCase):
    def test_flowrate_serializer(self):
        device = Device.objects.create(device_owner="Moses Makau")

        flow_rate = FlowRate.objects.create(device=device, flow_rate=0.2542)

        serializer = FlowRateSerializer(flow_rate)

        expected_data = {
            'id': flow_rate.id,
            'device': device.id,
            'flow_rate': 0.2542,
        }

class FlowRateAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_flowrate_list_api(self):
        device1 = Device.objects.create(device_owner="Ann Aketch")
        device2 = Device.objects.create(device_owner="Rose Kivuva")

        flow1 = FlowRate.objects.create(device=device1, flow_rate= 0.0014)
        flow2 = FlowRate.objects.create(device=device2, flow_rate= 0.0136)

        response = self.client.get('/api/flowrate/')

        serializer = FlowRateSerializer([flow1, flow2], many=True)
        expected_data = serializer.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_flowrate_detail_api(self):
        device = Device.objects.create(device_owner="Test Device")

        flow = FlowRate.objects.create(device=device, flow_rate=0.2542)

        response = self.client.get(f'/api/flowrate/{flow.pk}/')

        serializer = FlowRateSerializer(flow)
        expected_data = serializer.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)



class DeviceModelTestCase(TestCase):
    def test_device_serial_number_generation(self):
        device = Device(device_owner="Megan Wairimu")
        device.save()
        self.assertIsNotNone(device.serial_number)

    def test_device_string_representation(self):
        device = Device(device_owner="Megan Wairimu")
        self.assertEqual(str(device), "Megan Wairimu")

class FlowRateModelTestCase(TestCase):
    def test_flow_rate_creation(self):
        device = Device(device_owner="Megan Wairimu")
        device.save()
        flow_rate = FlowRate(device=device, flow_rate=0.1234)
        flow_rate.save()
        self.assertEqual(FlowRate.objects.count(), 1)