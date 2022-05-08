from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.http import JsonResponse

from app.forms.search import SearchLogDataForm
from app.models import SensorDataLog as SensorDataLogModel, Sensor


@login_required
def index(request):
    form = SearchLogDataForm()
    return render(request, 'charts/show.html', {"form": form})


@login_required
def sensor_data(request):
    # form = SearchLogDataForm()
    response = []
    if request.method == 'POST':
        sensor_type = request.POST['sensor_digital_type']
        filter = Q()
        filter &= Q(sensor_type=sensor_type)

        sensors = Sensor.objects.filter(type=sensor_type)
        for sensor in sensors:
            data = SensorDataLogModel.objects.values_list("created_at", "value")\
                .filter(filter).filter(db_id=sensor.db_id).filter(byte_id=sensor.byte_id).order_by('created_at')
            result = []
            for dt in data:
                result.append([int(dt[0].timestamp()) * 1000, dt[1]])
            response.append({"name": sensor.title, "data": result})

        if sensor_type == "humidity":
            data = SensorDataLogModel.objects.values_list("created_at", "value") \
                .filter(filter).filter(db_id=64).order_by('created_at')
            result = []
            for dt in data:
                result.append([int(dt[0].timestamp()) * 1000, round(dt[1], 2)])
            response.append({"name": "AvgHum(x)", "data": result})

            data = SensorDataLogModel.objects.values_list("created_at", "value") \
                .filter(filter).filter(db_id=85).order_by('created_at')
            result = []
            for dt in data:
                result.append([int(dt[0].timestamp()) * 1000, round(dt[1], 2)])
            response.append({"name": "AvgHum(y)", "data": result})

        if sensor_type == "temperature":
            data = SensorDataLogModel.objects.values_list("created_at", "value") \
                .filter(filter).filter(db_id=64).order_by('created_at')
            result = []
            for dt in data:
                result.append([int(dt[0].timestamp()) * 1000, round(dt[1], 2)])
            response.append({"name": "AvgTmp(x)", "data": result})

            data = SensorDataLogModel.objects.values_list("created_at", "value") \
                .filter(filter).filter(db_id=85).order_by('created_at')
            result = []
            for dt in data:
                result.append([int(dt[0].timestamp()) * 1000, round(dt[1], 2)])
            response.append({"name": "AvgTmp(y)", "data": result})

    return JsonResponse({'success': True, 'name': 'humidity', 'data': response})
