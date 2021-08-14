
class CurrentHelper():

    def get_config_from_request(self, request):
        config = {}
        config["high"] = int(request.POST['high'])
        config["time"] = int(request.POST['time'])
        return config

    def set_data_to_form(self, form, sensor):
        form.initial["db_id"] = sensor.db_id
        form.initial["title"] = sensor.title
        form.initial["high"] = sensor.config['high']
        form.initial["time"] = sensor.config['time']
        return form