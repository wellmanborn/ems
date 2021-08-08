from app.classes.ConvertData import ConvertData
from app.classes.Device import Device
from app.classes.SensorInterface import SensorInterface


class Waterleakage(SensorInterface, ConvertData):

    sensor_type = "waterleakage"

    def get_sensor_data(self):
        data = self.client.db_read(int(self.db_id), 0, 1)
        value = self.get_bool(data, 0, 0)
        alarm = self.get_int(self.client.db_read(int(self.db_id), 8, 2))
        return self.send_response_data()

    def get_sensor_config(self):
        self.config["time"] = int(self.get_int(self.client.db_read(int(self.db_id), 2, 4)) / 1000)
        return self.config

    def set_sensor_data(self):
        self.client.db_write(int(self.db_id), 2, self.set_dword(int(self.config['time']) * 1000))
        return self.config