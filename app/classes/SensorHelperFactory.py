from app.helpers.DoorHelper import DoorHelper
from app.helpers.FuseHelper import FuseHelper
from app.helpers.HumidityHelper import HumidityHelper
from app.helpers.PowerHelper import PowerHelper
from app.helpers.PoweroneHelper import PoweroneHelper
from app.helpers.PowerthreeHelper import PowerthreeHelper
from app.helpers.SmokeHelper import SmokeHelper
from app.helpers.TemperatureHelper import TemperatureHelper
from app.helpers.WaterleakageHelper import WaterleakageHelper
from app.helpers.CurrentHelper import CurrentHelper


class SensorHelperFactory():

    @staticmethod
    def get_sensor_helper(sensor_type):
        try:
            if sensor_type == "temperature":
                return TemperatureHelper()
            if sensor_type == "humidity":
                return HumidityHelper()
            if sensor_type == "power":
                return PowerHelper()
            if sensor_type == "waterleakage":
                return WaterleakageHelper()
            if sensor_type == "smoke":
                return SmokeHelper()
            if sensor_type == "door":
                return DoorHelper()
            if sensor_type == "fuse":
                return FuseHelper()
            if sensor_type == "current":
                return CurrentHelper()
            if sensor_type == "powerone":
                return PoweroneHelper()
            if sensor_type == "powerthree":
                return PowerthreeHelper()
            raise AssertionError("Sensor Form Not Fount")
        except AssertionError as e:
            raise AssertionError(e)
