"""Tests for seeding the database."""


import pytest
from djangoapp.models import Musician as Model
import djangoapp.seed as Seeder


@pytest.mark.django_db
class Test_Seed():
    """Should test seed functionality."""

    def test_should_find_import_of_model_without_crashing_when_running_from_root(self):
        assert Seeder.SQLiteSeed is not None, "SQLiteSeed could not be found, should exist in seed.py"

    def test_should_seed_the_musician_table(self):
        testdata_seed = [
            Model(firstname="James", lastname="Hetfield", band="Metallica"),
            Model(firstname="John", lastname="Petrucci", band="Dream Theater"),
            Model(firstname="Mike", lastname="Portnoy", band="Dream Theater"),
            Model(firstname="Dave", lastname="Mustaine", band="Megadeth"),
        ]
        seeder = Seeder.SQLiteSeed(testdata_seed)
        seeder.seed()

        try:
            # Expected behaviour is to fail here and raise exception
            Model.objects.get(firstname="Non", lastname="Existing", band="Entry")
        except Model.DoesNotExist:
            pass
            assert Model.objects.get(firstname="Mike", lastname="Portnoy", band="Dream Theater") is not None, "Did not find A seeded entry that should exist"
