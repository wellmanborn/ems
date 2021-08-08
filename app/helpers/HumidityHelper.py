
class HumidityHelper():

    def get_config_from_request(self, request):
        config = {}
        config["very_high"] = int(request.POST['very_high'])
        config["high"] = int(request.POST['high'])
        config["low"] = int(request.POST['low'])
        config["very_low"] = int(request.POST['very_low'])
        config["offset"] = int(request.POST['offset'])
        return config

    def set_data_to_form(self, form, sensor):
        form.initial["db_id"] = sensor.db_id
        form.initial["title"] = sensor.title
        form.initial["very_high"] = sensor.config['very_high']
        form.initial["high"] = sensor.config['high']
        form.initial["low"] = sensor.config['low']
        form.initial["very_low"] = sensor.config['very_low']
        form.initial["offset"] = sensor.config['offset']
        return form