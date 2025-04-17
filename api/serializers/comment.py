from rest_framework import serializers

from app.models import Comment, Document, Forum


class CommentSerializer(serializers.ModelSerializer):
    content_type = serializers.CharField()

    class Meta:
        model = Comment
        fields = [
            "object_id",
            "text",
            "content_type",
        ]

    def save(self, **kwargs):
        content_type = self.validated_data["content_type"]
        object_id = self.validated_data["object_id"]
        text = self.validated_data["text"]

        request = self.context.get("request")
        user = request.user

        if content_type == "Document":
            content_model = Document
        else:
            content_model = Forum

        content_object = content_model.objects.filter(pk=object_id).first()

        Comment.objects.create(
            content_object=content_object,
            owner=user.student,
            text=text,
        )
