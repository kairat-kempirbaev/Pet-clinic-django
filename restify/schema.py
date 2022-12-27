from graphene_django import DjangoObjectType
from .models import *
import graphene

class UserType(DjangoObjectType):
    class Meta:
        model = User


class PetClassType(DjangoObjectType):
    class Meta:
        model = Type


class PetType(DjangoObjectType):
    class Meta:
        model = Pet


class OwnersType(DjangoObjectType):
    class Meta:
        model = Owner

class SpecialtyType(DjangoObjectType):
    class Meta:
        model = Specialty

class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee


class VisitType(DjangoObjectType):
    class Meta:
        model = Visit


class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return User.objects.all()

schema = graphene.Schema(query=Query)