# import sys
# sys.path.append('../../')
# import load_db
# migrations.RunPython
import datetime


def make_user(role: int, f_name: str, l_name: str, street: str, city: str, phone: str) -> dict:
    return {"username": f'{f_name} {l_name} {street}', "role": role, "first_name": f_name,
            "last_name": l_name, "address": street, "city": city, "telephone": phone, "password": "password"}


def populate_database(apps, schema_editor):
    '''
    Update to match the schema.
    '''
    # Set Users
    User = apps.get_model('restify', 'User')
    user_john = User.objects.create_user(
        **make_user(1, "John", "Lennon", "Grumpy valley", "some city", "1234567890"))
    user_john.save()
    user_paul = User.objects.create_user(
        **make_user(1, "Paul", "James", "Desert street", "Happy-vil", "2234567890"))
    user_paul.save()
    user_helen = User.objects.create_user(
        **make_user(1, "Helen", "Leary", "Stormy street", "Royal vil", "3234567890"))
    user_helen.save()
    user_linda = User.objects.create_user(
        **make_user(1, "Linda", "Douglas", "Sunny street", "Up hill village", "4234567890"))
    user_linda.save()
    user_rafael = User.objects.create_user(
        **make_user(1, "Rafael", "Ortega", "Happy valley", "the bottom", "5234567890"))
    user_rafael.save()
    user_henry = User.objects.create_user(
        **make_user(1, "Henry", "Stevens", "Hill will", "the highway", "6234567890"))
    user_henry.save()
    user_sharon = User.objects.create_user(
        **make_user(1, "Sharon", "Jenkins", "Up and down", "intersection", "7234567890"))
    user_sharon.save()

    # Set Specialities
    Specialty = apps.get_model('restify', 'Specialty')
    speciality_radiology = Specialty(name="radiology")
    speciality_radiology.save()
    speciality_surgery = Specialty(name="surgery")
    speciality_surgery.save()
    speciality_dentistry = Specialty(name="dentistry")
    speciality_dentistry.save()

    # Set Specialities for employees
    Employee = apps.get_model('restify', 'Employee')
    emp = Employee(user=user_john)
    emp.specialities.add(speciality_radiology, speciality_surgery)
    emp.save()
    emp = Employee(user=user_paul)
    emp.specialities.add(speciality_radiology, speciality_dentistry)
    emp.save()
    emp = Employee(user=user_helen)
    emp.specialities.add(speciality_radiology)
    emp.save()
    emp = Employee(user=user_linda)
    emp.specialities.add(speciality_surgery)
    emp.save()
    Employee(user=user_rafael)
    emp.specialities.add(speciality_radiology, speciality_surgery)
    emp.save()
    emp = Employee(user=user_henry)
    emp.specialities.add(speciality_dentistry)
    emp.save()
    emp = Employee(user=user_sharon)
    emp.specialities.add(speciality_surgery)
    emp.save()

    # PET TYPE
    PetKind = apps.get_model('restify', 'Type')
    lizard_type = PetKind(name="lizard")
    lizard_type.save()
    cat_type = PetKind(name="cat")
    cat_type.save()
    hamster_type = PetKind(name="hamster")
    hamster_type.save()
    snake_type = PetKind(name="snake")
    snake_type.save()
    dog_type = PetKind(name="dog")
    dog_type.save()
    parrot_type = PetKind(name="parrot")
    parrot_type.save()
    unique_bird_type = PetKind(name="unique bird")
    unique_bird_type.save()
    tortoise_type = PetKind(name="tortoise")
    tortoise_type.save()

    # PETS
    Pet = apps.get_model('restify', 'Pet')
    parrot_pet = Pet(name="wisdom", birth_date=datetime.date(
        2002, 8, 6), type_id=parrot_type)
    parrot_pet.save()
    dog_pet = Pet(name="barker", birth_date=datetime.date(
        2012, 4, 1), type_id=dog_type)
    dog_pet.save()
    lizard_pet = Pet(name="sneaky", birth_date=datetime.date(
        2018, 5, 6), type_id=lizard_type)
    lizard_pet.save()
    cat_pet = Pet(name="king", birth_date=datetime.date(
        2001, 8, 22), type_id=cat_type)
    cat_pet.save()
    bird_pet = Pet(name="beauty", birth_date=datetime.date(
        2018, 6, 6), type_id=unique_bird_type)
    bird_pet.save()
    hamster_pet = Pet(name="sleepster", birth_date=datetime.date(
        2022, 8, 24), type_id=hamster_type)
    hamster_pet.save()
    snake_pet = Pet(name="ka", birth_date=datetime.date(
        2020, 8, 12), type_id=snake_type)
    snake_pet.save()
    parrot2_pet = Pet(name="grumpy", birth_date=datetime.date(
        1993, 11, 10), type_id=parrot_type)
    parrot2_pet.save()
    tortoise_pet = Pet(name="slowy", birth_date=datetime.date(
        1983, 11, 10), type_id=tortoise_type)
    tortoise_pet.save()

    # Owners
    Owner = apps.get_model('restify', 'Owner')
    betty_user = User.objects.create_user(**make_user(2,
                                                      "Betty",
                                                      "Davis",
                                                      "638 Cardinal Ave.",
                                                      "Sun Prairie",
                                                      "6085551749"
                                                      ))
    betty_user.save()
    betty_owner = Owner(user=betty_user)
    betty_owner.pets.add(tortoise_pet)
    betty_owner.save()

    eduardo_user = User.objects.create_user(**make_user(2,
                                                        "Eduardo",
                                                        "Rodriquez",
                                                        "2693 Commerce St.",
                                                        "McFarland",
                                                        "6085558763"))
    eduardo_user.save()
    eduardo_owner = Owner(user=eduardo_user)
    eduardo_owner.pets.add(tortoise_pet)
    eduardo_owner.save()

    harold_user = User.objects.create_user(**make_user(2,
                                                       "Harold",
                                                       "Davis",
                                                       "563 Friendly St.",
                                                       "Windsor",
                                                       "6085553198"))
    harold_user.save()
    harold_owner = Owner(user=harold_user)
    harold_owner.pets.add(parrot2_pet, hamster_pet)
    harold_owner.save()

    peter_user = User.objects.create_user(**make_user(2,
                                                      "Peter",
                                                      "McTavish",
                                                      "2387 S. Fair Way",
                                                      "Madison",
                                                      "6085552765"))
    peter_user.save()
    peter_owner = Owner(user=peter_user)
    peter_owner.pets.add(bird_pet)
    peter_owner.save()

    jean_user = User.objects.create_user(**make_user(2,
                                                     "Jean",
                                                     "Coleman",
                                                     "105 N. Lake St.",
                                                     "Monona",
                                                     "6085552654"))
    jean_user.save()
    jean_owner = Owner(user=jean_user)
    jean_owner.pets.add(snake_pet)
    jean_owner.save()

    jeff_user = User.objects.create_user(** make_user(2,
                                                      "Jeff",
                                                      "Black",
                                                      "1450 Oak Blvd.",
                                                      "Monona",
                                                      "6085555387"
                                                      ))
    jeff_user.save()
    jeff_owner = Owner(user=jeff_user)
    jeff_owner.pets.add(cat_pet)
    jeff_owner.save()

    maria_user = User.objects.create_user(** make_user(2,
                                                       "Maria",
                                                       "Escobito",
                                                       "345 Maple St.",
                                                       "Madison",
                                                       "6085557683"))
    maria_user.save()
    maria_owner = Owner(user=maria_user)
    maria_owner.pets.add(lizard_pet)
    maria_owner.save()

    david_user = User.objects.create_user(** make_user(2,
                                                       "David",
                                                       "Schroeder",
                                                       "2749 Blackhawk Trail",
                                                       "Madison",
                                                       "6085559435"))
    david_user.save()
    david_owner = Owner(user=david_user)
    david_owner.pets.add(dog_pet)
    david_owner.save()

    carlos_user = User.objects.create_user(** make_user(2,
                                                        "Carlos",
                                                        "Estaban",
                                                        "2335 Independence La.",
                                                        "Waunakee",
                                                        "6085555487"))
    carlos_user.save()
    carlos_owner = Owner(user=carlos_user)
    carlos_owner.pets.add(parrot_pet)
    carlos_owner.save()

    # Visits
    Visit = apps.get_model('restify', 'Visit')
    Visit(owner=dog_pet.owners.all()[0],pet=dog_pet, **{
        "visit_date": datetime.date(2008, 9, 4),
        "description": "spayed"
    }).save()
    Visit(owner=dog_pet.owners.all()[0],pet=dog_pet, **{
        "visit_date": datetime.date(2009, 9, 4),
        "description": "rabies shot"
    }).save()
    Visit(owner=cat_pet.owners.all()[0],pet=cat_pet, **{
        "visit_date": datetime.date(2022, 9, 4),
        "description": "neutered."
    }).save()
    Visit(owner=tortoise_pet.owners.all()[0],pet=tortoise_pet, **{
        "visit_date": datetime.date(2021, 7, 4),
        "description": "Health check"
    }).save()
# python manage.py migrate
# python manage.py createsuperuser
