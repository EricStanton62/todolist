# Generated by Django 2.1 on 2018-08-14 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20180813_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='checkbox',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
