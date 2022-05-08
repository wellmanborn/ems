from app.classes.SensorFactory import SensorFactory
import logging
logger = logging.getLogger('django')


class Sensor():

    def get_all_sensors_data(self, sensors, additional_data = None):
        response = []
        message = ""
        for SensorData in sensors:
            try:
                data = self.get_sensor_data(SensorData, additional_data)
                response.append(data)
            except Exception as e:
                logger.critical(e.__str__() + " db_id: " + str(SensorData.db_id))
        return {"data": response, "message": message}

    def get_sensor_data(self, SensorData, additional_data=None):
        sensor = SensorFactory.get_sensor(SensorData.type, additional_data)
        return sensor.get_data(SensorData)

    def get_sensor_config(self, SensorData):
        sensor = SensorFactory.get_sensor(SensorData.type)
        return sensor.get_config(SensorData.db_id, SensorData)

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