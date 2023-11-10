from django.db import models

# Create your models here.

class Lugat(models.Model):
    inglizcha=models.CharField(max_length=250)
    uzbekcha=models.CharField(max_length=250)

class English(models.Model):
    sarlavha=models.CharField(max_length=250)
    text=models.TextField()