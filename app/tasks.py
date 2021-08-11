from asgiref.sync import async_to_sync
from celery import shared_task
import logging

from jdatetime import datetime

from app.classes.Notification import send_notification
from app.models import AlarmLog as AlarmLogModel, SensorDataLog as SensorDataLogModel, Notification as NotificationModel
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
            log = SensorDataLogModel(sensor_id=dt["sensor_id"], sensor_title=dt["sensor_title"], sensor_type=dt["sensor"],
                                db_id=dt["db_id"], byte_id=dt["byte_id"], bit_id=dt["bit_id"],
                                value=dt["value"], alarm=int(dt["alarm"]))
            log.save()
    return None


@shared_task
def log_alarm(sensor_title, sensor_type, sensor_id, db_id, byte_id, bit_id, alarm):
    if int(alarm) >= 3:
        sensor = AlarmLogModel.objects.get_or_create(db_id=int(db_id), sensor_id=int(sensor_id), byte_id=int(byte_id),
                                                     bit_id=int(bit_id), sensor_type=sensor_type)[0]
        if str(sensor.alarm) != str(alarm):
            sensor.alarm = str(alarm)
            sensor.save()
            message = "سنسور " + sensor_title + " خطایی دارد "
            send_notification("error", message)
    else:
        sensor = AlarmLogModel.objects.filter(db_id=int(db_id), sensor_id=int(sensor_id), byte_id=int(byte_id),
                                              bit_id=int(bit_id), sensor_type=sensor_type)
        if sensor:
            sensor[0].delete()
            message = "سنسور " + sensor_title + " به حالت نرمال رسید "
            send_notification("success", message)
    return None
