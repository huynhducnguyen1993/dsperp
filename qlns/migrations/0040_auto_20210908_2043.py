# Generated by Django 3.2.7 on 2021-09-08 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qlns', '0039_auto_20210908_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quatrinhdongbhxh',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='quatrinhdongbhxh',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]