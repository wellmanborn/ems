from asgiref.sync import async_to_sync
from celery import shared_task
import logging

from jdatetime import datetime as jdatetime
from django.utils import timezone
from datetime import timedelta

from app.classes.DataLog import digital_sensor_log
from ems.settings import SENSOR_NUMERIC

from app.models import SensorDataLog as SensorDataLogModel, AnalogSensorDataLog as AnalogSensorDataLogModel
from app.classes.Sensor import Sensor
from app.models import Sensor as SensorModel
from channels.layers import get_channel_layer

logger = logging.getLogger('django')
channel_layer = get_channel_layer()
sensors = SensorModel.objects.all()
digital_sensors = SensorModel.objects.filter(type__in=SENSOR_NUMERIC)


@shared_task
def read_from_plc():
    response = {"data": {}, "message": ""}
    time = "-"
    reset_airconditioner = 0
    allow_to_snooze = False
    try:
        response["data"] = Sensor().get_all_sensors_data(sensors)["data"]
        # reset_airconditioner = Sensor().get_reset_airconditioner()
        # allow_to_snooze = 1 if Sensor().get_allow_to_snooze() else 0
        response["data"].append({"time": str(jdatetime.now().replace(microsecond=0))})
        response["reset_airconditioner"] = reset_airconditioner
        response["allow_to_snooze"] = allow_to_snooze
        response["time"] = str(jdatetime.now().replace(microsecond=0))
    except Exception as e:
        response["message"] = e.__str__()
    async_to_sync(channel_layer.group_send)('snap7', {'type': 'send_data', 'response': response})


@shared_task
def read_from_plc_and_insert_to_database():
    data = {}
    try:
        data = Sensor().get_all_sensors_data(digital_sensors)["data"]
    except Exception as e:
        logger.error(e.__str__())

    is_air_conditioner_inserted = False
    for dt in data:
        if 'sensor' in dt:
            try:
                if dt["sensor"] == "airconditioner":
                    if not is_air_conditioner_inserted:
                        digital_sensor_log("average temperature", "temperature", dt["sensor_id"], dt["db_id"],
                                           dt["byte_id"], dt["bit_id"], dt["avg_tmp"], dt["alarm"])
                        is_air_conditioner_inserted = True
                else:
                    digital_sensor_log(dt["sensor_title"], dt["sensor"], dt["sensor_id"], dt["db_id"],
                                           dt["byte_id"],dt["bit_id"],dt["value"], dt["alarm"])
            except Exception as e:
                logger.error(e.__str__())
    return None

@shared_task
def remove_old_data_log_from_database():
    try:
        data = SensorDataLogModel().objects.\
            filter(created_at__lte=timezone.now() - timedelta(days=14)).order_by('created_at')
        data.delete()
        data = AnalogSensorDataLogModel().objects. \
            filter(created_at__lte=timezone.now() - timedelta(days=30)).order_by('created_at')
        data.delete()
    except Exception as e:
        logger.error(e.__str__())