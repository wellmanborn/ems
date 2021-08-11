from app.classes.SensorABC import SensorABC


class Fuse(SensorABC):

    sensor_type = "fuse"

    def get_sensor_data(self):
        data = self.client.db_read(int(self.db_id), 0, 1)
        self.value = self.get_bool(data, int(self.byte_id), int(self.bit_id))
        self.alarm = True != self.value
        return self.send_response_data()

    def get_sensor_config(self):
        return self.config

    def set_sensor_data(self):
        return self.config