import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class AnalyticsConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_group_name="Analytics"
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        print("connected")

    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        self.close()
    
    async def receive(self, text_data):
        data=await self.decode_json(text_data)
        message=data['value']
        print(message)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'send_data',
                'value':message
            }
        )

    async def send_data(self,event):
        data=event['value']
        await self.send(text_data=await self.encode_json({"value":data}))