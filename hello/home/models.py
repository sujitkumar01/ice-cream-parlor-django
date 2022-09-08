from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phnumber = models.CharField(max_length=122)
    purpose = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
