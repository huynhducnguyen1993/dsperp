# Generated by Django 3.2.3 on 2021-07-26 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khachhang', '0002_auto_20210726_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='khachhanglon',
            name='tenkhachhang',
            field=models.CharField(default='', max_length=255, verbose_name='Tên Khách Hàng'),
        ),
    ]
