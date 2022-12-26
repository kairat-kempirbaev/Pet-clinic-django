from graphene_django import DjangoObjectType
from .models import Employee, Owner, Pet, Specialty, Type, User, Visit


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name",
                  "address", "city", "telephone")


class SpecialtiesType(DjangoObjectType):
    class Meta:
        model = Specialty
        fields = ("id", "name")


class PetClassType(DjangoObjectType):
    class Meta:
        model = Type
        fields = ("id", "name",)


class PetType(DjangoObjectType):
    class Meta:
        model = Pet
        fields = ("id", "pets")


class OwnersType(DjangoObjectType):
    class Meta:
        model = Owner
        fields = ("id", "pets")


class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee
        fields = ("user", "specialities")


class VisitType(DjangoObjectType):
    class Meta:
        model = Visit
        fields = ("id", "pet", "owner", "visit_date", "description")
