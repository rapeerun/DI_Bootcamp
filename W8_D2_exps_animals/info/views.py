from django.shortcuts import render
from .models import Animals,Family

def animals_view (request):
    animals_list=Animals.objects.all()

    context = {
        'animals_list' :  animals_list,

        
    }
    return render(request, 'animals.html', context)

def family_detail(request, family_id):
    family = Family.objects.get(pk=family_id)
    animals = Animals.objects.filter(family=family)
    return render(request, 'family_detail.html', {'family': family, 'animals': animals})




def animal_detail(request, animal_id):
    animal = Animals.objects.get(pk=animal_id)
    return render(request, 'animal_detail.html', {'animal': animal})


# Create your views here.
