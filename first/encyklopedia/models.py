from django.db import models

# Create your models here.
from django.db import models

class Nation(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Tank(models.Model):
    name   =models.CharField(max_length=50)
    nation =models.ForeignKey(Nation, on_delete=models.CASCADE)
    type   =models.ManyToManyField('Type')

    def __str__(self):
        return self.name
        
class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

