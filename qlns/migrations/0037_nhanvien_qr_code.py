# Generated by Django 3.2.7 on 2021-09-08 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qlns', '0036_auto_20210907_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='nhanvien',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='qr_codes'),
        ),
    ]
