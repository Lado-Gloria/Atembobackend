from rest_framework.test import APITestCase
from device.models import Device
from temperature_recording.models import TemperatureHumidityRecord
from .serializers import TemperatureHumidityRecordSerializer

class TemperatureHumidityRecordSerializerTest(APITestCase):
    def setUp(self):
        self.device = Device.objects.create(name='Test Device')

        self.record = TemperatureHumidityRecord.objects.create(
            device=self.device,
            humidity=60.25,
            temperature=25.50
        )

        self.serializer = TemperatureHumidityRecordSerializer(instance=self.record)

    def test_serializer_fields(self):
        expected_fields = ['id', 'device', 'time_stamp', 'humidity_with_unit', 'temperature_with_unit']
        self.assertEqual(list(self.serializer.fields.keys()), expected_fields)

    def test_humidity_with_unit(self):
        expected_result = '60.25% RH'
        self.assertEqual(self.serializer.data['humidity_with_unit'], expected_result)

    def test_temperature_with_unit(self):
        expected_result = '25.5°C'
        self.assertEqual(self.serializer.data['temperature_with_unit'], expected_result)