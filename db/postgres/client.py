import logging
import psycopg2

logger = logging.getLogger(__name__)

class Client():

    def __init__(self, **kwargs):
        self.connection = psycopg2.connect(**kwargs)

    def select(self, statement):
        logger.debug("select: %s", statement)

        with self.connection.cursor() as cursor:
            cursor.execute(statement)
            return cursor.fetchall()

    def execute(self, statement):
        logger.debug("execute: %s", statement)

        with self.connection.cursor() as cursor:
            cursor.execute(statement)

        self.connection.commit()
