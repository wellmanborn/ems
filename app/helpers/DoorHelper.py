
class DoorHelper():

    def get_config_from_request(self, request):
        config = {}
        config["start_hour"] = int(request.POST['start_hour'])
        config["start_min"] = int(request.POST['start_min'])
        config["end_hour"] = int(request.POST['end_hour'])
        config["end_min"] = int(request.POST['end_min'])
        return config

    def set_data_to_form(self, form, sensor):
        form.initial["db_id"] = sensor.db_id
        form.initial["title"] = sensor.title
        form.initial["start_hour"] = sensor.config['start_hour']
        form.initial["start_min"] = sensor.config['start_min']
        form.initial["end_hour"] = sensor.config['end_hour']
        form.initial["end_min"] = sensor.config['end_min']
        form.initial["start_value"] = sensor.start_value
        return form