import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from .models import Message


class ChatConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        print('ACCEPT')

        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_id = 'chat_%s' % self.room_id
        await self.channel_layer.group_add(
            self.room_group_id,
            self.channel_name,
        )

    async def disconnect(self, _close_code):
        await self.channel_layer.group_discard(  # グループからチャンネルを削除
            self.room_group_id,
            self.channel_name,
        )
        await self.close()

    async def receive_json(self, data):
        # websocket からメッセージを json 形式で受け取る
        message = data['message']  # 受信データからメッセージを取り出す
        user = data['user']
        await self.createMessage(data)  # メッセージを DB に保存する
        await self.channel_layer.group_send(  # 指定グループにメッセージを送信する
            self.room_group_id,
            {
                'type': 'chat_message',
                'message': message,
                'user': user,
            }
        )

    async def chat_message(self, event):
        # グループメッセージを受け取る
        message = event['message']
        user = event['user']
        # websocket でメッセージを送信する
        await self.send(text_data=json.dumps({
            'type': 'chat_message',
            'message': message,
            'user': user,
        }))

    @database_sync_to_async
    def createMessage(self, event):
        Message.objects.create(
            room_id=self.room_id,
            content=event['message'],
            posted_by=event['user'],
        )
