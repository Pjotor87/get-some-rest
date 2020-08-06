"""Tests for seeding the database."""


import pytest
import djangoapp.models as Models
import djangoapp.seed as Seeder


@pytest.mark.django_db
class Test_Seed():

    def test_should_find_import_of_model_without_crashing_when_running_from_root(self):
        """Should."""
        assert Seeder.SQLiteSeed is not None, "SQLiteSeed could not be found, should exist in seed.py"

    def test_should_seed_the_musician_table(self):
        """Should."""
        testdata_seed = [
            Models.Musician(firstname="James", lastname="Hetfield", band="Metallica"),
            Models.Musician(firstname="John", lastname="Petrucci", band="Dream Theater"),
            Models.Musician(firstname="Mike", lastname="Portnoy", band="Dream Theater"),
            Models.Musician(firstname="Dave", lastname="Mustaine", band="Megadeth"),
        ]
        seeder = Seeder.SQLiteSeed(testdata_seed)
        seeder.seed()

        try:
            # Expected behaviour is to fail here and raise exception
            Models.Musician.objects.get(firstname="Non", lastname="Existing", band="Entry")
        except Models.Musician.DoesNotExist:
            pass
            assert Models.Musician.objects.get(firstname="Mike", lastname="Portnoy", band="Dream Theater") is not None, "Did not find A seeded entry that should exist"
