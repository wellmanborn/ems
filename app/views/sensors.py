import jdatetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from app.classes.Sensor import Sensor
from app.classes.SensorFactory import SensorFactory
from app.classes.SensorFormFactory import SensorFormFactory
from app.classes.SensorHelperFactory import SensorHelperFactory

from app.classes.Sensors.Alarm import Alarm


from app.forms.setting.sms import SmsForm
from app.forms.search import SearchLogDataForm
from app.forms.setting.alarm import AlarmForm
from app.models import Sensor as SensorModel, Setting, AnalogSensorDataLog
from app.views.air_conditioner import delete as DeleteAirConditioner


@login_required
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
                sensor = SensorModel.objects.get_or_create(db_id=db_id, byte_id=byte_id, bit_id=bit_id,
                                                           type=sensor_type)[0]
                sensor.title = request.POST['title']
                sensor.start_value = start_value
                sensor.byte_id = byte_id
                sensor.bit_id = bit_id

                settings = {}
                for key, value in request.POST.items():
                    if key.startswith('setting__'):
                        key = key.replace('setting__', '')
                        settings[key] = value

                sensor.setting = settings
                sensor.save()
                config = sensor_class.get_config(db_id, sensor)
                sensor.config = config
                sensor.save()
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
    sensor = get_object_or_404(SensorModel, pk=id)
    sensor_class = SensorFactory.get_sensor(sensor.type)
    sensor_helper_class = SensorHelperFactory.get_sensor_helper(sensor.type)
    if request.method == 'POST':
        form = SensorFormFactory.get_sensor_form(sensor.type, request.POST)
        if form.is_valid():
            try:
                config = sensor_helper_class.get_config_from_request(request)
                sensor_class.set_data(sensor, config)
                sensor.title = request.POST['title']
                if "byte_id" in request.POST:
                    sensor.byte_id = int(request.POST['byte_id'])
                if "bit_id" in request.POST:
                    sensor.bit_id = int(request.POST['bit_id'])
                if "start_value" in request.POST:
                    sensor.start_value = int(request.POST['start_value'])
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
def delete_sensor(request, id):
    sensor = get_object_or_404(SensorModel, pk=id)
    if sensor.type == "airconditioner":
        DeleteAirConditioner(sensor.db_id)
    else:
        sensor.delete()
    return redirect("/")

@login_required
def stop_snooze(request):
    if request.method == 'POST':
        try:
            Sensor().stop_snooze()
            return JsonResponse({'success': True, 'message': 'با موفقیت انجام شد'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': 'حطایی رخ داد، لطفا مجددا تلاش نمایید'})
    pass


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
def setting_alarm(request):
    airconditioner_setting = Setting.objects.filter(key="air_conditioner").count()
    alarm_setting = Setting.objects.get_or_create(key="alarm")[0]
    if request.method == 'POST':
        form = AlarmForm(request.POST)
        if form.is_valid():
            config = {
                "snooze_time": form.cleaned_data["snooze_time"],
                "time_for_siren_on_day": form.cleaned_data["time_for_siren_on_day"],
                "time_for_siren_off_day": form.cleaned_data["time_for_siren_off_day"],
                "time_for_siren_on_night": form.cleaned_data["time_for_siren_on_night"],
                "time_for_siren_off_night": form.cleaned_data["time_for_siren_off_night"],
                "start_work_time": form.cleaned_data["start_work_time"],
                "end_work_time": form.cleaned_data["end_work_time"],
                "total_sms": form.cleaned_data["total_sms"],
                "time_for_repeat_send_sms": form.cleaned_data["time_for_repeat_send_sms"],
            }

            alarm_setting.config = config
            alarm_setting.save()
            Alarm().set_data(None, config, 69)

            messages.success(request, 'با موفقیت ویرایش شد')
        else:
            messages.error(request, 'حطایی رخ داد، لطفا مجددا تلاش نمایید')
    else:
        form = AlarmForm()
        config = Alarm().get_config(69)
        form.initial["snooze_time"] = config["snooze_time"]
        form.initial["time_for_siren_on_day"] = config["time_for_siren_on_day"]
        form.initial["time_for_siren_off_day"] = config["time_for_siren_off_day"]
        form.initial["time_for_siren_on_night"] = config["time_for_siren_on_night"]
        form.initial["time_for_siren_off_night"] = config["time_for_siren_off_night"]
        form.initial["start_work_time"] = config["start_work_time"]
        form.initial["end_work_time"] = config["end_work_time"]
        form.initial["total_sms"] = config["total_sms"]
        form.initial["time_for_repeat_send_sms"] = config["time_for_repeat_send_sms"]
    return render(request, 'settings/alarm.html', {'form': form, 'airconditioner_setting': airconditioner_setting})


@login_required
def sensor_log(request):
    form = SearchLogDataForm()
    filter = Q()

    sensor_type = request.GET.get('sensor_type') if 'sensor_type' in request.GET else None
    if sensor_type is not None:
        filter &= Q(sensor_type=sensor_type)
        form.initial["sensor_type"] = sensor_type
        CHOICE_LIST = list(SensorModel.objects.values_list("id", "title").filter(type=sensor_type))
        form.fields["sensor_id"].choices = tuple([(u'', 'انتخاب نمایید ...')] + CHOICE_LIST)

        sensor_id = request.GET.get('sensor_id') if 'sensor_id' in request.GET else None
        if sensor_id is not None:
            filter &= Q(sensor_id=sensor_id)
            form.initial["sensor_id"] = sensor_id

    from_date = request.GET.get('from_date') if 'from_date' in request.GET else None
    if from_date is not None:
        form.initial["from_date"] = to_persian_numbers(from_date.replace("-", "/"))
        form.initial["from_date_value"] = from_date
        from_date = from_date.split(' ')
        date = str(from_date[0]).split("-")
        time = str(from_date[1]).split(":")
        filter &= Q(created_at__gte=jdatetime.datetime(int(date[0]), int(date[1]), int(date[2]),
                                                       int(time[0]), int(time[1]), int(time[2])).togregorian())

    to_date = request.GET.get('to_date') if 'to_date' in request.GET else None
    if to_date is not None:
        form.initial["to_date"] = to_persian_numbers(to_date.replace("-", "/"))
        form.initial["to_date_value"] = to_date
        to_date = to_date.split(' ')
        date = str(to_date[0]).split("-")
        time = str(to_date[1]).split(":")
        filter &= Q(created_at__lte=jdatetime.datetime(int(date[0]), int(date[1]), int(date[2]),
                                                       int(time[0]), int(time[1]), int(time[2])).togregorian())

    logs = AnalogSensorDataLog.objects.filter(filter)
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


def to_english_numbers(input_text):
    fa = ["۰", "۱", "۲", "۳", "۴", "۵", "۶", "۷", "۸", "۹"]
    en = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in range(len(fa)):
        input_text = input_text.replace(fa[i], en[i])

    return input_text


@login_required
def get_sensor_by_type(request, sensor_type):
    sensors = SensorModel.objects.values("id", "title").filter(type=sensor_type)
    data = list(sensors)
    return JsonResponse(data, safe=False)
