# Generated by Django 2.2 on 2019-05-31 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='categories',
        ),
        migrations.AlterModelTable(
            name='todolist',
            table='todo_lists',
        ),
    ]
