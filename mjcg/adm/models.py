from django.db import models


class Membre(models.Model):

    class Meta:
        ordering = ['nom', 'prenom']

    prenom = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    code_postal =  models.CharField(u'code postal', max_length=5)
    localite = models.CharField(u'localité', max_length=100)
    tel = models.CharField(u'téléphone', max_length=14)
    naissance = models.DateField(u'date de naissance')
    email = models.CharField(max_length=200, null=True, blank=True)
    date_certificat = models.DateField('date de certificat médical', 
        null=True, blank=True)
    remarque = models.CharField(max_length=200, null=True, blank=True)    
    activites = models.ManyToManyField('Tarif', through='Cotisation')

    def __str__(self):

        return '{} {}'.format(self.nom, self.prenom)


class Activite(models.Model):

    class Meta:
        ordering = ['nom']

    nom = models.CharField(max_length=200)

    def __str__(self):

        return self.nom


class Tarif(models.Model):

    class Meta:
        ordering = ['annee', 'nom']

    activite = models.ForeignKey(Activite, on_delete=models.CASCADE,
        verbose_name=u"activité")
    nom = models.CharField(max_length=200)
    annee = models.IntegerField(u'année')
    montant = models.IntegerField(u'montant')

    def __str__(self):

        return '{} {} / "{}": {} euros'.format(self.activite, self.annee, self.nom, self.montant)


class Cotisation(models.Model):
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    tarif = models.ForeignKey(Tarif, on_delete=models.CASCADE)
    reglement = models.BooleanField(u'réglement reçu')