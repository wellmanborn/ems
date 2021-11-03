from app.classes.SensorABC import SensorABC


class Powerthree(SensorABC):

    sensor_type = "powerthree"
    config = {
        "high": 410,
        "low": 360,
        "time": 5
    }

    def get_sensor_data(self):
        self.value = self.get_real(self.client.db_read(int(self.db_id), int(self.byte_id), 4))
        self.alarm = self.get_int(self.client.db_read(int(self.db_id), 42, 2))
        return self.send_response_data()

    # def get_sensor_data(self):
    #     self.value = 0
    #     self.alarm = self.get_int(self.client.db_read(int(self.db_id), 42, 2))
    #     all_data = {}
    #     all_data["value_rs"] = self.get_real(self.client.db_read(int(self.db_id), 0, 4))
    #     all_data["value_rt"] = self.get_real(self.client.db_read(int(self.db_id), 4, 4))
    #     all_data["value_st"] = self.get_real(self.client.db_read(int(self.db_id), 8, 4))
    #     return self.send_response_data(all_data)

    def get_sensor_config(self):
        self.config["high"] = int(self.get_real(self.client.db_read(self.db_id, 24 + int(self.byte_id), 4)))
        # self.config["high_rt"] = int(self.get_real(self.client.db_read(self.db_id, 28, 4)))
        # self.config["high_st"] = int(self.get_real(self.client.db_read(self.db_id, 32, 4)))
        self.config["low"] = int(self.get_real(self.client.db_read(self.db_id, 12 + int(self.byte_id), 4)))
        # self.config["low_rt"] = int(self.get_real(self.client.db_read(self.db_id, 16, 4)))
        # self.config["low_st"] = int(self.get_real(self.client.db_read(self.db_id, 20, 4)))
        self.config["time"] = int(self.get_int(self.client.db_read(int(self.db_id), 36, 4)) / 1000)
        return self.config

    def set_sensor_data(self):
        self.client.db_write(int(self.db_id), 24 + int(self.byte_id), self.set_real(int(self.config['high'])))
        # self.client.db_write(int(self.db_id), 28, self.set_real(int(self.config['high_rt'])))
        # self.client.db_write(int(self.db_id), 32, self.set_real(int(self.config['high_st'])))
        self.client.db_write(int(self.db_id), 12 + int(self.byte_id), self.set_real(int(self.config['low'])))
        # self.client.db_write(int(self.db_id), 16, self.set_real(int(self.config['low_rt'])))
        # self.client.db_write(int(self.db_id), 20, self.set_real(int(self.config['low_st'])))
        self.client.db_write(int(self.db_id), 36, self.set_dword(int(self.config['time']) * 1000))
        return self.config