from database.accessor.database_accessor import DatabaseAccessor
from data_storeage_object import ComicGenre
# from mysql.connector import errors
from mysql.connector import MySQLConnection
import datetime


class ComicAuthorTable:
    accessor: MySQLConnection

    def __init__(self):
        self.accessor = DatabaseAccessor.get_accessor()
        pass

    def insert(self, comic_author):
        """

        :type comic_author: ComicAuthor
        """
        query = "INSERT INTO comic.comic_author(`AuthorID`, `ComicID`) VALUES (%s,%s)"
        value = (comic_author.__getattribute__("author_id"), comic_author.__getattribute__("comic_id"),)
        cursor = self.accessor.cursor()
        cursor.execute(query, value)
        self.accessor.commit()
        return cursor.getlastrowid()
        pass

    pass


if __name__ == '__main__':
    print(ComicAuthorTable().insert(ComicGenre(1, 1)))
    pass
