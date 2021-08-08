import json
# from asyncio import sleep

# from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

# from app.classes.Device import Device
# from app.classes.Sensor import Sensor
# from app.models import Sensor as SensorModel


class SnapConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.channel_layer.group_add("snap7", self.channel_name)
        await self.accept()
        # client = Device().get_client()
        # if client and client.get_connected():
        #     sensors = await sync_to_async(list)(SensorModel.objects.all())
        #     while True:
        #         try:
        #             if Device().get_status() != "writing" and Device().get_status() != "reading":
        #                 response = Sensor().get_all_sensors_data(sensors)
        #                 await self.send(text_data=json.dumps({
        #                     'data': response["data"],
        #                     'message': response["message"]
        #                 }))
        #         except Exception as e:
        #             await self.send(text_data=json.dumps({
        #                 'message': str(e),
        #                 "data": {}
        #             }))
        #         await sleep(1)
        # else:
        #     await self.send(text_data=json.dumps({
        #         'message': "1- Device is not connected, please be sure the device is ready and accessible",
        #         "data": {}
        #     }))


    async def disconnect(self, **kwargs):
        await self.channel_layer.group_discard("snap7", self.channel_name)

    async def send_data(self, event):
        resp = event['response']
        data = resp['data']
        message = resp['message']
        await self.send(text_data=json.dumps({
            'message': message,
            "data": data
        }))