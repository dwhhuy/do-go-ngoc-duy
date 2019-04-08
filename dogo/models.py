# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Tag(models.Model):
    tag_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.tag_name


class Product(models.Model):
    image = models.FileField()
    product_name = models.CharField(max_length=200)
    product_price = models.CharField(blank=True, max_length=200)
    product_tag = models.ForeignKey(Tag)

    def __unicode__(self):
        return self.product_name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.FileField()

    def __unicode__(self):
        return self.title
