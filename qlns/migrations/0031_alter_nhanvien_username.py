# Generated by Django 3.2.7 on 2021-09-05 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qlns', '0030_alter_nhanvien_sdt2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nhanvien',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Tài Khoản Nhân Viên'),
        ),
    ]
