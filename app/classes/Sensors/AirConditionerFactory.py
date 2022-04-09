from app.classes.Sensors.Airconditioner.AirconditionerFull import AirConditionerFull
from app.classes.Sensors.Airconditioner.AirconditionerTempOnly import AirConditionerTempOnly
import logging
logger = logging.getLogger('django')

class AirConditionerFactory():

    @staticmethod
    def get_air_conditioner(air_conditioner_type="full"):
        logger.warning("here")
        if air_conditioner_type == "full":
            logger.warning("fullllllllllll")
            return AirConditionerFull()
        elif air_conditioner_type == "temponly":
            logger.warning("temponlyyyyyyyyyyyyyyyyyyyyyyy")
            return AirConditionerTempOnly()
