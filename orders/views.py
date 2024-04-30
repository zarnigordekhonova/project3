from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def get_user_order(request):
    return HttpResponse('Fill out the form to make an order!')