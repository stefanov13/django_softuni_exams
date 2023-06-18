# Generated by Django 4.2.2 on 2023-06-17 16:45

import apps.plant.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_type', models.CharField(choices=[('outdoor_plants', 'Outdoor Plants'), ('indoor_plants', 'Indoor Plants')], max_length=14)),
                ('name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), apps.plant.validators.name_only_letters])),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
    ]