# Generated by Django 4.2.7 on 2023-11-04 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Levashova_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carowner',
            old_name='car_owner_id',
            new_name='id',
        ),
    ]