# Generated by Django 3.2.20 on 2023-07-08 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('square', models.FloatField()),
                ('price', models.IntegerField()),
                ('date', models.DateField()),
                ('decor', models.BooleanField()),
                ('date_view', models.DateField()),
                ('is_metro', models.BooleanField()),
                ('metro_name', models.CharField(blank=True, max_length=50)),
                ('is_mcd', models.BooleanField()),
                ('mcd_name', models.CharField(blank=True, max_length=50)),
                ('rent', models.IntegerField()),
                ('mortgage', models.IntegerField()),
            ],
        ),
    ]
