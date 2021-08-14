import jdatetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from app.classes.SensorFactory import SensorFactory
from app.classes.SensorFormFactory import SensorFormFactory
from app.classes.SensorHelperFactory import SensorHelperFactory
from app.classes.Sensors.Airconditioner import Airconditioner

from app.forms import AirconditionerForm, AirconditionerSettingForm, SmsForm, EmailForm, AirconditionerEditForm, \
    SearchLogDataForm
from app.models import Sensor, Setting, SensorDataLog


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
                messages.error(request, e.__str__())
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
            config = Airconditioner().get_config(db_id)
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
            Airconditioner().set_data(None, airconditioner.config, 64)
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
        status = setting.config["manual_air" + str(int(airconditioner.bit_id) + 1) + "_on"]
        form.initial["status"] = 1 if status else 0

    return render(request, 'airconditioner_edit.html', {'form': form, "manual": manual})

@login_required
def setting_sms(request):
    airconditioner_setting = Setting.objects.filter(key="air_conditioner").count()
    sms_setting = Setting.objects.get_or_create(key="sms")[0]
    if request.method == 'POST':
        form = SmsForm(request.POST)
        if form.is_valid():
            config = {
                "username": form.cleaned_data["username"],
                "password": form.cleaned_data["password"],
                "url": form.cleaned_data["url"],
                "originator": form.cleaned_data["originator"],
            }

            sms_setting.config = config
            sms_setting.save()

            messages.success(request, 'با موفقیت ویرایش شد')
        else:
            messages.error(request, 'حطایی رخ داد، لطفا مجددا تلاش نمایید')
    else:
        form = SmsForm()
        form.initial["username"] = sms_setting.config["username"] if "username" in sms_setting.config else None
        form.initial["password"] = sms_setting.config["password"] if "password" in sms_setting.config else None
        form.initial["url"] = sms_setting.config["url"] if "url" in sms_setting.config else None
        form.initial["originator"] = sms_setting.config["originator"] if "originator" in sms_setting.config else None
    return render(request, 'settings/sms.html', {'form': form, 'airconditioner_setting': airconditioner_setting})


@login_required
def sensor_log(request):

    form = SearchLogDataForm()
    filter = Q()

    sensor_type = request.GET.get('sensor_type') if 'sensor_type' in request.GET else None
    if sensor_type is not None:
        filter &= Q(sensor_type=sensor_type)
        form.initial["sensor_type"] = sensor_type
        CHOICE_LIST = list(Sensor.objects.values_list("id","title").filter(type=sensor_type))
        form.fields["sensor_id"].choices = tuple([(u'', 'انتخاب نمایید ...')] + CHOICE_LIST)

        sensor_id = request.GET.get('sensor_id') if 'sensor_id' in request.GET else None
        if sensor_id is not None:
            filter &= Q(sensor_id=sensor_id)
            form.initial["sensor_id"] = sensor_id

    sensor_alarm = request.GET.get('sensor_alarm') if 'sensor_alarm' in request.GET else None
    if sensor_alarm is not None:
        filter &= Q(alarm=int(sensor_alarm))
        form.initial["sensor_alarm"] = sensor_alarm

    from_date = request.GET.get('from_date') if 'from_date' in request.GET else None
    if from_date is not None:
        form.initial["from_date"] = to_persian_numbers(from_date.replace("-", "/"))
        form.initial["from_date_value"] = from_date
        from_date = from_date.split(' ')
        date = str(from_date[0]).split("-")
        time = str(from_date[1]).split(":")
        filter &= Q(created_at__gte=jdatetime.datetime(int(date[0]),int(date[1]),int(date[2]),
                                                      int(time[0]),int(time[1]),int(time[2])).togregorian())

    to_date = request.GET.get('to_date') if 'to_date' in request.GET else None
    if to_date is not None:
        form.initial["to_date"] = to_persian_numbers(to_date.replace("-", "/"))
        form.initial["to_date_value"] = to_date
        to_date = to_date.split(' ')
        date = str(to_date[0]).split("-")
        time = str(to_date[1]).split(":")
        filter &= Q(created_at__lte=jdatetime.datetime(int(date[0]), int(date[1]), int(date[2]),
                                                      int(time[0]), int(time[1]), int(time[2])).togregorian())


    logs = SensorDataLog.objects.filter(filter)
    paginator = Paginator(logs, 100)

    page_number = request.GET.get('page') if 'page' in request.GET else 1
    page_obj = paginator.get_page(int(page_number))

    return render(request, 'sensors/log_list.html', {'form': form, 'page_obj': page_obj})


def to_persian_numbers(input_text):
    fa = ["۰", "۱", "۲", "۳", "۴", "۵", "۶", "۷", "۸", "۹"]
    en = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in range(len(en)):
        input_text = input_text.replace(en[i], fa[i])

    return input_text

@login_required
def get_sensor_by_type(request, sensor_type):
    sensors = Sensor.objects.values("id","title").filter(type=sensor_type)
    data = list(sensors)
    return JsonResponse(data, safe=False)
