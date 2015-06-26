from django.db import models

class Martyr(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    cause_of_death = models.TextField(max_length=500)
    officer_name = models.CharField(max_length=200)
    governorate = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name