from django.db import models


# Create your models here.

class Apartment(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название ЖК')
    development = models.ForeignKey('Development', on_delete=models.CASCADE, verbose_name='Застройщик')
    url = models.URLField(unique=True, verbose_name='Ссылка')
    square = models.FloatField(verbose_name='Площадь')
    price = models.IntegerField(verbose_name='Цена')
    date = models.DateField(verbose_name='Дата сдачи ЖК')
    decor = models.BooleanField(verbose_name='Отделка')
    date_view = models.DateField(verbose_name='Дата просмотра', auto_now_add=True)
    is_metro = models.BooleanField(verbose_name='Наличие метро')
    metro_name = models.CharField(max_length=50, blank=True, verbose_name='Название метро')
    is_mcd = models.BooleanField(verbose_name='Наличие МЦД')
    mcd_name = models.CharField(max_length=50, blank=True, verbose_name='Название МЦД')
    rent = models.IntegerField(verbose_name='Плата за аренду')
    mortgage = models.IntegerField(verbose_name='Ипотека')
    image = models.FilePathField(path='F:/github/bazParsing/bazParsing/media/', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Обьект'
        verbose_name_plural = 'Обьекты'

    def __str__(self):
        return self.name


class Development(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название застройщика')

    class Meta:
        verbose_name = 'Застройщик'
        verbose_name_plural = 'Застройщики'

    def __str__(self):
        return self.name
