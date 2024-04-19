from django.db import models

class SweetType(models.Model):
    name = models.CharField(max_length=128)
