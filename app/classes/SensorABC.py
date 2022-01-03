import logging

from app.classes.DataLog import analog_sensor_log

logger = logging.getLogger('django')
from app.classes.Device import Device
from app.classes.ConvertData import ConvertData
from abc import ABC, abstractmethod
from app.classes.AlarmLog import alarm_log


class SensorABC(ABC, ConvertData):

    sensor_id = None
    sensor_title = None
    sensor_type = None
    value = None
    alarm = False
    db_id = 0
    byte_id = 0
    bit_id = 0
    client = None
    device = None
    config = {}
    setting = {}

    def __init__(self):
        try:
            self.device = Device()
            self.client = self.device.get_client()
            if self.client == False or self.client.get_connected() != True or \
                    self.client.get_cpu_state() != "S7CpuStatusRun":
                self.client = self.device.refresh_client()
        except Exception as e:
            logger.error(e.__str__())
            logger.error("device connection error")
            raise Exception(e)

    def get_data(self, SensorDetail):
        try:
            self.device.set_status("reading")
            self.db_id = SensorDetail.db_id
            self.byte_id = SensorDetail.byte_id
            self.bit_id = SensorDetail.bit_id
            self.sensor_title = SensorDetail.title
            self.sensor_id = SensorDetail.id
            self.setting = SensorDetail.setting
            response = self.get_sensor_data()
            alarm_log(self.sensor_title, self.sensor_type, SensorDetail.id, self.db_id, self.byte_id,
                      self.bit_id, self.alarm)
            analog_sensor_log(self.sensor_type, SensorDetail.id, self.db_id, self.byte_id,
                              self.bit_id, self.alarm)
            self.device.set_status("")
            return response
        except Exception as e:
            logger.error(e.__str__())
            logger.error("error ---> " + str(SensorDetail.db_id))
            raise Exception(e)

    @abstractmethod
    def get_sensor_data(self):
        """ must be implemented in child classes """

    def send_response_data(self, additional_data = None):
        data = {"sensor_title": self.sensor_title, "sensor_id": self.sensor_id,
                "sensor": self.sensor_type, "db_id": str(self.db_id),
                "byte_id": self.byte_id, "bit_id": self.bit_id,
                "value": self.value, "alarm": self.alarm}
        if additional_data != None:
            for dt, val in additional_data.items():
                data[dt] = val
        return data

    def set_data(self, SensorDetail, config, db_id = None):
        try:
            self.device.set_status("writing")
            if SensorDetail != None:
                self.db_id = SensorDetail.db_id
                self.byte_id = SensorDetail.byte_id
                self.bit_id = SensorDetail.bit_id
                self.setting = SensorDetail.setting
            else:
                self.db_id = db_id
            self.config = config
            self.set_sensor_data()
            self.device.set_status("")
            return True
        except Exception as e:
            logger.error(e.__str__())
            raise Exception(e)

    @abstractmethod
    def set_sensor_data(self):
        """ must be implemented in child classes"""

    def get_config(self, db_id, SensorDetail = None):
        try:
            self.device.set_status("reading")
            self.db_id = db_id
            if SensorDetail != None:
                self.byte_id = SensorDetail.byte_id
                self.bit_id = SensorDetail.bit_id
                self.config = SensorDetail.config
                self.setting = SensorDetail.setting
            config = self.get_sensor_config()
            self.device.set_status("")
            return config
        except Exception as e:
            logger.error(e.__str__())
            logger.error("sensor db id: " + str(db_id))
            raise Exception(e)

    @abstractmethod
    def get_sensor_config(self):
        """ must be implemented in child classes"""