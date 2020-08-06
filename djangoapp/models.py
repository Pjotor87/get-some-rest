from django.db import models


class Musician(models.Model):
    firstname_text = models.CharField(max_length=50)
    lastname_text = models.CharField(max_length=50)
    band_text = models.CharField(max_length=50)
    added_date = models.DateTimeField('date published')


class Instrument(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    instrument_text = models.CharField(max_length=50)
