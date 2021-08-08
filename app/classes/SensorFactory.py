class SensorFactory():

    @staticmethod
    def get_sensor(SensorType):
        try:
            if SensorType == "power":
                from app.classes.Sensors.Power import Power
                return Power()
            if SensorType == "temperature":
                from app.classes.Sensors.Temperature import Temperature
                return Temperature()
            if SensorType == "humidity":
                from app.classes.Sensors.Humidity import Humidity
                return Humidity()
            if SensorType == "waterleakage":
                from app.classes.Sensors.Waterleakage import Waterleakage
                return Waterleakage()
            if SensorType == "door":
                from app.classes.Sensors.Door import Door
                return Door()
            if SensorType == "smoke":
                from app.classes.Sensors.Smoke import Smoke
                return Smoke()
            if SensorType == "fuse":
                from app.classes.Sensors.Fuse import Fuse
                return Fuse()
            if SensorType == "airconditioner":
                from app.classes.Sensors.Airconditioner import Airconditioner
                return Airconditioner()
            raise AssertionError("Sensor Not Fount")
        except AssertionError as e:
            raise AssertionError(e)
