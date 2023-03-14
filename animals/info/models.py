from django.db import models

import json
from django.http import HttpResponse



# Open the 
#JSON file and load its contents
with open('./info/dj.json') as json_file:
    data = json.load(json_file)

# Use the data in a Django view
def my_view(request):
    # Do something with the data
    return HttpResponse("Data loaded from JSON file!")



with open('./info/dj.json', 'r+') as json_file:
    data = json.load(json_file)
    new_data = {' families': 'id', 'name': "mammal"}
    new_data = {' families': 'id', 'name': "reptile"}
    new_data = {' families': 'id', 'name': "insect"}
    new_data = {' families': 'id', 'name': "arachnid"}
    new_data = {' families': 'id', 'name': "amphibian"}
    new_data = {"id": 3,
            "name": "Cow",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1}
    
    data["animals"].append(new_data)
    json_file.seek(0)
    json.dump(data, json_file, indent=4)



class Family(models.Model):
    name = models.CharField(max_length=50)

class Animal(models.Model):
    name = models.CharField(max_length=50)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    species = models.CharField(max_length=50)


  

# Create your models here.
