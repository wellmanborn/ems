from app.classes.SensorABC import SensorABC


class Alarm(SensorABC):

    sensor_type = "alarm"

    def get_sensor_data(self):
        return self.config

    def allow_to_snooze(self):
        try:
            data = self.client.db_read(70, 0, 1)
            value = self.get_bool(data, 0, 1)
        except Exception as e:
            raise Exception(e)
        return value

    def stop_snooze(self):
        try:
            self.bool_write_to(self.client, 70, 0, 0, True)
        except Exception as e:
            raise Exception(e)
        return True

    def get_sensor_config(self):
        self.config["snooze_time"] = int(self.get_int(self.client.db_read(69, 12, 4)) / 60000)
        self.config["time_for_siren_off_day"] = int(self.get_int(self.client.db_read(69, 20, 4)) / 60000)
        self.config["time_for_siren_off_night"] = int(self.get_int(self.client.db_read(69, 28, 4)) / 60000)
        self.config["time_for_repeat_send_sms"] = int(self.get_int(self.client.db_read(69, 36, 4)) / 60000)
        self.config["time_for_siren_on_day"] = int(self.get_int(self.client.db_read(69, 16, 4)) / 1000)
        self.config["time_for_siren_on_night"] = int(self.get_int(self.client.db_read(69, 24, 4)) / 1000)
        self.config["start_work_time"] = int(self.get_int(self.client.db_read(69, 32, 1)))
        self.config["end_work_time"] = int(self.get_int(self.client.db_read(69, 33, 1)))
        self.config["total_sms"] = int(self.get_int(self.client.db_read(69, 34, 2)))
        return self.config

    def set_sensor_data(self):
        self.client.db_write(69, 12, self.set_dword(int(self.config['snooze_time']) * 60000))
        self.client.db_write(69, 20, self.set_dword(int(self.config['time_for_siren_off_day']) * 60000))
        self.client.db_write(69, 28, self.set_dword(int(self.config['time_for_siren_off_night']) * 60000))
        self.client.db_write(69, 36, self.set_dword(int(self.config['time_for_repeat_send_sms']) * 60000))
        self.client.db_write(69, 16, self.set_dword(int(self.config['time_for_siren_on_day']) * 1000))
        self.client.db_write(69, 24, self.set_dword(int(self.config['time_for_siren_on_night']) * 1000))
        self.client.db_write(69, 32, self.set_int(int(self.config['start_work_time'])))
        self.client.db_write(69, 33, self.set_int(int(self.config['end_work_time'])))
        self.client.db_write(69, 34, self.set_word(int(self.config['total_sms'])))
        return self.config

    # def get_alarm(self):
    #     try:
    #         alarm = int(self.get_int(self.client.db_read(60, 4, 2)))
    #     except Exception as e:
    #         raise Exception(e)
    #     return alarm

    def get_reset_airconditioner(self):
        try:
            data = self.client.db_read(64, 104, 1)
            value = self.get_bool(data, 0, 1)
        except Exception as e:
            raise Exception(e)
        return value