# Generated by Django 4.2.7 on 2023-11-04 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Levashova_app', '0006_alter_carowner_options_alter_carowner_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carowner',
            options={},
        ),
        migrations.AlterModelManagers(
            name='carowner',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='carowner',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='carowner',
            name='email',
        ),
        migrations.RemoveField(
            model_name='carowner',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='carowner',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='carowner',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='carowner',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='carowner',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='carowner',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='carowner',
            name='password',
        ),
        migrations.RemoveField(
            model_name='carowner',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='carowner',
            name='username',
        ),
    ]