# Generated by Django 3.2.3 on 2021-08-14 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qlns', '0026_auto_20210811_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='dexuat',
            name='nhanviencc',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
    ]
