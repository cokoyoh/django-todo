# Generated by Django 2.2 on 2019-05-31 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('created_at', models.DateField(default='2019-05-31')),
                ('due_date', models.DateField(default='2019-05-31')),
                ('category', models.ForeignKey(default='general', on_delete='CASCADE', to='todolist.Category')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
