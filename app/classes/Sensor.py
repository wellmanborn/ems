from app.classes.SensorFactory import SensorFactory
import logging
logger = logging.getLogger('django')


class Sensor():

    def get_all_sensors_data(self, sensors):
        response = []
        message = ""
        for SensorData in sensors:
            try:
                data = self.get_sensor_data(SensorData)
                response.append(data)
            except Exception as e:
                logger.critical(e.__str__() + "db_id:" + SensorData.db_id)
                raise Exception("Error reading data from device \n Check device connection \n " + e.__str__())
        return {"data": response, "message": message}

    def get_sensor_data(self, SensorData):
        sensor = SensorFactory.get_sensor(SensorData.type)
        return sensor.get_data(SensorData)

    def stop_snooze(self):
        try:
            alarm = SensorFactory.get_sensor("alarm")
            alarm.stop_snooze()
        except Exception as e:
            raise Exception(e)
        return True

    def get_reset_airconditioner(self):
        try:
            alarm = SensorFactory.get_sensor("alarm")
            response = alarm.get_reset_airconditioner()
        except Exception as e:
            raise Exception(e)
        return response

    def get_allow_to_snooze(self):
        try:
            alarm = SensorFactory.get_sensor("alarm")
            allow_to_snooze = alarm.allow_to_snooze()
        except Exception as e:
            raise Exception(e)
        return allow_to_snooze