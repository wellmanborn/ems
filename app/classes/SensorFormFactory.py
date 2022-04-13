from app.forms.sensors.temperature import TemperatureForm
from app.forms.sensors.humidity import HumidityForm
from app.forms.sensors.current import CurrentForm
from app.forms.sensors.door import DoorForm
from app.forms.sensors.electricity import PowerForm
from app.forms.sensors.fan import FanForm
from app.forms.sensors.fuse import FuseForm
from app.forms.sensors.one_phase_electricity import OnePhaseElectricityForm
from app.forms.sensors.smoke import SmokeForm
from app.forms.sensors.three_phase_electricity import ThreePhaseElectricityForm
from app.forms.sensors.water_leakage import WaterleakageForm


class SensorFormFactory():

    @staticmethod
    def get_sensor_form(sensor_type, post_data = None):
        try:
            if sensor_type == "temperature":
                return TemperatureForm(post_data)
            if sensor_type == "humidity":
                return HumidityForm(post_data)
            if sensor_type == "power":
                return PowerForm(post_data)
            if sensor_type == "waterleakage":
                return WaterleakageForm(post_data)
            if sensor_type == "door":
                return DoorForm(post_data)
            if sensor_type == "smoke":
                return SmokeForm(post_data)
            if sensor_type == "fuse":
                return FuseForm(post_data)
            if sensor_type == "current":
                return CurrentForm(post_data)
            if sensor_type == "powerone":
                return OnePhaseElectricityForm(post_data)
            if sensor_type == "powerthree":
                return ThreePhaseElectricityForm(post_data)
            if sensor_type == "fan":
                return FanForm(post_data)
            raise AssertionError("Sensor Form Not Fount")
        except AssertionError as e:
            raise AssertionError(e)
