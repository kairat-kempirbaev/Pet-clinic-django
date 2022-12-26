from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    EMPLOYEE = 1
    OWNER = 2

    ROLE_CHOICES = (
        (EMPLOYEE, 'Employee'),
        (OWNER, 'Owner'),
    )

    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=80)
    telephone = models.CharField(max_length=20)


class Type(models.Model):
    name = models.CharField(max_length=80)


class Pet(models.Model):
    name = models.CharField(max_length=30)
    birth_date = models.DateField()
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)


class Owner(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    pets = models.ManyToManyField(Pet, related_name='owners')


class Specialty(models.Model):
    name = models.CharField(max_length=80)


class Employee(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    specialities = models.ManyToManyField(Specialty, related_name='specialists')


class Visit(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    visit_date = models.DateField()
    description = models.CharField(max_length=255)
