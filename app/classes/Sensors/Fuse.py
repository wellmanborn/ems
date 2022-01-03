from app.classes.SensorABC import SensorABC


class Fuse(SensorABC):

    sensor_type = "fuse"

    def get_sensor_data(self):
        data = self.client.db_read(int(self.db_id), int(self.byte_id), 1)
        self.value = self.get_bool(data, 0, int(self.bit_id))
        self.alarm = 4 if self.value == False else 0
        return self.send_response_data()

    def get_sensor_config(self):
        return self.config

    def set_sensor_data(self):
        return self.config