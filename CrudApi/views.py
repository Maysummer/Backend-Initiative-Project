from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def Users(request):
    dataReturned = {
        'id' : 1,
        'name' : 'Nmesoma Udojike',
    }
    return JsonResponse(dataReturned)

def Movies(request):
    dataReturned = {
        'id' : 1,
        'name' : 'The Crown',
        'legthInHours' : 2,
    }
    return JsonResponse(dataReturned)

def Rentals(request):
    dataReturned = {
        'id' : 1,
        'amount' : 2000,
    }
    return JsonResponse(dataReturned)