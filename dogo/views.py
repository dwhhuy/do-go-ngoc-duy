# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from dogo.models import Post, Product, Tag
import json


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def chair(request):
    products = Product.objects.filter(product_tag=1)
    return render(request, 'ban_ghe.html', context={'data': products})


def statue(request):
    products = Product.objects.filter(product_tag=2)
    return render(request, 'tuong_go.html', context={'data': products})


def another(request):
    products = Product.objects.filter(product_tag=3)
    return render(request, 'sp_khac.html', context={'data': products})


def blog(request):
    posts = Post.objects.all()
    return render(request, 'post.html', context={'data': posts})
