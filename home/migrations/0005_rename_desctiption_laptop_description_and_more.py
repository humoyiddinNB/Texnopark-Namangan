# Generated by Django 5.1.6 on 2025-02-27 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_laptop_options_alter_phone_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laptop',
            old_name='desctiption',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='phone',
            old_name='desctiption',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='watch',
            old_name='desctiption',
            new_name='description',
        ),
    ]
