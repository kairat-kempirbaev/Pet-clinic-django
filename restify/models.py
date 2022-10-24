from django.db import models

# Create your models here.
class Vets(models.Model):
    first_name = models.CharField(max_length=30)
    last_name =  models.CharField(max_length=30)

class Specialties(models.Model):
    name = models.CharField(max_length=80)

class VetSpecialties(models.Model):
    vet_id = models.ForeignKey(Vets, on_delete=models.CASCADE)
    specialty_id = models.ForeignKey(Specialties, on_delete=models.CASCADE)
