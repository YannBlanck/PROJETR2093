from django.db import models

# Create your models here.
class Albums(models.Model):
    nom_album = models.CharField(max_length=100)
    Groupe_chanteur = models.CharField(max_length=100)
    annee = models.DateField(blank=True, null=True)
    nbr_titre = models.IntegerField(blank=True)
    Acheter = models.ForeignKey("Acheter", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"Nom {self.nom_album} Groupe {self.Groupe_chanteur} Année de parrution {self.annee} nbr de titre {self.nbr_titre}"
        return chaine

    def music(self):
        return  {"nom_album" : self.nom_album, "Groupe_chanteur" : self.Groupe_chanteur, "annee": self.annee, "nbr_titre": self.nbr_titre, "Acheter": self.Acheter}

class Acheter(models.Model):
    Nom_acheteur = models.CharField(max_length=100)
    Nbr_album = models.CharField(max_length=100)
    date_achat = models.DateField(blank=True, null=True)
    Prix_total = models.IntegerField(blank=True)


    def __str__(self):
        chain = f"Nom {self.Nom_acheteur} Nbr_album {self.Nbr_album} date achat {self.date_achat} Prix total {self.Prix_total}"
        return chain

    def ach(self):
        return  {"Nom_acheteur" : self.Nom_acheteur, "Nbr_album" : self.Nbr_album, "date_achat": self.date_achat, "Prix_total": self.Prix_total}