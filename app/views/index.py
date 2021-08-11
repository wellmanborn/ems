from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from app.models import Sensor

@login_required
def index(request):
    temperatures = Sensor.objects.filter(type="temperature")
    humidities = Sensor.objects.filter(type="humidity")
    powers = Sensor.objects.filter(type="power")
    waterleakages = Sensor.objects.filter(type="waterleakage")
    doors = Sensor.objects.filter(type="door")
    smokes = Sensor.objects.filter(type="smoke")
    fuses = Sensor.objects.filter(type="fuse")
    airconditioners = Sensor.objects.filter(type="airconditioner")
    return render(request, "main.html", {
        "temperatures": temperatures,
        "humidities": humidities,
        "powers": powers,
        "waterleakages": waterleakages,
        "doors": doors,
        "smokes": smokes,
        "fuses": fuses,
        "airconditioners": airconditioners
    })