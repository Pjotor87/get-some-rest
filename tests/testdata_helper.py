import pytest
from djangoapp.models import Musician as Model
import djangoapp.seed as Seeder


@pytest.mark.django_db
def seed_musician_table():
    testdata_seed = [
        Model(firstname="James", lastname="Hetfield", band="Metallica"),
        Model(firstname="John", lastname="Petrucci", band="Dream Theater"),
        Model(firstname="Mike", lastname="Portnoy", band="Dream Theater"),
        Model(firstname="Dave", lastname="Mustaine", band="Megadeth"),
    ]
    seeder = Seeder.SQLiteSeed(testdata_seed)
    seeder.seed()


@pytest.mark.django_db
def clear_musician_table():
    seeder = Seeder.SQLiteSeed()
    seeder.clear(Model)
