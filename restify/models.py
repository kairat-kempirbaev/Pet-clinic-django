from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import VetUserManager


class Vets(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Specialties(models.Model):
    name = models.CharField(max_length=80)


class VetSpecialties(models.Model):
    vet_id = models.ForeignKey(Vets, on_delete=models.CASCADE)
    specialty_id = models.ForeignKey(Specialties, on_delete=models.CASCADE)


class Owners(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=80)
    telephone = models.CharField(max_length=20)


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


class Users(AbstractUser):
    # Alternative to is_active
    username = models.CharField(max_length=20, unique=True)
    enabled = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'

    objects = VetUserManager()

    def __str__(self):
        return self.username


class Roles(models.Model):
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    role = models.CharField(max_length=20)