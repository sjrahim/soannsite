# Generated by Django 3.2.4 on 2021-08-20 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soannapp', '0002_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productstatus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pv', to='soannapp.productstatus'),
        ),
    ]
