from database.accessor.database_accessor import DatabaseAccessor
from data_storeage_object import ComicGenre
from mysql.connector import MySQLConnection
# from mysql.connector import errors
import datetime


class ComicGenreTable:
    accessor: MySQLConnection

    def __init__(self):
        self.accessor = DatabaseAccessor.get_accessor()
        pass

    def insert(self, comic_genre):
        """

        :type comic_genre: ComicAuthor
        """
        query = "INSERT INTO comic.comic_genre(GenreID,ComicID) VALUES (%s,%s)"
        value = (comic_genre.__getattribute__("genre_id"), comic_genre.__getattribute__("comic_id"),)
        cursor = self.accessor.cursor()
        cursor.execute(query, value)
        self.accessor.commit()
        return cursor.getlastrowid()
        pass

    pass


if __name__ == '__main__':
    print(ComicGenreTable().insert(ComicGenre(1, 1)))
    pass
