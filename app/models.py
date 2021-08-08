from django.contrib.auth.models import User
from django.db import models

SENSOR_TYPE = (
    ('temperature', 'دما'),
    ('humidity', 'رطوبت'),
    ('current', 'جریان'),
    ('power', 'ولتاژ تک فاز'),
    ('power3', 'ولتاژ سه فاز'),
    ('door', 'سنسور درب'),
    ('waterleakage', 'نشتی آب'),
    ('smoke', 'سنسور دود'),
    ('digitalpower', 'سنسور کنترل برق'),
    ('fuse', 'سنسور فیوز'),
    ('light', 'سنسور نور'),
    ('aircondition', 'سنسور نور')
)


# Create your models here.
class Sensor(models.Model):
    title = models.CharField(max_length=255, blank=False)
    type = models.CharField(blank=False, max_length=255, choices=SENSOR_TYPE)
    db_id = models.IntegerField(blank=False)
    byte_id = models.IntegerField(blank=True, default=0)
    bit_id = models.IntegerField(blank=True, default=0)
    start_value = models.IntegerField(blank=True, default=0)
    config = models.JSONField(blank=True, default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']


class Setting(models.Model):
    key = models.CharField(max_length=255, blank=False)
    value = models.CharField(max_length=255, blank=False)
    config = models.JSONField(default=dict)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']


class LogAlarm(models.Model):
    sensor_id = models.IntegerField(blank=False)
    sensor_type = models.CharField(max_length=255, blank=False)
    db_id = models.IntegerField(blank=False)
    byte_id = models.IntegerField(blank=False)
    bit_id = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    alarm = models.CharField(max_length=255, blank=False)
    alarm_count = models.BigIntegerField(blank=False, default=1)


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    job_title = models.CharField(max_length=300, blank=False)
    mobile = models.CharField(db_index=True, max_length=20, blank=False)


class LogSensorData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    sensor_title = models.CharField(blank=False, max_length=255)
    sensor_type = models.CharField(blank=False, max_length=255, choices=SENSOR_TYPE)
    db_id = models.IntegerField(blank=False)
    byte_id = models.IntegerField(blank=True, default=0)
    bit_id = models.IntegerField(blank=True, default=0)
    value = models.IntegerField(blank=False, default=0)
    alarm = models.IntegerField(blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']