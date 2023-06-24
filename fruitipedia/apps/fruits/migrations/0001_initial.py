# Generated by Django 4.2.2 on 2023-06-24 06:23

import apps.fruits.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), apps.fruits.validators.name_content_only_letter], verbose_name='Name')),
                ('image_url', models.URLField(verbose_name='Image URL')),
                ('description', models.TextField(verbose_name='Description')),
                ('nutrition', models.TextField(blank=True, null=True, verbose_name='Nutrition')),
            ],
        ),
    ]
