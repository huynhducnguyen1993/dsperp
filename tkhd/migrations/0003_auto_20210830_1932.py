# Generated by Django 3.2.3 on 2021-08-30 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tkhd', '0002_auto_20210829_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='tkhd',
            name='khachhang',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='tkhd',
            name='mahopdong',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]