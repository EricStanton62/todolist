# Generated by Django 2.1 on 2018-08-15 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20180814_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='is_complete',
            field=models.BooleanField(default=True),
        ),
    ]
