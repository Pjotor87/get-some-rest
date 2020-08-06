from django.db import models


class Musician(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    band = models.CharField(max_length=50)


class Instrument(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    instrument = models.CharField(max_length=50)
