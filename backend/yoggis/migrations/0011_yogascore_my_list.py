# Generated by Django 4.1.5 on 2023-03-07 10:15

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoggis', '0010_merge_20230128_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='yogascore',
            name='my_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, default=[], size=None),
        ),
    ]
