# Generated by Django 2.0 on 2020-08-18 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20200811_0906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_data',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='user_data',
            name='email',
        ),
        migrations.AddField(
            model_name='user_data',
            name='identity',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
