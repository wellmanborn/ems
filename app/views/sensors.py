from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from app.classes.SensorFactory import SensorFactory
from app.classes.SensorFormFactory import SensorFormFactory
from app.classes.SensorHelperFactory import SensorHelperFactory
from app.classes.Sensors.Airconditioner import Airconditioner


from app.forms import AirconditionerForm, AirconditionerSettingForm, SmsForm, EmailForm, AirconditionerEditForm
from app.models import Sensor, Setting


def add_sensor(request, sensor_type):
    if request.method == 'POST':
        form = SensorFormFactory.get_sensor_form(sensor_type, request.POST)
        if form.is_valid():
            try:
                db_id = int(request.POST['db_id'])
                byte_id = int(request.POST['byte_id'] if "byte_id" in request.POST else 0)
                bit_id = int(request.POST['bit_id'] if "bit_id" in request.POST else 0)
                start_value = request.POST['start_value'] if "start_value" in request.POST else 0
                sensor_class = SensorFactory().get_sensor(sensor_type)
                config = sensor_class.get_config(db_id)
                sensor = Sensor.objects.get_or_create(db_id=db_id, byte_id=byte_id, bit_id=bit_id, type=sensor_type)
                sensor[0].title = request.POST['title']
                sensor[0].start_value = start_value
                sensor[0].byte_id = byte_id
                sensor[0].bit_id = bit_id
                sensor[0].config = config
                sensor[0].save()
                messages.success(request, 'با موفقیت افزوده شد')
            except Exception as e:
                messages.error(request, e.__str__())
        else:
            messages.error(request, 'حطایی رخ داد، لطفا مجددا تلاش نمایید')
    else:
        form = SensorFormFactory.get_sensor_form(sensor_type)
    return render(request, sensor_type + '.html', {'form': form})

@login_required
def edit_sensor(request, id):
    sensor = get_object_or_404(Sensor, pk=id)
    sensor_class = SensorFactory.get_sensor(sensor.type)
    sensor_helper_class = SensorHelperFactory.get_sensor_helper(sensor.type)
    if request.method == 'POST':
        form = SensorFormFactory.get_sensor_form(sensor.type, request.POST)
        if form.is_valid():
            try:
                config = sensor_helper_class.get_config_from_request(request)
                sensor_class.set_data(sensor, config)
                sensor.title = request.POST['title']
                sensor.byte_id = int(request.POST['byte_id'] if "byte_id" in request.POST else 0)
                sensor.bit_id = int(request.POST['bit_id'] if "bit_id" in request.POST else 0)
                sensor.start_value = int(request.POST['start_value'] if "start_value" in request.POST else 0)
                sensor.config = config
                sensor.save()
                messages.success(request, 'با موفقیت ویرایش شد')
            except Exception as e:
                messages.error(request, str(request.POST['db_id']) + e.__str__())
        else:
            messages.error(request, 'حطایی رخ داد، لطفا مجددا تلاش نمایید')
    else:
        form = SensorFormFactory.get_sensor_form(sensor.type)
        form = sensor_helper_class.set_data_to_form(form, sensor)
    return render(request, sensor.type + '.html', {'form': form, "edit": True, "id": id})


@login_required
def add_airconditioner(request):
    if request.method == 'POST':
        form = AirconditionerForm(request.POST)
        if form.is_valid():
            db_id = int(request.POST['db_id']) if 'db_id' in request.POST else 64
            byte_id = int(request.POST['byte_id']) if 'byte_id' in request.POST else 42
            config = Airconditioner().get_airconditioner_config(db_id)
            airconditioner = Setting.objects.get_or_create(key="air_conditioner")
            airconditioner[0].config = config
            airconditioner[0].save()

            Sensor.objects.filter(type="airconditioner").delete()

            title = request.POST['title']
            for bit in range(0, int(request.POST['airconditioner_count'])):
                sensor = Sensor(title=title + " " + str(bit+1),db_id=db_id, byte_id=byte_id, bit_id=bit,
                                config={}, type="airconditioner")
                sensor.save()
            messages.success(request, 'با موفقیت افزوده شد')
        else:
            messages.error(request, 'حطایی رخ داد، لطفا مجددا تلاش نمایید')
    else:
        form = AirconditionerForm()
    return render(request, 'airconditioner.html', {'form': form})


@login_required
def setting_airconditioner(request):
    airconditioner = get_object_or_404(Setting, key="air_conditioner")
    if request.method == 'POST':
        form = AirconditionerSettingForm(request.POST)
        if form.is_valid():
            airconditioner.config["set_point_on"] = int(request.POST['set_point_on'])
            airconditioner.config["set_point_off"] = int(request.POST['set_point_off'])
            airconditioner.config["control_method"] = True if int(request.POST['control_method']) == 1 else False
            airconditioner.config["start_first_hour"] = int(request.POST['start_first_hour'])
            airconditioner.config["start_second_hour"] = int(request.POST['start_second_hour'])
            airconditioner.config["start_third_hour"] = int(request.POST['start_third_hour'])
            airconditioner.config["set_point_humidity"] = int(request.POST['set_point_humidity'])
            airconditioner.config["time_for_over_range"] = int(request.POST['time_for_over_range'])
            airconditioner.config["manual_air1_on"] = airconditioner.config["manual_air1_on"]
            airconditioner.config["manual_air2_on"] = airconditioner.config["manual_air2_on"]
            airconditioner.config["manual_air3_on"] = airconditioner.config["manual_air3_on"]
            airconditioner.config["manual_air4_on"] = airconditioner.config["manual_air4_on"]
            airconditioner.save()
            Airconditioner().set_airconditioner_config(airconditioner.config, 64)
            messages.success(request, 'با موفقیت ویرایش شد')
        else:
            messages.error(request, 'حطایی رخ داد، لطفا مجددا تلاش نمایید')
    else:
        form = AirconditionerSettingForm()
        form.initial["set_point_on"] = airconditioner.config["set_point_on"]
        form.initial["set_point_off"] = airconditioner.config["set_point_off"]
        form.initial["control_method"] = 1 if airconditioner.config["control_method"] else 0
        form.initial["start_first_hour"] = airconditioner.config["start_first_hour"]
        form.initial["start_third_hour"] = airconditioner.config["start_third_hour"]
        form.initial["start_second_hour"] = airconditioner.config["start_second_hour"]
        form.initial["set_point_humidity"] = airconditioner.config["set_point_humidity"]
        form.initial["time_for_over_range"] = airconditioner.config["time_for_over_range"]
    return render(request, 'settings/airconditioner.html', {'form': form})


@login_required
def edit_airconditioner(request, id=None):
    airconditioner = get_object_or_404(Sensor, pk=id, type="airconditioner")
    setting = get_object_or_404(Setting, key="air_conditioner")
    manual = setting.config["control_method"]
    if request.method == 'POST':
        form = AirconditionerEditForm(request.POST)
        if form.is_valid():
            airconditioner.title = request.POST["title"]
            airconditioner.save()

            if 'status' in request.POST:
                status = True if int(request.POST["status"]) == 1 else False
                Airconditioner().set_airconditioner_status(airconditioner.db_id, airconditioner.config["bit_id"], status)
                setting.config["manual_air" + str(int(airconditioner.config["bit_id"]) + 1) + "_on"] = status
                setting.save()

            messages.success(request, 'با موفقیت ویرایش شد')
        else:
            messages.error(request, 'حطایی رخ داد، لطفا مجددا تلاش نمایید')
    else:
        form = AirconditionerEditForm()
        form.initial["title"] = airconditioner.title
        status = setting.config["manual_air" + str(int(airconditioner.config["bit_id"]) + 1) + "_on"]
        form.initial["status"] = 1 if status else 0

    return render(request, 'airconditioner_edit.html', {'form': form, "manual": manual})

@login_required
def setting_sms(request):
    form = SmsForm()
    return render(request, 'settings/sms.html', {'form': form})

@login_required
def setting_email(request):
    form = EmailForm()
    return render(request, 'settings/email.html', {'form': form})
