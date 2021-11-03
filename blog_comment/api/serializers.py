from rest_framework import serializers

from blog_comment.models import Comment


class CommentListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return {
            "username":obj.user.username,
        }


    class Meta:
        model = Comment
        fields = [
            'user',
            'name',
            'body',           
            'create', 
            'object_id',
        ]


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'object_id',
            'name',
            'body',
        ]