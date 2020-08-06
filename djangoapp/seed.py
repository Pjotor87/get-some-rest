"""Seeds the database with testdata."""


from logzero import logger
from djangoapp.models import Musician


class SQLiteSeed():
    """Class for seeding an SQLite database."""

    def __init__(self, model_list=[]):
        self.model_list = model_list

    def clear(self, model):
        """Will deletes all the table data."""
        logger.debug("Delete instances")
        model.objects.all().delete()

    def seed(self):
        """Seeds the model_list property content into the db."""
        for entry in self.model_list:
            logger.debug(entry)
            entry.save()
            logger.info("{} entry created.".format(entry))


def ensure_base_seed(clear=False):
    base_seed = [
        Musician(firstname="James", lastname="Hetfield", band="Metallica"),
        Musician(firstname="John", lastname="Petrucci", band="Dream Theater"),
        Musician(firstname="Mike", lastname="Portnoy", band="Dream Theater"),
        Musician(firstname="Dave", lastname="Mustaine", band="Megadeth"),
    ]
    seeder = SQLiteSeed(base_seed)
    if clear is True:
        seeder.clear(Musician)
    seeder.seed()
