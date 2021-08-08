from app.classes.ConvertData import ConvertData
from app.classes.SensorInterface import SensorInterface


class Door(SensorInterface, ConvertData):

    sensor_type = "door"

    def get_sensor_data(self):
        data = self.client.db_read(int(self.db_id), 0, 1)
        self.value = self.get_bool(data, 0, 0)
        self.alarm = self.get_int(self.client.db_read(int(self.db_id), 8, 2))
        return self.send_response_data()

    def get_sensor_config(self):
        self.config["start_hour"] = int(self.get_int(self.client.db_read(int(self.db_id), 2, 1)))
        self.config["start_min"] = int(self.get_int(self.client.db_read(int(self.db_id), 3, 1)))
        self.config["end_hour"] = int(self.get_int(self.client.db_read(int(self.db_id), 4, 1)))
        self.config["end_min"] = int(self.get_int(self.client.db_read(int(self.db_id), 5, 1)))
        return self.config

    def set_sensor_data(self):
        self.client.db_write(int(self.db_id), 2, self.set_int(int(self.config['start_hour'])))
        self.client.db_write(int(self.db_id), 3, self.set_int(int(self.config['start_min'])))
        self.client.db_write(int(self.db_id), 4, self.set_int(int(self.config['end_hour'])))
        self.client.db_write(int(self.db_id), 5, self.set_int(int(self.config['end_min'])))
        return self.config
