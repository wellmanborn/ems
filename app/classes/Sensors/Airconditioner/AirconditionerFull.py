from app.classes.Sensors.IAirConditioner import IAirConditioner


class AirConditionerFull(IAirConditioner):

    def get_sensor_data(self):
        data = self.client.db_read(int(self.db_id), int(self.byte_id), 1)
        self.value = self.get_bool(data, 0, int(self.bit_id))
        self.alarm = False

        average_data = {}
        average_data["avg_tmp"] = self.get_real(self.client.db_read(int(self.db_id), 2, 4))
        average_data["avg_hum"] = self.get_real(self.client.db_read(int(self.db_id), 6, 4))

        return self.send_response_data(average_data)

    def get_sensor_config(self):
        self.config["set_point_on"] = int(self.get_real(self.client.db_read(self.db_id, 10, 4)))
        self.config["set_point_off"] = int(self.get_real(self.client.db_read(self.db_id, 14, 4)))
        self.config["set_point_humidity"] = int(self.get_real(self.client.db_read(self.db_id, 18, 4)))

        self.config["start_first_hour"] = int(self.get_int(self.client.db_read(self.db_id, 22, 1)))
        self.config["start_second_hour"] = int(self.get_int(self.client.db_read(self.db_id, 23, 1)))
        self.config["start_third_hour"] = int(self.get_int(self.client.db_read(self.db_id, 24, 1)))

        self.config["time_for_over_range"] = int(self.get_int(self.client.db_read(self.db_id, 26, 4)) / 60000)

        data = self.client.db_read(self.db_id, 40, 1)
        self.config["control_method"] = self.get_bool(data, 0, 0)

        data = self.client.db_read(self.db_id, 98, 1)
        self.config["manual_air1_on"] = self.get_bool(data, 0, 3)
        self.config["manual_air2_on"] = self.get_bool(data, 0, 4)
        self.config["manual_air3_on"] = self.get_bool(data, 0, 5)
        self.config["manual_air4_on"] = self.get_bool(data, 0, 6)
        return self.config

    def set_sensor_data(self):
        self.client.db_write(int(self.db_id), 10, self.set_real(int(self.config['set_point_on'])))
        self.client.db_write(int(self.db_id), 14, self.set_real(int(self.config['set_point_off'])))
        self.client.db_write(int(self.db_id), 18, self.set_real(int(self.config['set_point_humidity'])))
        self.client.db_write(int(self.db_id), 22, self.set_int(int(self.config['start_first_hour'])))
        self.client.db_write(int(self.db_id), 23, self.set_int(int(self.config['start_second_hour'])))
        self.client.db_write(int(self.db_id), 24, self.set_int(int(self.config['start_third_hour'])))
        self.client.db_write(int(self.db_id), 26, self.set_dword(int(self.config['time_for_over_range']) * 60000))
        self.bool_write_to(self.client, int(self.db_id), 40, 0, self.config['control_method'])
        return self.config

    def set_airconditioner_status(self, db, bit_id, status):
        try:
            self.device.set_status("writing")
            self.bool_write_to(self.client, int(db), 98, bit_id + 3, status)
            self.device.set_status("")
        except Exception as e:
            self.device.set_status("")
            raise e

    def reset_airconditioner(self, status = True):
        try:
            self.bool_write_to(self.client, 64, 0, 2, status)
        except Exception as e:
            raise e
