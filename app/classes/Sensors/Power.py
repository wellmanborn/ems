from app.classes.SensorABC import SensorABC


class Power(SensorABC):

    sensor_type = "power"

    def get_sensor_data(self):
        data = self.client.db_read(int(self.db_id), 0, 1)
        self.value = self.get_bool(data, 0, 0)
        self.alarm = self.get_int(self.client.db_read(int(self.db_id), 8, 2))
        return self.send_response_data()

    def set_sensor_data(self):
        self.client.db_write(int(self.db_id), 2, self.set_dword(int(self.config['time']) * 1000))
        return self.config

    def get_sensor_config(self):
        self.config["time"] = int(self.get_int(self.client.db_read(int(self.db_id), 2, 4)) / 1000)
        return self.config