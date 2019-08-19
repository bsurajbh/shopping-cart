from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """first index page"""
    return HttpResponse('First Page.Works')
