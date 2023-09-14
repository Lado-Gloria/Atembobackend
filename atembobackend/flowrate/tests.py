from django.test import TestCase
from .models import Device, FlowRate
from django.test import TestCase, Client
from django.urls import reverse
from .models import FlowRate

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




class FlowRateViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_water_flow_list(self):
        response = self.client.get(reverse('waterflow_list'))
        self.assertEqual(response.status_code, 200)

    def test_water_flow_detail(self):
        flow_rate = FlowRate.objects.create(serial_number="1234", flow_rate=0.1234)
        response = self.client.get(reverse('waterflow_detail', args=[flow_rate.serial_number]))
        self.assertEqual(response.status_code, 200)

    def test_daily_average_flow(self):
        FlowRate.objects.create(serial_number="1234", flow_rate=0.1)
        FlowRate.objects.create(serial_number="1234", flow_rate=0.2)
        response = self.client.get(reverse('daily_average_flow', args=["1234"]))
        self.assertEqual(response.status_code, 200)

