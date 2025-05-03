# # your_chat_app/consumers.py
# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from channels.db import database_sync_to_async
# from django.contrib.auth.models import User
# from .models import ChatRoom, Message

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.connect_id = self.scope['url_route']['kwargs']['connect_id']
#         self.room_group_name = f"chat_{self.connect_id}"
#         self.user = self.scope.get('user')

#         if self.user.is_authenticated:
#             try:
#                 room = await self.get_room(self.connect_id)
#                 await self.add_user_to_room(room, self.user)
#                 await self.channel_layer.group_add(
#                     self.room_group_name,
#                     self.channel_name
#                 )
#                 await self.accept()
#                 await self.send_previous_messages(room)
#             except ChatRoom.DoesNotExist:
#                 await self.close()
#         else:
#             await self.close()

#     async def disconnect(self, close_code):
#         if self.user.is_authenticated:
#             try:
#                 room = await self.get_room(self.connect_id)
#                 await self.remove_user_from_room(room, self.user)
#                 await self.channel_layer.group_discard(
#                     self.room_group_name,
#                     self.channel_name
#                 )
#             except ChatRoom.DoesNotExist:
#                 pass

#     async def receive(self, text_data):
#         if self.user.is_authenticated:
#             text_data_json = json.loads(text_data)
#             message_content = text_data_json['message']
#             room = await self.get_room(self.connect_id)

#             if room:
#                 message = await self.create_message(room, self.user, message_content)
#                 await self.channel_layer.group_send(
#                     self.room_group_name,
#                     {
#                         'type': 'chat.message',
#                         'message': message_content,
#                         'user': self.user.username,
#                         'timestamp': message.timestamp.isoformat(),
#                     }
#                 )

#     async def chat_message(self, event):
#         message = event['message']
#         user = event['user']
#         timestamp = event['timestamp']

#         await self.send(text_data=json.dumps({
#             'message': message,
#             'user': user,
#             'timestamp': timestamp,
#         }))

#     @database_sync_to_async
#     def get_room(self, connect_id):
#         return ChatRoom.objects.get(connect_id=connect_id)

#     @database_sync_to_async
#     def add_user_to_room(self, room, user):
#         room.subscribers.add(user)

#     @database_sync_to_async
#     def remove_user_from_room(self, room, user):
#         room.subscribers.remove(user)

#     @database_sync_to_async
#     def create_message(self, room, user, content):
#         return Message.objects.create(room=room, user=user, content=content)

#     @database_sync_to_async
#     def get_previous_messages(self, room):
#         return list(Message.objects.filter(room=room).order_by('timestamp')[:50])

#     async def send_previous_messages(self, room):
#         messages = await self.get_previous_messages(room)
#         for message in messages:
#             await self.send(text_data=json.dumps({
#                 'message': message.content,
#                 'user': message.user.username,
#                 'timestamp': message.timestamp.isoformat(),
#             }))