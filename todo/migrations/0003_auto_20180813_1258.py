# Generated by Django 2.1 on 2018-08-13 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20180803_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='item',
            field=models.CharField(max_length=50),
        ),
    ]