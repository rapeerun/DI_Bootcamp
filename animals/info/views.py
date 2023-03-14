from django.shortcuts import render
# from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from .models import Family, Animal
import json

def family_detail(request, pk):
    with open('./info/dj.json') as jsonfile:
        data=json.load(jsonfile)

    context={
            'family_name' : data['families'][pk]['name']

        }
    
    return render(request, 'info/family_details.html',context)
    # family = get_object_or_404(Family, pk=pk)
    # animals = Animal.objects.filter(family=family)
    # return render(request, 'family_detail.html', {'family': family, 'animals': animals})

def animal_detail(request, pk):
    with open('./info/dj.json') as jsonfile:
        data=json.load(jsonfile)

    context={
            'animal_name' : data['animals'][pk]['name']

        }
    return render(request, 'info/animals_details.html',context)


    # animal = get_object_or_404(Animal, pk=pk)
    # return render(request, 'animal_detail.html', {'animal': animal})

# Create your views here.
