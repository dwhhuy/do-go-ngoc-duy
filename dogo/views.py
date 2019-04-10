# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from dogo.models import Post, Product, Tag
import json


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def chair(request):
    product = Product.objects.get(product_tag=1)
    return render(request, 'ban_ghe.html', product)
