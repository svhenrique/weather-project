# Generated by Django 3.1.2 on 2020-10-19 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201019_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='estado',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='pais',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='País'),
        ),
    ]
