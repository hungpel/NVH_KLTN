from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from app.models import Document, Forum, Like


class LikeSerializer(serializers.ModelSerializer):
    content_type = serializers.CharField()

    class Meta:
        model = Like
        fields = [
            "object_id",
            "content_type",
        ]

    def save(self, **kwargs):
        content_type = self.validated_data["content_type"]
        object_id = self.validated_data["object_id"]

        request = self.context.get("request")
        user = request.user

        if content_type == "Document":
            content_model = Document
        else:
            content_model = Forum

        content_object = content_model.objects.filter(pk=object_id).first()
        content_type = ContentType.objects.get_for_model(content_model)

        like = Like.objects.filter(
            content_type=content_type.pk,
            owner=user.student,
            object_id=object_id,
        )

        if like.exists():
            like.delete()
            return False
        else:
            Like.objects.create(
                content_object=content_object,
                owner=user.student,
            )
            return True
