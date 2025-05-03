# your_chat_app/views.py
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from app.models import ChatRoom

class ChatRoomDetailView(LoginRequiredMixin, DetailView):
    model = ChatRoom
    template_name = 'pages/room.html'
    pk_url_kwarg = 'connect_id'
    context_object_name = 'room'

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except ChatRoom.DoesNotExist:
            return redirect('some_error_url')  # Thay bằng URL xử lý lỗi
        context = self.get_context_data(object=self.object)
        context['room_name'] = self.object.name  # Hoặc thông tin từ Connect nếu cần
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['connect'] = self.object.connect
        context['page_name'] = f"Chat cho Connect ID: {self.object.connect.id}"
        # Thêm bất kỳ biến context nào khác bạn muốn
        context['room_description'] = f"Đây là phòng chat liên kết với Connect có ID {self.object.connect.id}."
        return context