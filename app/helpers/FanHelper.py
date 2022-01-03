from app.classes.Sensor import Sensor


class FanHelper():

    def get_config_from_request(self, request):
        config = {}
        config["status"] = False if int(request.POST['status']) == 0 else True
        return config

    def set_data_to_form(self, form, sensor):
        form.initial["db_id"] = sensor.db_id
        form.initial["title"] = sensor.title
        config = Sensor().get_sensor_config(sensor)
        form.initial["status"] = 0 if config["status"] == False else 1
        return form