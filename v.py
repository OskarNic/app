from django.db import models

class Nation(models.Model):
    nation = models.Charfield(max_length=50)

class Tank(models.Model):
    tank   =models.Charfield(max_length=50)
    nation =models.ForeignKey(Nation, on_delete=models.CASCADE)
    type   =models.ManyToManyField('Type')

class Type(models.Model):
    type = models.Charfield(max_length=50)
