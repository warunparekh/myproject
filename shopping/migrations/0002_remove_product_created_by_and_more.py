# Generated by Django 5.0.3 on 2024-03-29 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='product',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='discounted_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated_date',
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_data',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]