# Generated by Django 4.1.7 on 2023-03-01 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='login',
        ),
        migrations.AddField(
            model_name='profile',
            name='length_of_last_session',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]