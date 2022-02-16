from app.models import Sensor as SensorModel


def store_air_conditioner_sensor(title, db_id, byte_id, air_conditioner_count):
    SensorModel.objects.filter(type="airconditioner", db_id=db_id).delete()

    for bit in range(0, air_conditioner_count):
        sensor = SensorModel(title=title + " " + str(bit + 1), db_id=db_id, byte_id=byte_id, bit_id=bit,
                             config={}, type="airconditioner")
        sensor.save()