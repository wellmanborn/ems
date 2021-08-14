import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import datetime

from app.models import Sensor as SensorModel, SensorDataLog as SensorDataLogModel



@login_required
def show(request, sensor_type):
    humidities = SensorModel.objects.filter(type=sensor_type)
    response = {}
    for humidity in humidities:
        data = SensorDataLogModel.objects.values_list("created_at", "value").filter(sensor_id=humidity.id)
        result = []
        for dt in data:
            result.append([int(dt[0].timestamp()), dt[1]])
        response[humidity.title] = result
    return render(request, 'charts/show.html', {'data': json.load(response)})

