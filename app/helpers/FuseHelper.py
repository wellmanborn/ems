
class FuseHelper():

    def get_config_from_request(self, request):
        config = {}
        return config

    def set_data_to_form(self, form, sensor):
        form.initial["db_id"] = sensor.db_id
        form.initial["start_value"] = sensor.start_value
        form.initial["title"] = sensor.title
        return form