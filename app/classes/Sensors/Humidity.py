from app.classes.ConvertData import ConvertData
from app.classes.SensorInterface import SensorInterface


class Humidity(SensorInterface, ConvertData):

    sensor_type = "humidity"

    def get_sensor_data(self):
        self.value = self.get_real(self.client.db_read(int(self.db_id), 56, 4))
        self.alarm = self.get_int(self.client.db_read(int(self.db_id), 62, 2))
        return self.send_response_data()

    def get_sensor_config(self):
        self.config["very_high"] = int(self.get_real(self.client.db_read(int(self.db_id), 28, 4)))
        self.config["high"] = int(self.get_real(self.client.db_read(int(self.db_id), 32, 4)))
        self.config["low"] = int(self.get_real(self.client.db_read(int(self.db_id), 36, 4)))
        self.config["very_low"] = int(self.get_real(self.client.db_read(int(self.db_id), 40, 4)))
        self.config["offset"] = int(self.get_real(self.client.db_read(int(self.db_id), 48, 4)))
        return self.config

    def set_sensor_data(self):
        self.client.db_write(int(self.db_id), 28, self.set_real(int(self.config['very_high'])))
        self.client.db_write(int(self.db_id), 32, self.set_real(int(self.config['high'])))
        self.client.db_write(int(self.db_id), 36, self.set_real(int(self.config['low'])))
        self.client.db_write(int(self.db_id), 40, self.set_real(int(self.config['very_low'])))
        self.client.db_write(int(self.db_id), 48, self.set_real(int(self.config['offset'])))
        return self.config
