# Generated by Django 4.2 on 2023-05-05 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deliveries', '0009_alter_restaurant_num_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='price',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='categories',
            field=models.ManyToManyField(blank=True, to='deliveries.restaurant_types'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals', to='deliveries.restaurant'),
        ),
    ]