from app.forms import TemperatureForm, HumidityForm, PowerForm, WaterleakageForm, DoorForm, SmokeForm, FuseForm


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
            raise AssertionError("Sensor Form Not Fount")
        except AssertionError as e:
            raise AssertionError(e)
