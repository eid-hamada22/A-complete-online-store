# Generated by Django 4.0.3 on 2022-07-15 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_det_delete_types'),
        ('pages', '0019_remove_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='det',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.det'),
        ),
    ]