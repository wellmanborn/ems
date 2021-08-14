from app.classes.SensorABC import SensorABC


class Current(SensorABC):

    sensor_type = "current"

    def get_sensor_data(self):
        self.value = self.get_real(self.client.db_read(int(self.db_id), 12, 4))
        self.alarm = self.get_int(self.client.db_read(int(self.db_id), 18, 2))
        return self.send_response_data()

    def get_sensor_config(self):
        self.config["high"] = int(self.get_real(self.client.db_read(int(self.db_id), 4, 4)))
        self.config["time"] = int(self.get_int(self.client.db_read(int(self.db_id), 8, 4)) / 1000)
        return self.config

    def set_sensor_data(self):
        self.client.db_write(int(self.db_id), 4, self.set_real(int(self.config['high'])))
        self.client.db_write(int(self.db_id), 8, self.set_dword(int(self.config['time']) * 1000))
        return self.config
