# Generated by Django 3.2.16 on 2023-10-16 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20231016_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulaireevenement',
            name='relance',
            field=models.BooleanField(default=False),
        ),
    ]
