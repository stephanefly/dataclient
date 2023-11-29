# Generated by Django 3.2.16 on 2023-10-16 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_formulaireevenement_salle'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulaireevenement',
            name='abonner',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='formulaireevenement',
            name='commentaire',
            field=models.TextField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='formulaireevenement',
            name='photobooth',
            field=models.CharField(choices=[('je sais pas', 'je sais pas'), ('photobooth', 'Photobooth'), ('miroirbooth', 'Miroirbooth'), ('360booth', '360booth'), ('miroirbooth+360booth', 'miroirbooth+360booth')], max_length=100, null=True),
        ),
    ]