# Generated by Django 4.0.6 on 2022-07-27 09:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_contact_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='description',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='title',
            name='sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='title',
            name='type',
            field=models.CharField(choices=[('RC', 'Records'), ('CL', 'Clothing'), ('PS', 'Posters'), ('ML', 'Miscellaneous')], default='RC', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='title',
            name='year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2023)]),
        ),
    ]
