from django.db import models

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=50)
    numero_habitantes = models.PositiveIntegerField()

    def __str__(self):
        return "{}".format(self.nombre)
    
    class Meta():
        db_table = 'pais'
