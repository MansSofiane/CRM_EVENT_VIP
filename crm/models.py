from django.db import models

class Collaborateurs(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)
    class Meta:
        db_table = 'Collaborateurs'

class Option(models.Model):
    id = models.AutoField(primary_key=True)
    nom_option = models.CharField(max_length=100)
    description = models.TextField()
    cout_additionnel = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        db_table = 'Option'

class Formules(models.Model):
    id = models.AutoField(primary_key=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    titre = models.CharField(max_length=100)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    class Meta:
        db_table = 'Formules'

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    nom_societe = models.CharField(max_length=255)
    secteur_activite = models.CharField(max_length=255)
    adresse = models.TextField()
    contact_email = models.EmailField()
    contact_telephone = models.CharField(max_length=20)
    class Meta:
        db_table = 'Client'

    def __str__(self):
        return self.nom_societe

class Evenements(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    lieu = models.CharField(max_length=100)
    prix_total = models.DecimalField(max_digits=10, decimal_places=2)
    cout = models.DecimalField(max_digits=10, decimal_places=2)
    benifice = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    formules = models.ForeignKey(Formules, on_delete=models.CASCADE)
    collaborateur = models.ForeignKey(Collaborateurs, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    class Meta:
        db_table = 'Evenements'

class Prestations(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    cout = models.DecimalField(max_digits=10, decimal_places=2)
    conditions = models.TextField()
    class Meta:
        db_table = 'Prestation'

    def __str__(self):
        return self.description
