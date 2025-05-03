# your_chat_app/views.py
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from app.models import ChatRoom

class ChatRoomDetailPage(LoginRequiredMixin, DetailView):
    model = ChatRoom
    template_name = 'pages/room.html'
    pk_url_kwarg = 'connect_id'
    context_object_name = 'room'

    def get_queryset(self):
        # Tùy chọn: Nếu bạn muốn lọc queryset theo user hoặc điều kiện khác
        return super().get_queryset()

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        try:
            return queryset.get(connect_id=self.kwargs['connect_id'])
        except ChatRoom.DoesNotExist:
            raise redirect('some_error_url')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = f"Chat cho Connect ID: {self.object.connect.id}"
        context['connect'] = self.object.connect
        # Thêm bất kỳ biến context nào khác bạn muốn
        context['room_description'] = f"Đây là phòng chat liên kết với Connect có ID {self.object.connect.id}."
        return context