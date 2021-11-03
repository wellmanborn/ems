import json
from channels.generic.websocket import AsyncWebsocketConsumer


class SnapConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.channel_layer.group_add("snap7", self.channel_name)
        await self.accept()

    async def disconnect(self, **kwargs):
        await self.channel_layer.group_discard("snap7", self.channel_name)

    async def send_data(self, event):
        resp = event['response']
        data = resp['data']
        message = resp['message']
        time_data = resp['time']
        reset_airconditioner = resp['reset_airconditioner']
        allow_to_snooze = resp['allow_to_snooze']
        await self.send(text_data=json.dumps({
            'message': message,
            "data": data,
            "time": time_data,
            "reset_airconditioner": reset_airconditioner,
            "allow_to_snooze": allow_to_snooze
        }))