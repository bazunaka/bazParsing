# Generated by Django 3.2.20 on 2023-07-15 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='image',
            field=models.CharField(blank=True, max_length=80, verbose_name='Изображение'),
        ),
    ]
