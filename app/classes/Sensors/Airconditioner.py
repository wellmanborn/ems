from app.classes.ConvertData import ConvertData
from app.classes.Device import Device
from app.classes.SensorInterface import SensorInterface


class Airconditioner(SensorInterface, ConvertData):

    sensor_type = "airconditioner"
    config = {}

    def get_sensor_data(self):
        data = self.client.db_read(int(self.db_id), int(self.byte_id), 1)
        self.value = self.get_bool(data, 0, int(self.bit_id))
        self.alarm = False

        average_data = {}
        average_data["avg_tmp"] = self.get_real(self.client.db_read(int(self.db_id), 2, 4))
        average_data["avg_hum"] = self.get_real(self.client.db_read(int(self.db_id), 6, 4))

        return self.send_response_data(average_data)

    def get_airconditioner_config(self, db=64):
        Device().set_status("reading")
        try:
            config = {}
            config["set_point_on"] = int(self.get_real(self.client.db_read(db, 10, 4)))
            config["set_point_off"] = int(self.get_real(self.client.db_read(db, 14, 4)))
            config["set_point_humidity"] = int(self.get_real(self.client.db_read(db, 18, 4)))

            config["start_first_hour"] = int(self.get_int(self.client.db_read(db, 22, 1)))
            config["start_second_hour"] = int(self.get_int(self.client.db_read(db, 23, 1)))
            config["start_third_hour"] = int(self.get_int(self.client.db_read(db, 24, 1)))

            config["time_for_over_range"] = int(self.get_int(self.client.db_read(db, 26, 4)) / 60000)

            data = self.client.db_read(db, 40, 1)
            config["control_method"] = self.get_bool(data, 0, 0)

            data = self.client.db_read(db, 98, 1)
            config["manual_air1_on"] = self.get_bool(data, 0, 3)
            config["manual_air2_on"] = self.get_bool(data, 0, 4)
            config["manual_air3_on"] = self.get_bool(data, 0, 5)
            config["manual_air4_on"] = self.get_bool(data, 0, 6)
            Device().set_status("")
            return config
        except Exception as e:
            Device().set_status("")
            raise e

    def set_airconditioner_config(self, config, db=64):
        Device().set_status("writing")
        try:
            client = Device().get_client()
            client.db_write(int(db), 10, self.set_real(int(config['set_point_on'])))
            client.db_write(int(db), 14, self.set_real(int(config['set_point_off'])))
            client.db_write(int(db), 18, self.set_real(int(config['set_point_humidity'])))
            client.db_write(int(db), 22, self.set_int(int(config['start_first_hour'])))
            client.db_write(int(db), 23, self.set_int(int(config['start_second_hour'])))
            client.db_write(int(db), 24, self.set_int(int(config['start_third_hour'])))
            client.db_write(int(db), 26, self.set_dword(int(config['time_for_over_range']) * 60000))

            self.bool_write_to(client, int(db), 40, 0, config['control_method'])
            Device().set_status("")
        except Exception as e:
            Device().set_status("")
            raise e

    def set_airconditioner_status(self, db, bit_id, status):
        Device().set_status("writing")
        try:
            client = Device().get_client()
            self.bool_write_to(client, int(db), 98, bit_id + 3, status)
            Device().set_status("")
        except Exception as e:
            Device().set_status("")
            raise e