from django.test import TestCase, Client
from flowrate.models import Device, FlowRate
from rest_framework import status
from api.serializers import FlowRateSerializer

class FlowRateAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_flowrate_list_api(self):
        device1 = Device.objects.create(name="Moses Makau")
        device2 = Device.objects.create(name="Lilian Mutheu")

        flow1 = FlowRate.objects.create(device=device1, flow_rate=0.2542)
        flow2 = FlowRate.objects.create(device=device2, flow_rate=0.2542)


        response = self.client.get('/api/flowrate/')


        serializer = FlowRateSerializer([flow1, flow2], many=True)
        expected_data = serializer.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_flowrate_detail_api(self):
        device = Device.objects.create(name="Test Device")

        flow = FlowRate.objects.create(device=device, flow_rate=0.2542)


        response = self.client.get(f'/api/flowrate/{flow.pk}/')


        serializer = FlowRateSerializer(flow)
        expected_data = serializer.data


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)