pets=[
    [
        "Leo",
        "2000-09-07",
        1,
        1
    ],
    [
        "Basil",
        "2002-08-06",
        6,
        2
    ],
    [
        "Rosy",
        "2001-04-17",
        2,
        3
    ],
    [
        "Jewel",
        "2000-03-07",
        2,
        3
    ],
    [
        "Iggy",
        "2000-11-30",
        3,
        4
    ],
    [
        "George",
        "2000-01-20",
        4,
        5
    ],
    [
        "Samantha",
        "1995-09-04",
        1,
        6
    ],
    [
        "Max",
        "1995-09-04",
        1,
        6
    ],
    [
        "Lucky",
        "1999-08-06",
        5,
        7
    ],
    [
        "Mulligan",
        "1997-02-24",
        2,
        8
    ],
    [
        "Freddy",
        "2000-03-09",
        5,
        9
    ],
    [
        "Lucky",
        "2000-06-24",
        2,
        10
    ],
    [
        "Sly",
        "2002-06-08",
        1,
        10
    ]
]
for i,elem in enumerate(pets):
    toPrint=f"""{{"model": "myapp.pets","pk": {i},"fields": {{"birth_date": "{elem[1]}","type_id":"{elem[2]}","owner_id":"{elem[3]}"}}}},"""
    print(toPrint)
owners = [
    [ 'George', 'Franklin', '110 W. Liberty St.', 'Madison', '6085551023' ],
    [ 'Betty', 'Davis', '638 Cardinal Ave.', 'Sun Prairie', '6085551749' ],
    [ 'Eduardo', 'Rodriquez', '2693 Commerce St.', 'McFarland', '6085558763' ],
    [ 'Harold', 'Davis', '563 Friendly St.', 'Windsor', '6085553198' ],
    [ 'Peter', 'McTavish', '2387 S. Fair Way', 'Madison', '6085552765' ],
    [ 'Jean', 'Coleman', '105 N. Lake St.', 'Monona', '6085552654' ],
    [ 'Jeff', 'Black', '1450 Oak Blvd.', 'Monona', '6085555387' ],
    [ 'Maria', 'Escobito', '345 Maple St.', 'Madison', '6085557683' ],
    [ 'David', 'Schroeder', '2749 Blackhawk Trail', 'Madison', '6085559435' ],
    [ 'Carlos', 'Estaban', '2335 Independence La.', 'Waunakee', '6085555487' ]
]
for i,elem in enumerate(owners):
    toPrint=f"""{{"model": "myapp.owners","pk": {i},"fields": {{"first_name": "{elem[0]}","last_name":"{elem[1]}","address":"{elem[2]}","city":"{elem[3]}","telephone":"{elem[4]}"}}}},"""
    print(toPrint)
