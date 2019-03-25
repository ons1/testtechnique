from django.db import models


class Equipe (models.Model):
    nom=models.CharField('Nom')
    drapeau=models.CharField('Drapeau')





class Joueur (models.Model):
    nom=models.CharField('Nom')
    num=models.IntegerField('Num')
    present=models.BooleanField('Present ?')
    equipe_id=models.ForeignKey('Equipe')
