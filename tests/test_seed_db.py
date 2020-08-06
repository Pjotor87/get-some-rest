"""Tests for seeding the database."""


import pytest
from djangoapp.models import Musician as Model
import testdata_helper as Seeder


@pytest.mark.django_db
class Test_Seed():
    """Should test seed functionality."""

    def test_should_seed_the_musician_table(self):
        Seeder.seed_musician_table()

        try:
            # Expected behaviour is to fail here and raise exception
            Model.objects.get(firstname="Non", lastname="Existing", band="Entry")
        except Model.DoesNotExist:
            pass
            assert Model.objects.get(firstname="Mike", lastname="Portnoy", band="Dream Theater") is not None, "Did not find A seeded entry that should exist"

    def test_should_clear_the_musician_table(self):
        Seeder.seed_musician_table()

        Seeder.clear_musician_table()

        try:
            # Expected behaviour is to fail here and raise exception
            assert Model.objects.get(firstname="Mike", lastname="Portnoy", band="Dream Theater") is not None, "Did not find A seeded entry that should exist"
        except Model.DoesNotExist:
            pass
