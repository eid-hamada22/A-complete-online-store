# Generated by Django 4.0.6 on 2022-07-19 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_rename_category_pproduct_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='ar_name',
        ),
        migrations.RenameField(
            model_name='pcategory',
            old_name='name',
            new_name='ar_name',
        ),
        migrations.AddField(
            model_name='category',
            name='en_name',
            field=models.CharField(default=' ', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pcategory',
            name='en_name',
            field=models.CharField(default=' ', max_length=250),
            preserve_default=False,
        ),
    ]