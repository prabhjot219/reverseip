from django.db import models

class ReversedIP(models.Model):
    original_ip = models.CharField(max_length=15)
    reversed_ip = models.CharField(max_length=15)

