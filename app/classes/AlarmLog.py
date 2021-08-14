from asyncio import sleep

from asgiref.sync import sync_to_async

from app.classes.Notification import send_notification
from app.models import AlarmLog as AlarmLogModel


def alarm_log(sensor_title, sensor_type, sensor_id, db_id, byte_id, bit_id, alarm):
    if int(alarm) >= 3:
        sensor = AlarmLogModel.objects.get_or_create(db_id=int(db_id), sensor_id=int(sensor_id), byte_id=int(byte_id),
                                                     bit_id=int(bit_id), sensor_type=sensor_type)[0]
        if sensor.alarm == 0:
            message = "سنسور " + sensor_title + " خطایی دارد "
            alert_alarm("error", message)
        if sensor.alarm == 0 or int(sensor.alarm) != int(alarm):
            sensor.alarm = alarm
            sensor.save()
    else:
        sensor = AlarmLogModel.objects.filter(db_id=int(db_id), sensor_id=int(sensor_id), byte_id=int(byte_id),
                                              bit_id=int(bit_id), sensor_type=sensor_type)
        if sensor:
            sensor[0].delete()
            message = "سنسور " + sensor_title + " به حالت نرمال رسید "
            alert_alarm("success", message)
    return None


def alert_alarm(type, message):
    send_notification(type, message)