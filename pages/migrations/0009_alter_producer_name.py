# Generated by Django 4.0.3 on 2022-03-28 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_user_h_purchase_remove_brand_category_brand_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producer',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
