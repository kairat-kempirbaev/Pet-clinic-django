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
    user = graphene.Field(UserType, user_id=graphene.Int())

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_user(self, info, user_id):
        return User.objects.all(pk=user_id)


schema = graphene.Schema(query=Query)
