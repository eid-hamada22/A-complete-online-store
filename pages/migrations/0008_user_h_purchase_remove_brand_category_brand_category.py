# Generated by Django 4.0.3 on 2022-03-28 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_brand_alter_producer_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='h_purchase',
            field=models.BooleanField(default=False),
        ),
        migrations.RemoveField(
            model_name='brand',
            name='Category',
        ),
        migrations.AddField(
            model_name='brand',
            name='Category',
            field=models.ManyToManyField(null=True, to='pages.category'),
        ),
    ]
