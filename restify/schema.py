import graphene
from graphene_django import DjangoObjectType

from .models import Vets, Specialties, VetSpecialties, Owners, Types, Pets, Visits, Roles, Users


class VetsType(DjangoObjectType):
    class Meta:
        model = Vets
        fields = ("id", "first_name", "last_name")


class SpecialtiesType(DjangoObjectType):
    class Meta:
        model = Specialties
        fields = ("id", "name")


class VetSpecialtiesType(DjangoObjectType):
    class Meta:
        model = VetSpecialties
        fields = ("id", "vet_id", "specialty_id")


class OwnersType(DjangoObjectType):
    class Meta:
        model = Owners
        fields = ("id", "first_name", "last_name",
                  "address", "city", "telephone")


class TypesType(DjangoObjectType):
    class Meta:
        model = Types
        fields = ("id", "name")


class PetsType(DjangoObjectType):
    class Meta:
        model = Pets
        fields = ("id", "name", "birth_date", "type_id", "owner_id")


class VisitsType(DjangoObjectType):
    class Meta:
        model = Visits
        fields = ("id", "pet_id", "visit_date", "description")


class RolesType(DjangoObjectType):
    class Meta:
        model = Roles
        fields = ("id", "name", "notes", "category")


class UsersType(DjangoObjectType):
    class Meta:
        model = Users
        fields = ("id", "username", "enabled")


class RolesType(DjangoObjectType):
    class Meta:
        model = Users
        fields = ("id", "username", "role")


class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    category_by_name = graphene.Field(
        CategoryType, name=graphene.String(required=True))

    def resolve_all_ingredients(root, info):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
