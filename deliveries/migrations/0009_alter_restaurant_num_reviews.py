# Generated by Django 4.2 on 2023-05-05 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveries', '0008_restaurant_num_reviews_restaurant_stars_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='num_reviews',
            field=models.IntegerField(blank=True),
        ),
    ]
