
class PowerthreeHelper():

    def get_config_from_request(self, request):
        config = {}
        config["high"] = int(request.POST['high'])
        config["low"] = int(request.POST['low'])
        # config["high_rs"] = int(request.POST['high_rs'])
        # config["high_rt"] = int(request.POST['high_rt'])
        # config["high_st"] = int(request.POST['high_st'])
        # config["low_rs"] = int(request.POST['low_rs'])
        # config["low_rt"] = int(request.POST['low_rt'])
        # config["low_st"] = int(request.POST['low_st'])
        config["time"] = int(request.POST['time'])
        return config

    def set_data_to_form(self, form, sensor):
        form.initial["db_id"] = sensor.db_id
        form.initial["title"] = sensor.title
        form.initial["high"] = sensor.config['high']
        form.initial["low"] = sensor.config['low']
        # form.initial["high_rs"] = sensor.config['high_rs']
        # form.initial["high_rt"] = sensor.config['high_rt']
        # form.initial["high_st"] = sensor.config['high_st']
        # form.initial["low_rs"] = sensor.config['low_rs']
        # form.initial["low_rt"] = sensor.config['low_rt']
        # form.initial["low_st"] = sensor.config['low_st']
        form.initial["time"] = sensor.config['time']
        return form