# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1> Book Homepage</h1>")

def library_details(request, library_id):
    return HttpResponse("<h1> This is library number %s</h1>"%str(library_id))

