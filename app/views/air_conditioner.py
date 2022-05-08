import time

from django.contrib.auth.decorators import login_required

from app.classes.Sensors.AirConditionerFactory import AirConditionerFactory
from app.classes.models.sensor import store_air_conditioner_sensor
from app.classes.models.setting import store_air_conditioner_config
from app.forms.sensors.air_conditioner import AirConditionerForm, AirConditionerSettingForm, AirConditionerEditForm, \
    AirConditionerSettingTempOnlyForm
from app.models import Sensor as SensorModel, Setting
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from app.classes.Sensor import Sensor
# from ems.settings import AIRCONDITIONER_REVERSES




def delete(db_id):
    sensors = SensorModel.objects.filter(type="airconditioner", db_id=db_id)
    for sensor in sensors:
        sensor.delete()
    airconditioner_setting_filter = Setting.objects.filter(key="air_conditioner")
    airconditioner_setting = airconditioner_setting_filter[0]

    if "config" in airconditioner_setting.config:
        config = airconditioner_setting.config["config"]
        setting = airconditioner_setting.config["setting"]
        if int(setting["count"]) == 1:
            airconditioner_setting_filter.delete()
        else:
            setting["count"] = setting["count"] - 1
            config_data = {}
            for key in config:
                if int(key) != int(db_id):
                    config_data[key] = config[key]
            airconditioner_setting.config["config"] = config_data
            airconditioner_setting.save()
    else:
        airconditioner_setting_filter.delete()
    return redirect("/")


@login_required
def create(request):
    if request.method != 'POST':
        form = AirConditionerForm()
    else:
        form = store(request)
    return render(request, 'sensors/air_conditioner.html', {'form': form})

@login_required
def setting(request, id):
    airconditioner = get_object_or_404(SensorModel, pk=id, type="airconditioner")
    airconditioner_setting = get_object_or_404(Setting, key="air_conditioner")
    if "config" in airconditioner_setting.config:
        config = airconditioner_setting.config["config"][str(airconditioner.db_id)]
    else:
        config = airconditioner_setting.config
    if airconditioner_setting.config["setting"]["type"] == "temponly":
        template = 'settings/air_conditioner_temp_only.html'
    else:
        template = 'settings/air_conditioner_full.html'

    if request.method == 'POST':
        if airconditioner_setting.config["setting"]["type"] == "temponly":
            form = AirConditionerSettingTempOnlyForm(request.POST)
        else:
            form = AirConditionerSettingForm(request.POST)
        if form.is_valid():
            if airconditioner_setting.config["setting"]["type"] == "temponly":
                config = set_data_on_config_for_air_conditioner_temp_only(config, request)
            else:
                config = set_data_on_config_for_air_conditioner_full(config, request)
            airconditioner_setting.save()
            AirConditionerFactory()\
                .get_air_conditioner(airconditioner_setting.config["setting"]["type"])\
                .set_data(None, config, airconditioner.db_id)
            messages.success(request, 'با موفقیت ویرایش شد')
        else:
            messages.error(request, 'حطایی رخ داد، لطفا مجددا تلاش نمایید')
    else:
        if airconditioner_setting.config["setting"]["type"] == "temponly":
            form = get_air_conditioner_temp_only_with_initialed_data(config)
        else:
            form = get_air_conditioner_full_with_initialed_data(config)

    return render(request, template, {'form': form,
                                    'title': airconditioner.title,
                                    'db_id': airconditioner.db_id,
                                    'id': airconditioner.id})


def get_air_conditioner_full_with_initialed_data(config):
    form = AirConditionerSettingForm()
    form.initial["set_point_on"] = config["set_point_on"]
    form.initial["set_point_off"] = config["set_point_off"]
    form.initial["control_method"] = 1 if config["control_method"] else 0
    form.initial["start_first_hour"] = config["start_first_hour"]
    form.initial["start_third_hour"] = config["start_third_hour"]
    form.initial["start_second_hour"] = config["start_second_hour"]
    form.initial["set_point_humidity"] = config["set_point_humidity"]
    form.initial["time_for_over_range"] = config["time_for_over_range"]
    return form

def get_air_conditioner_temp_only_with_initialed_data(config):
    form = AirConditionerSettingTempOnlyForm()
    form.initial["set_point_on"] = config["set_point_on"]
    form.initial["set_point_off"] = config["set_point_off"]
    form.initial["control_method"] = 1 if config["control_method"] else 0
    form.initial["alarm_time"] = config["alarm_time"]
    form.initial["warning_time"] = config["warning_time"]
    return form

def set_data_on_config_for_air_conditioner_full(config, request):
    config["set_point_on"] = int(request.POST['set_point_on'])
    config["set_point_off"] = int(request.POST['set_point_off'])
    config["control_method"] = True if int(request.POST['control_method']) == 1 else False
    config["start_first_hour"] = int(request.POST['start_first_hour'])
    config["start_second_hour"] = int(request.POST['start_second_hour'])
    config["start_third_hour"] = int(request.POST['start_third_hour'])
    config["set_point_humidity"] = int(request.POST['set_point_humidity'])
    config["time_for_over_range"] = int(request.POST['time_for_over_range'])
    config["manual_air1_on"] = config["manual_air1_on"]
    config["manual_air2_on"] = config["manual_air2_on"]
    config["manual_air3_on"] = config["manual_air3_on"]
    config["manual_air4_on"] = config["manual_air4_on"]
    return config

def set_data_on_config_for_air_conditioner_temp_only(config, request):
    config["set_point_on"] = float(request.POST['set_point_on'])
    config["set_point_off"] = float(request.POST['set_point_off'])
    config["control_method"] = True if int(request.POST['control_method']) == 1 else False
    config["alarm_time"] = int(request.POST['alarm_time'])
    config["warning_time"] = int(request.POST['warning_time'])
    config["manual_air1_on"] = config["manual_air1_on"]
    config["manual_air2_on"] = config["manual_air2_on"]
    config["manual_air3_on"] = config["manual_air3_on"]
    config["manual_air4_on"] = config["manual_air4_on"]
    return config


@login_required
def edit(request, id):
    airconditioner = get_object_or_404(SensorModel, pk=id, type="airconditioner")
    airconditioner_setting = get_object_or_404(Setting, key="air_conditioner")

    if "config" in airconditioner_setting.config:
        manual = airconditioner_setting.config["config"][str(airconditioner.db_id)]["control_method"]
    else:
        manual = airconditioner_setting.config["control_method"]
    if request.method == 'POST':
        form = AirConditionerEditForm(request.POST)
        if form.is_valid():
            airconditioner.title = request.POST["title"]
            airconditioner.save()

            if 'status' in request.POST:
                if AIRCONDITIONER_REVERSE:
                    status = 0 if int(request.POST["status"]) == 1 else 1
                else:
                    status = 1 if int(request.POST["status"]) == 1 else 0
                AirConditionerFactory.get_air_conditioner(airconditioner_setting.config["setting"]["type"]).\
                    set_airconditioner_status(airconditioner.db_id, airconditioner.bit_id, status)
                airconditioner_setting.save()

            messages.success(request, 'با موفقیت ویرایش شد')
        else:
            messages.error(request, 'حطایی رخ داد، لطفا مجددا تلاش نمایید')
    else:
        form = AirConditionerEditForm()
        form.initial["title"] = airconditioner.title
        data = Sensor().get_sensor_data(airconditioner, {"type": airconditioner_setting.config["setting"]["type"]})
        form.initial["status"] = 0 if data["value"] else 1

    return render(request, 'sensors/air_conditioner_edit.html', {
        'form': form,
        "manual": manual,
        "airconditioner": airconditioner})

@login_required
def reset(request):
    if request.method == 'POST':
        try:
            AirConditionerFactory.get_air_conditioner("full").reset_airconditioner(True)
            time.sleep(1.5)
            AirConditionerFactory.get_air_conditioner("full").reset_airconditioner(False)
            return JsonResponse({'success': True, 'message': 'با موفقیت ریست شدند'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': 'حطایی رخ داد، لطفا مجددا تلاش نمایید'})
    pass

@login_required
def store(request):
    form = AirConditionerForm(request.POST)
    if form.is_valid():
        try:

            air_conditioner_service = AirConditionerFactory.get_air_conditioner(request.POST['air_conditioner_type'])
            config = air_conditioner_service.get_config(int(request.POST['db_id']))

            store_air_conditioner_config(int(request.POST['db_id']), request.POST['air_conditioner_type'], config)
            store_air_conditioner_sensor(request.POST['title'], int(request.POST['db_id']),
                                         int(request.POST['byte_id']), int(request.POST['air_conditioner_count']))

            messages.success(request, 'با موفقیت افزوده شد')
        except Exception as e:
            messages.error(request, e.__str__())
    else:
        messages.error(request, 'حطایی رخ داد، لطفا مجددا تلاش نمایید')
    return form
