"""Seeds the database with testdata."""


from logzero import logger


class SQLiteSeed():
    """Class for seeding an SQLite database."""

    def __init__(self, model_list):
        self.model_list = model_list

    def clear(model):
        """Will deletes all the table data."""
        logger.debug("Delete instances")
        model.objects.all().delete()

    def seed(self):
        """Seeds the model_list property content into the db."""
        for entry in self.model_list:
            logger.debug(entry)
            entry.save()
            logger.info("{} entry created.".format(entry))
