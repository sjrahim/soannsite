# Generated by Django 3.2.4 on 2021-08-20 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soannapp', '0003_alter_product_productstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='childcategory',
            name='slug',
            field=models.SlugField(max_length=60, null=True, unique=True),
        ),
    ]