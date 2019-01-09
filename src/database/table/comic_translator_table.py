from database.accessor.database_accessor import DatabaseAccessor
from data_storeage_object import ComicTranslator
# from mysql.connector import errors
from mysql.connector import MySQLConnection
import datetime


class ComicTranslatorTable:
    accessor: MySQLConnection

    def __init__(self):
        self.accessor = DatabaseAccessor.get_accessor()
        pass

    def insert(self, comic_translator):
        """

        :type comic_translator: ComicTranslator
        """
        query = "INSERT INTO comic.comic_translator(TranslatorID, `ComicID`) VALUES (%s,%s)"
        value = (comic_translator.__getattribute__("translator_id"), comic_translator.__getattribute__("comic_id"),)
        cursor = self.accessor.cursor()
        cursor.execute(query, value)
        self.accessor.commit()
        return cursor.getlastrowid()
        pass

    pass


if __name__ == '__main__':
    print(ComicTranslatorTable().insert(ComicTranslator(1, 1)))
    pass
