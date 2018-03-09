from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)


class Company(models.Model):
    pass