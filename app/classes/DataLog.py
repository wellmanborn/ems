from django.utils import timezone
from app.models import AnalogSensorDataLog
from ems.settings import SENSOR_NUMERIC
from app.models import SensorDataLog as SensorDataLogModel


def digital_sensor_log(sensor_title, sensor_type, sensor_id, db_id, byte_id, bit_id, value, alarm):
    log = SensorDataLogModel(sensor_id=sensor_id, sensor_title=sensor_title,
                                 sensor_type=sensor_type,
                                 db_id=db_id, byte_id=byte_id, bit_id=bit_id,
                                 value=value, alarm=int(alarm))
    log.save()


def analog_sensor_log(sensor_type, sensor_id, db_id, byte_id, bit_id, alarm):
    if alarm == 4 or alarm == 3:
        if alarm == 3:
            alarm = 4
        sensor = AnalogSensorDataLog.objects.get_or_create(db_id=int(db_id),
                                                           sensor_id=int(sensor_id), byte_id=int(byte_id),
                                                           alarm=int(alarm), bit_id=int(bit_id),
                                                           sensor_type=sensor_type,
                                                           finished_at__isnull=True)
    elif alarm == 0:
        try:
            sensor = AnalogSensorDataLog.objects.filter(db_id=int(db_id),
                                                        sensor_id=int(sensor_id),
                                                        byte_id=int(byte_id),
                                                        bit_id=int(bit_id),
                                                        sensor_type=sensor_type,
                                                        finished_at__isnull=True).order_by('-created_at').first()
            if sensor:
                sensor.finished_at = timezone.now()
                sensor.save()
        except AnalogSensorDataLog.DoesNotExist:
            return None
    return None