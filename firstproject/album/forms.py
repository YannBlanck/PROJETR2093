from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class AlbumsForm(ModelForm):
    class Meta:
        model = models.Albums
        fields = ('nom_album', 'Groupe_chanteur', 'annee', 'nbr_titre', 'Acheter')
        labels = {
            'nom_album': _('Nom'),
            'Groupe_chanteur': _('Group'),
            'annee': _('Annee'),
            'nbr_titre': _('Nombre_de_titre'),
            'Acheter': _('Acheter')
        }
class AcheterForm(ModelForm):
    class Meta:
        model = models.Acheter
        fields = ('Nom_acheteur', 'Nbr_album', 'date_achat', 'Prix_total')
        labels = {
            'Nom_acheteur': _('Nom'),
            'Nbr_album': _('nbr_album'),
            'date_achat': _('date achat'),
            'Prix_total': _('Prix'),

        }