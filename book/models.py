# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Library(models.Model):
    library_name = models.CharField(max_length=250)
    capacity = models.CharField(max_length=250)
    def __str__(self):
        return self.library_name + " - " + self.capacity
class Book(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
