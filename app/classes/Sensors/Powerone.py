from app.classes.SensorABC import SensorABC


class Powerone(SensorABC):

    sensor_type = "powerone"
    config = {
        "high": 230,
        "low": 200,
        "time": 5
    }

    def get_sensor_data(self):
        self.value = self.get_real(self.client.db_read(int(self.db_id), 0, 4))
        self.alarm = self.get_int(self.client.db_read(int(self.db_id), 18, 2))
        return self.send_response_data()

    def get_sensor_config(self):
        self.config["high"] = int(self.get_real(self.client.db_read(self.db_id, 8, 4)))
        self.config["low"] = int(self.get_real(self.client.db_read(self.db_id, 4, 4)))
        self.config["time"] = int(self.get_int(self.client.db_read(int(self.db_id), 12, 4)) / 1000)
        return self.config

    def set_sensor_data(self):
        self.client.db_write(int(self.db_id), 8, self.set_real(int(self.config['high'])))
        self.client.db_write(int(self.db_id), 4, self.set_real(int(self.config['low'])))
        self.client.db_write(int(self.db_id), 12, self.set_dword(int(self.config['time']) * 1000))
        return self.config