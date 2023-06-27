# api/views.py

from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from news.models import News, Like
from .permissions import IsAdministratorOwnerOrReadOnly, IsAdministratorOwnerOwnerNewsOrReadOnly
from .serializers import NewsSerializer, CommentSerializer
from .utilities import delete_object


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAdministratorOwnerOrReadOnly,)
    http_method_names = ['get', 'post', 'put', 'delete']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    @action(
        detail=True,
        methods=['post', 'delete'],
        permission_classes=[IsAuthenticated],
    )
    def like(self, request, pk=None):
        news = self.get_object()
        fields = {'news': news, 'user': request.user}
        if_already_exists = Like.objects.filter(**fields).exists()
        if request.method == 'DELETE':
            return delete_object(
                model=Like,
                fields=fields,
                exist=if_already_exists,
                errors_message=_('Вы не лайкали эту новость.'),
            )
        if if_already_exists:
            return Response(
                {
                    'errors': _('Вы уже лайкнули этот комментарий.')
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            like = Like(**fields)
            like.save()
            return Response(
                {
                    'detail': _('Новость лайкнута.')
                },
                status=status.HTTP_201_CREATED
            )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAdministratorOwnerOwnerNewsOrReadOnly,)
    http_method_names = ['get', 'post', 'delete']

    def get_news(self):
        return get_object_or_404(News, pk=self.kwargs.get('news_id'))

    def get_queryset(self):
        return self.get_news().comments.all()

    def perform_create(self, serializer):
        serializer.save(news=self.get_news(), author=self.request.user)
