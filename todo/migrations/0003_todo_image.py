# Generated by Django 4.0 on 2022-03-26 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='image',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
