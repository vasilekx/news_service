# api/serializers.py

from rest_framework import serializers

from news.models import News, Comment


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    liked = serializers.SerializerMethodField()
    likes_quantity = serializers.SerializerMethodField()
    comment_quantity = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = (
            'id', 'author', 'text', 'pub_date', 'liked',
            'likes_quantity', 'comment_quantity', 'comments'
        )

    def get_likes_quantity(self, obj):
        return obj.likes.count()

    def get_comment_quantity(self, obj):
        return obj.comments.count()

    def get_comments(self, obj):
        comments = obj.comments.order_by('-created')[:10]
        return CommentSerializer(comments, many=True).data

    def get_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(user=request.user).exists()
        return False

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if request and not request.user.is_authenticated:
            representation.pop('liked')
        return representation


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'created')
