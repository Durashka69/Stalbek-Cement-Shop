from django.db import models
from django.contrib.auth import get_user_model

from mainapp.choices import ScoreChoice


User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(
        upload_to='pictures', verbose_name='Изображение товара', blank=True, null=True
    )
    price = models.PositiveSmallIntegerField(verbose_name='Цена товара')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    @property
    def product_raiting(self):
        if self.raiting.last():
            return sum(
                self.raiting.values_list('score', flat=True)) / \
                len(self.raiting.values_list('score', flat=True))
        return 0

    @property
    def quantity_of_raitings(self):
        if self.product_raiting.last():
            return len(self.raiting.values_list('score', flat=True))


class Raiting(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='raiting', verbose_name='Пользователь'
    )
    score = models.PositiveSmallIntegerField(
        choices=ScoreChoice.choices, verbose_name='Рейтинг'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='Товар', related_name='raiting'
    )
    comment = models.TextField(
        verbose_name='Комментарий', blank=True, null=True
    )

    def __str__(self):
        return f'{self.user} - {self.score} - {self.product}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
