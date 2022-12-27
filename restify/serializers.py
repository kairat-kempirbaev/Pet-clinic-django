from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    specialities = SpecialtySerializer(read_only=True, many=True)

    class Meta:
        model = Employee
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class PetSerializer(serializers.ModelSerializer):
    type_id = TypeSerializer(read_only=True)

    class Meta:
        model = Pet
        fields = '__all__'


class OwnerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    pets = PetSerializer(read_only=True, many=True)
    class Meta:
        model = Owner
        fields = '__all__'


class VisitSerializer(serializers.ModelSerializer):
    pet = PetSerializer(read_only=True)
    owner = OwnerSerializer(read_only=True)

    class Meta:
        model = Visit
        fields = '__all__'
