# Generated by Django 4.1.3 on 2023-01-10 05:30

from django.db import migrations, models
import main.utils


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_car_brand_car_color_car_engine_car_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(default='default-images/car/car_default.png', null=True, upload_to=main.utils.upload_image),
        ),
    ]
