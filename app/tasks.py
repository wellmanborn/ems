from asgiref.sync import async_to_sync
from celery import shared_task
import logging

from jdatetime import datetime

from app.models import SensorDataLog as SensorDataLogModel
from app.classes.Sensor import Sensor
from app.models import Sensor as SensorModel
from channels.layers import get_channel_layer

logger = logging.getLogger('django')
channel_layer = get_channel_layer()
sensors = SensorModel.objects.all()
from ems.settings import SENSOR_NUMERIC


@shared_task
def read_from_plc():
    response = {"data": {}, "message": ""}
    try:
        response["data"] = Sensor().get_all_sensors_data(sensors)["data"]
        response["data"].append({"time": str(datetime.now().replace(microsecond=0))})
    except Exception as e:
        response["message"] = e.__str__()
    async_to_sync(channel_layer.group_send)('snap7', {'type': 'send_data', 'response': response})


@shared_task
def read_from_plc_and_insert_to_database():
    data = {}
    try:
        data = Sensor().get_all_sensors_data(sensors)["data"]
    except Exception as e:
        logger.error(e.__str__())

    for dt in data:
        if 'sensor' in dt:
            if dt["sensor"] in SENSOR_NUMERIC or int(dt["alarm"]) != 0:
                log = SensorDataLogModel(sensor_id=dt["sensor_id"], sensor_title=dt["sensor_title"], sensor_type=dt["sensor"],
                                    db_id=dt["db_id"], byte_id=dt["byte_id"], bit_id=dt["bit_id"],
                                    value=dt["value"], alarm=int(dt["alarm"]))
                log.save()
    return None