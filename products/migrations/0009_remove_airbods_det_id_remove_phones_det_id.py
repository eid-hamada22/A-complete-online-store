# Generated by Django 4.0.6 on 2022-07-25 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_airbods_img_alter_phones_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airbods',
            name='det_id',
        ),
        migrations.RemoveField(
            model_name='phones',
            name='det_id',
        ),
    ]
