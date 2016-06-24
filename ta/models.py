from __future__ import unicode_literals

from django.db import models

# Create your models here.

class employee(models.Model):
    emp_no = models.IntegerField(default=0)
    emp_name = models.CharField(max_length=200)
    basic_pay = models.IntegerField(default=0)
    division = models.CharField(max_length=200)
    headq = models.CharField(max_length=50, default='Varanasi')
    branch = models.CharField(max_length=200)
    ta = models.IntegerField(default=500)
