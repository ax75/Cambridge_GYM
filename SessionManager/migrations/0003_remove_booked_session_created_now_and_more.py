# Generated by Django 4.1.2 on 2022-10-21 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SessionManager', '0002_rename_date_created_booked_session_created_now'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booked_session',
            name='created_now',
        ),
        migrations.AddField(
            model_name='booked_session',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]