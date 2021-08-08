from django.test import TestCase

from app.classes.device import Device


class PlcTestCase(TestCase):

    def test_singleton(self):
        Device().set_status("writing")
        self.assertEqual(True, True)

    def test_singleton1(self):
        self.assertEqual(Device().get_status(), "writing")