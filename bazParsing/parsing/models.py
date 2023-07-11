from django.db import models

# Create your models here.

class Apartment(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название ЖК')
    square = models.FloatField(verbose_name='Площадь')
    price = models.IntegerField(verbose_name='Цена')
    date = models.DateField(verbose_name='Дата сдачи ЖК')
    decor = models.BooleanField(verbose_name='Отделка')
    date_view = models.DateField(verbose_name='Дата просмотра')
    is_metro = models.BooleanField(verbose_name='Наличие метро')
    metro_name = models.CharField(max_length=50, blank=True, verbose_name='Название метро')
    is_mcd = models.BooleanField(verbose_name='Наличие МЦД')
    mcd_name = models.CharField(max_length=50, blank=True, verbose_name='Название МЦД')
    rent = models.IntegerField(verbose_name='Плата за аренду')
    mortgage = models.IntegerField(verbose_name='Ипотека')