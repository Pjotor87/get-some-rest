"""Tests for seeding the database."""


import pytest
from djangoapp.models import Musician as Model
import testdata_helper as Seeder


@pytest.mark.django_db
class Test_Musician():
    """Should test musician model."""

    def test_should_serialize_musician_entries_for_api_exposure(self):
        pass
