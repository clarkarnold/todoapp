# Generated by Django 3.1.2 on 2020-10-02 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='urgent',
            field=models.BooleanField(default=False),
        ),
    ]
