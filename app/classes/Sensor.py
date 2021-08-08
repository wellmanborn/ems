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
                logger.critical(str(e))
                raise Exception("Error reading data from device \n Check device connection \n " + SensorData.type +
                                str(SensorData.db_id) + e.__str__())
        return {"data": response, "message": message}

    def get_sensor_data(self, SensorData):
        sensor = SensorFactory.get_sensor(SensorData.type)
        return sensor.get_data(SensorData)
