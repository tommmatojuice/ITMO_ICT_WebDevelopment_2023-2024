# Generated by Django 4.2.7 on 2023-11-04 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Levashova_app', '0003_rename_cer_brand_car_car_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='state_number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='carowner',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='driverlicense',
            name='license_number',
            field=models.CharField(max_length=10),
        ),
    ]