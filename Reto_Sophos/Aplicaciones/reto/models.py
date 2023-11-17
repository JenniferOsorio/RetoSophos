from django.db import models

class Heroe(models.Model):
    id_heroe = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    edad = models.PositiveSmallIntegerField(null=True)
    origen = models.CharField(max_length=100)
    habilidades = models.TextField(blank=True)
    debilidad = models.TextField(blank=True)

class Villano(models.Model):
    id_villano = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    edad = models.PositiveSmallIntegerField(null=True)
    origen = models.CharField(max_length=100)
    habilidades = models.TextField(blank=True)
    debilidad = models.TextField(blank=True)

class Pelea(models.Model):
    id_pelea = models.AutoField(primary_key=True)
    id_villano = models.ForeignKey(Villano, on_delete=models.CASCADE)
    id_heroe = models.ForeignKey(Heroe, on_delete=models.CASCADE)
    resultado = models.CharField(max_length=100)

class Patrocinador(models.Model):
    id_patrocinador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_heroe = models.ForeignKey(Heroe, on_delete=models.CASCADE)
    monto = models.PositiveSmallIntegerField(null=True)
    origenDinero = models.CharField(max_length=100)

