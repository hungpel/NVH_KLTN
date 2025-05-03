# your_chat_app/models.py
from django.db import models
from django.contrib.auth.models import User
from app.models import Connect  # Thay 'your_app_name' bằng ứng dụng chứa Connect

class ChatRoom(models.Model):
    connect = models.ForeignKey(
        Connect,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='chat_room'
    )
    name = models.CharField(max_length=255, unique=True)  # Tên phòng (có thể dựa trên Connect name/ID)
    subscribers = models.ManyToManyField(User, blank=True, related_name='chat_rooms')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    room = models.ForeignKey(
        ChatRoom,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='chat_messages'
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {self.user.username}: {self.content[:50]}"