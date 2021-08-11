"""ems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from app.views import index, sensors, accounts

urlpatterns = [
    path('', index.index),
    path('sensors/create/<sensor_type>', sensors.add_sensor),
    path('sensors/edit/<id>', sensors.edit_sensor),

    path('sensors/add/airconditioner', sensors.add_airconditioner),
    path('setting/airconditioner', sensors.setting_airconditioner),
    path('sensors/edit/airconditioner/<id>', sensors.edit_airconditioner),
    path('setting/sms', sensors.setting_sms),
    path('setting/email', sensors.setting_email),

    path('accounts/', accounts.list),
    path('accounts/create', accounts.create),
    path('accounts/edit/<id>', accounts.edit),
    path('accounts/change/password/user/<id>', accounts.change_user_password),
    path('accounts/login/', accounts.login_page),
    path('accounts/logout/', accounts.logout_page),
]
