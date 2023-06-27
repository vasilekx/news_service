# news/models.py

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class News(models.Model):
    text = models.TextField(
        _('Текст'),
        help_text=_('Текст новости')
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name=_('Автор'),
        help_text=_('Автор, к которому будет относиться новость')
    )
    pub_date = models.DateTimeField(
        _('Дата создания'),
        auto_now_add=True,
        help_text=_('Дата создания будет автоматически установлена '
                    'в текущую дату при создании')
    )

    class Meta:
        ordering = ('pub_date',)
        verbose_name = _('Новость')
        verbose_name_plural = _('Новости')

    def __str__(self):
        return '{:.10} {} {}'.format(
            self.text,
            self.pub_date,
            self.author.get_username(),
        )


class Comment(models.Model):
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('Новость'),
        help_text=_('Новость, к которому будет относиться комментарий')
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('Автор'),
        help_text=_('Автор, к которому будет относиться комментарий')
    )
    text = models.TextField(
        _('Текст'),
        help_text=_('Текст комментария')
    )
    created = models.DateTimeField(
        _('Дата создания'),
        auto_now_add=True,
        help_text=_('Дата создания будет автоматически установлена '
                    'в текущую дату при создании')
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = _('Комментарий')
        verbose_name_plural = _('Комментарии')

    def __str__(self):
        return '{:.15}'.format(self.text)


class Like(models.Model):
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name='likes',
        verbose_name=_('Новость'),
        help_text=_('Новость которую лайкнули'),
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='liked',
        verbose_name=_('Пользователь'),
        help_text=_('Пользователь, который лайкнул'),
        blank=True,
        null=True
    )
    created = models.DateTimeField(
        _('Дата создания'),
        auto_now_add=True,
        blank=True,
        null=True,
        help_text=_('Дата создания будет автоматически установлена '
                    'в текущую дату при создании')
    )

    class Meta:
        verbose_name = _('Лайк')
        verbose_name_plural = _('Лайки')
        constraints = [
            models.UniqueConstraint(fields=['news', 'user'],
                                    name='unique_relationships'),
        ]

    def __str__(self):
        return '{} likes {:.10}'.format(
            self.user.get_username(),
            self.news.text,
        )
