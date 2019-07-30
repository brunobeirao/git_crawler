# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    id = models.AutoField('ID', primary_key=True)
    name = models.CharField('NAME', max_length=32)

    class Meta:
        db_table = 'User'


class Commit(models.Model):
    id = models.AutoField('ID', primary_key=True)
    title = models.CharField('NAME', max_length=32)
    description = models.CharField('NAME', max_length=32)
    date = models.DateTimeField('DATE')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    class Meta:
        db_table = 'Commit'
