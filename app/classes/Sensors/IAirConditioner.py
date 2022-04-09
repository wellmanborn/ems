from abc import ABC

from app.classes.SensorABC import SensorABC


class IAirConditioner(SensorABC):

    sensor_type = "airconditioner"
    config = {}

    def get_sensor_data(self):
        raise NotImplementedError

    def get_sensor_config(self):
        raise NotImplementedError


    def set_sensor_data(self):
        raise NotImplementedError

    def set_airconditioner_status(self, db, bit_id, status):
        raise NotImplementedError

    def reset_airconditioner(self, status = True):
        raise NotImplementedError
