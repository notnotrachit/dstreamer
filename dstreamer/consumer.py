# import asyncio
# import json
# from channels.consumer import AsyncConsumer

# class StreamConsumer(AsyncConsumer):

#     async def websocket_connect(self, event):
#         # print('connected', event)
#         print('connected')
#         await self.send({
#             'type': 'websocket.accept'
#         })

#     async def websocket_receive(self, event):
#         # print('received', event)
#         print('received')
#         message = json.loads(event['text'])
#         await self.send({
#             'type': 'websocket.send',
#             'text': message['image']
#         })

#     async def websocket_send(self, event):
#         # print('sent', event)
#         print('sent')

#     async def websocket_disconnect(self, event):
#         # print('disconnected', event)
#         print('disconnected')
import asyncio
import json
import base64
from asgiref.sync import async_to_sync

from channels.generic.websocket import AsyncWebsocketConsumer

class StreamConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.stream_id = self.scope['url_route']['kwargs']['stream_id']
        self.stream_url = f'stream/{self.stream_id}/'
        await self.channel_layer.group_add(
            self.stream_id,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.stream_id,
            self.channel_name
        )

    async def receive(self, text_data):
        print('received')
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.stream_id,
            {
                'type': 'send_stream',
                'image': data['image']
            }
        )

    async def send_stream(self, event):
        await self.send(text_data=json.dumps({
            'image': event['image']
        }))

class WatchConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.stream_id = self.scope['url_route']['kwargs']['stream_id']
        self.stream_url = f'stream/{self.stream_id}/'
        await self.accept()

    async def disconnect(self, close_code):
        pass

