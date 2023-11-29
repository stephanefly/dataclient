from django.db import models

class FormulaireEvenement(models.Model):
    nom_insta = models.CharField(max_length=100)
    GENRE_CHOICES = [
        ('F', 'Féminin'),
        ('M', 'Masculin'),
    ]
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)
    nb_abo = models.IntegerField()
    ORIGINE_CHOICES = [
        ('Indien-Sri', 'Indien-Sri'),
        ('Europe', 'Europe'),
        ('Afrique', 'Afrique'),
        ('Arab', 'Arab'),
        ('Chinois', 'Chinois'),
        ('Portugais', 'Portugais'),
        ('Russe', 'Russe'),
        ('Turque', 'Turque'),
        ('Juifs', 'Juifs'),
    ]
    origine = models.CharField(max_length=10, choices=ORIGINE_CHOICES)
    date_demande = models.DateField()
    date_event = models.DateField(null=True, blank=True)
    TYPE_MARIAGE_CHOICES = [
        ('je sais pas', 'je sais pas'),
        ('Mariage', 'Mariage'),
        ('Anniversaire Maison', 'Anniversaire Maison'),
        ('Anniversaire Salle', 'Anniversaire Salle'),
    ]
    type_mariage = models.CharField(max_length=100, choices=TYPE_MARIAGE_CHOICES,null=True)
    salle = models.CharField(max_length=100, null=True)
    PHOTOBOTH_CHOICES = [
        ('je sais pas', 'je sais pas'),
        ('photobooth', 'Photobooth'),
        ('miroirbooth', 'Miroirbooth'),
        ('360booth', '360booth'),
        ('miroirbooth+360booth', 'miroirbooth+360booth'),
    ]
    photobooth = models.CharField(max_length=100, choices=PHOTOBOTH_CHOICES, null=True)
    mur_floral = models.BooleanField(default=False)
    prix_propose = models.IntegerField(null=True, blank=True)
    abonner = models.BooleanField(default=False)
    ok = models.BooleanField(default=False)
    relance = models.BooleanField(default=False)
    chezconcurrent = models.BooleanField(default=False)
    pas_de_dispo = models.BooleanField(default=False)
    commentaire = models.TextField(default=False, null=True)
