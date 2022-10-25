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


class Owners(models.Model):
    first_name = models.CharField(max_length=30)
    last_name =  models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    city =  models.CharField(max_length=80)
    telephone =  models.CharField(max_length=20)

class Types(models.Model):
    name = models.CharField(max_length=80)

class Pets(models.Model):
    name = models.CharField(max_length=30)
    birth_date = models.DateField()
    type_id = models.ForeignKey(Types, on_delete=models.CASCADE)
    owner_id = models.ForeignKey(Owners, on_delete=models.CASCADE)

class Visits(models.Model):
    pet_id = models.ForeignKey(Pets, on_delete=models.CASCADE)
    visit_date = models.DateField()
    description = models.CharField(max_length=255)
