from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from my_serializers import RegisterSerializer


class SignUp(APIView):
    serializer_class = RegisterSerializer
    success_url = reverse_lazy("overview")
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "pages/register.html"

    def get(self, request, *args, **kwargs):
        return Response(template_name=self.template_name)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(template_name=self.template_name)
