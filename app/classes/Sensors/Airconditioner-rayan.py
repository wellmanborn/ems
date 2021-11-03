from app.classes.Device import Device
from app.classes.SensorABC import SensorABC


class Airconditioner(SensorABC):

    sensor_type = "airconditioner"
    config = {}

    def get_sensor_data(self):
        data = self.client.db_read(int(self.db_id), int(self.byte_id), 1)
        self.value = self.get_bool(data, 0, int(self.bit_id))
        self.alarm = False

        average_data = {}
        average_data["avg_tmp"] = self.get_real(self.client.db_read(int(self.db_id), 0, 4))

        return self.send_response_data(average_data)

    def get_sensor_config(self):
        self.config["set_point_on"] = float(self.get_real(self.client.db_read(self.db_id, 4, 4)))
        self.config["set_point_off"] = float(self.get_real(self.client.db_read(self.db_id, 8, 4)))

        self.config["alarm_time"] = int(self.get_int(self.client.db_read(self.db_id, 12, 4)) / 60000)
        self.config["warning_time"] = int(self.get_int(self.client.db_read(self.db_id, 16, 4)) / 60000)

        data = self.client.db_read(self.db_id, 24, 1)
        self.config["control_method"] = self.get_bool(data, 0, 0)

        data = self.client.db_read(self.db_id, 54, 1)
        self.config["manual_air1_on"] = self.get_bool(data, 0, 2)
        self.config["manual_air2_on"] = self.get_bool(data, 0, 3)
        self.config["manual_air3_on"] = self.get_bool(data, 0, 4)
        self.config["manual_air4_on"] = self.get_bool(data, 0, 5)
        return self.config


    def set_sensor_data(self):
        self.client.db_write(int(self.db_id), 4, self.set_real(float(self.config['set_point_on'])))
        self.client.db_write(int(self.db_id), 8, self.set_real(float(self.config['set_point_off'])))

        self.client.db_write(int(self.db_id), 12, self.set_dword(int(self.config['alarm_time']) * 60000))
        self.client.db_write(int(self.db_id), 16, self.set_dword(int(self.config['warning_time']) * 60000))

        self.bool_write_to(self.client, int(self.db_id), 24, 0, self.config['control_method'])
        return self.config

    def set_airconditioner_status(self, db, bit_id, status):
        try:
            self.device.set_status("writing")
            self.bool_write_to(self.client, int(db), 54, bit_id + 2, status)
            self.device.set_status("")
        except Exception as e:
            self.device.set_status("")
            raise e

    def reset_airconditioner(self, status = True):
        try:
            self.bool_write_to(self.client, 64, 0, 2, status)
        except Exception as e:
            raise e
