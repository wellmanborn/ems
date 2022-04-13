from app.models import Setting
from ems.settings import AIRCONDITIONER_REVERSE


def store_air_conditioner_config(db_id, air_conditioner_type, config):
    airconditioner = Setting.objects.get_or_create(key="air_conditioner")[0]
    config_data = {}
    config_data["config"] = {}
    config_data["setting"] = {}
    if type(airconditioner.config) == dict:
        if "config" in airconditioner.config:
            for key in airconditioner.config["config"]:
                if int(key) != int(db_id):
                    config_data["config"][int(key)] = airconditioner.config["config"][key]
    config_data["config"][int(db_id)] = config
    config_data["setting"]["count"] = len(config_data["config"])
    config_data["setting"]["reverse"] = AIRCONDITIONER_REVERSE
    config_data["setting"]["type"] = air_conditioner_type
    airconditioner.config = config_data
    airconditioner.save()