from http.client import HTTPResponse
from django.shortcuts import render


# Create your views here.

def login(requests):
    return HTTPResponse("My first Django login App") 