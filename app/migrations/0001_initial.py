# Generated by Django 3.2.16 on 2023-10-14 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormulaireEvenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reseaux', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=20)),
                ('nb_abo', models.IntegerField()),
                ('origine', models.CharField(max_length=100)),
                ('date_demande', models.DateField()),
                ('date_event', models.DateField()),
                ('jour_semaine', models.CharField(max_length=10)),
                ('type_mariage', models.CharField(max_length=100)),
                ('salle', models.CharField(max_length=100)),
                ('photobooth', models.BooleanField()),
                ('mur_flora', models.BooleanField()),
                ('prix_propose', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ok', models.BooleanField()),
                ('commentaire', models.TextField()),
            ],
        ),
    ]
