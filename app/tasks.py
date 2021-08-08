from asgiref.sync import async_to_sync
from celery import shared_task
import logging

from jdatetime import datetime

from app.models import LogAlarm as LogAlarmModel, LogSensorData
from app.classes.Sensor import Sensor
from app.models import Sensor as SensorModel
from channels.layers import get_channel_layer

logger = logging.getLogger('django')
channel_layer = get_channel_layer()
sensors = SensorModel.objects.all()


@shared_task
def read_from_plc():
    response = {"data": {}, "message": ""}
    try:
        response["data"] = Sensor().get_all_sensors_data(sensors)["data"]
        response["data"].append({"time": str(datetime.now().replace(microsecond=0))})
    except Exception as e:
        response["message"] = str(e)
    async_to_sync(channel_layer.group_send)('snap7', {'type': 'send_data', 'response': response})


@shared_task
def read_from_plc_and_insert_to_database():
    data = {}
    try:
        data = Sensor().get_all_sensors_data(sensors)["data"]
    except Exception as e:
        logger.error(str(e))

    for dt in data:
        if 'sensor' in dt:
            log = LogSensorData(sensor_id=dt["sensor_id"], sensor_title=dt["sensor_title"], sensor_type=dt["sensor"],
                                db_id=dt["db_id"], byte_id=dt["byte_id"], bit_id=dt["bit_id"],
                                value=dt["value"], alarm=int(dt["alarm"]))
            log.save()
    return None


@shared_task
def log_alarm(sensor_type, sensor_id, db_id, byte_id, bit_id, alarm):
    if alarm == False or alarm == 0:
        sensor = LogAlarmModel.objects.filter(db_id=db_id, sensor_id=sensor_id, byte_id=byte_id,
                                              bit_id=bit_id, sensor_type=sensor_type)
        if sensor:
            sensor.delete()
            # @todo send notification
    else:
        sensor = LogAlarmModel.objects.get_or_create(db_id=db_id, sensor_id=sensor_id, byte_id=byte_id,
                                                     bit_id=bit_id, sensor_type=sensor_type)[0]
        if sensor.alarm != str(alarm):
            sensor.alarm = str(alarm)
            sensor.save()
            # @todo send notification
    return None
