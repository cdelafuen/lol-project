# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class ModeloDePrueba(models.Model):

    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)