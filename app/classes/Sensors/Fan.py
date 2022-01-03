from app.classes.SensorABC import SensorABC


class Fan(SensorABC):

    sensor_type = "fan"

    def get_sensor_data(self):
        data = self.client.db_read(int(self.db_id), self.byte_id, 1)
        self.value = self.get_bool(data, 0, self.bit_id)
        self.alarm = False
        return self.send_response_data()

    def get_sensor_config(self):
        data = self.client.db_read(int(self.db_id), int(self.setting["fan_control_byte_id"]), 1)
        self.config["status"] = self.get_bool(data,
                                              0,
                                              int(self.setting["fan_control_bit_id"]))
        return self.config

    def set_sensor_data(self):
        self.bool_write_to(self.client,
                           int(self.db_id),
                           int(self.setting["fan_control_byte_id"]),
                           int(self.setting["fan_control_bit_id"]),
                           self.config["status"])
        return self.config
