import asyncio
import json
import base64
from asgiref.sync import async_to_sync
from PIL import Image
from channels.generic.websocket import AsyncWebsocketConsumer
from io import BytesIO

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
        image_data = base64.b64decode(event['image'].split(',')[1])
        image = Image.open(BytesIO(image_data)).convert('L')
        buffer = BytesIO()
        image.save(buffer, format='JPEG')
        image_str = base64.b64encode(buffer.getvalue()).decode()
        await self.send(text_data=json.dumps({
            'image': f"data:image/jpeg;base64,{image_str}"
        }))

class WatchConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.stream_id = self.scope['url_route']['kwargs']['stream_id']
        self.stream_url = f'stream/{self.stream_id}/'
        await self.accept()

    async def disconnect(self, close_code):
        pass

