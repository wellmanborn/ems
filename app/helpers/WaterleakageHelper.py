
class WaterleakageHelper():

    def get_config_from_request(self, request):
        config = {}
        config["time"] = int(request.POST['time'])
        return config

    def set_data_to_form(self, form, sensor):
        form.initial["db_id"] = sensor.db_id
        form.initial["title"] = sensor.title
        form.initial["time"] = sensor.config['time']
        form.initial["start_value"] = sensor.start_value
        return form