from django.db import models

class Family(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return (self.name)





class Animals(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    legs = models.IntegerField()
    weight=models.FloatField()
    height=models.FloatField()
    speed=models.FloatField()
    family=models.ForeignKey(Family, on_delete=models.CASCADE)

    
    def __str__(self):
        return "%d %s" % (self.id,self.name)



# Create your models here.
