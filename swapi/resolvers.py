from swapi.models import Human


def resolver_humans():
    return Human.objects.all()


def resolver_human(id):
    return Human.objects.get(id=id)


def resolver_create_human(id, name, gender, birth_year, mass, height, home_planet):
    return Human.objects.create(
        id=id,
        name=name,
        gender=gender,
        birth_year=birth_year,
        mass=mass,
        height=height,
        home_planet=home_planet,
    )


def resolver_update_human(id, name, gender, birth_year, mass, height, home_planet):
    human = Human.objects.get(id=id)
    human.name = name
    human.gender = gender
    human.birth_year = birth_year
    human.mass = mass
    human.height = height
    human.home_planet = home_planet
    human.save()
    return human


def resolver_delete_human(id):
    _ = Human.objects.get(id=id).delete()
    return
