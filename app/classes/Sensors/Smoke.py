from app.classes.SensorABC import SensorABC


class Smoke(SensorABC):

    sensor_type = "smoke"

    def get_sensor_data(self):
        if "data_block_type" in self.setting and self.setting["data_block_type"] == "word":
            self.alarm = self.value = self.get_int(self.client.db_read(int(self.db_id), int(self.byte_id), 2))
        else:
            data = self.client.db_read(int(self.db_id), int(self.byte_id), 1)
            self.value = self.get_bool(data, 0, int(self.bit_id))
            self.alarm = 4 if self.value is True else 0
        return self.send_response_data()

    def get_sensor_config(self):
        return self.config

    def set_sensor_data(self):
        return self.config