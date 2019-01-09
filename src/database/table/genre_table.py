from database.accessor.database_accessor import DatabaseAccessor
from data_storeage_object import Genre
from mysql.connector import errors


class GenreTable:
    def __init__(self):
        self.accessor = DatabaseAccessor.get_accessor()
        pass

    def insert(self, genre):
        cursor = self.accessor.cursor()
        query = "INSERT INTO comic.genre(`GenreName`) VALUES (%s)"
        value = (genre.__getattribute__("genre_name"),)
        try:
            cursor.execute(query, value)
            self.accessor.commit()
            return cursor.getlastrowid()
            pass
        except errors.IntegrityError:
            return self.select(genre)
            pass
        pass

    def select(self, genre):
        cursor = self.accessor.cursor()
        query = "SELECT comic.genre.GenreID FROM comic.genre WHERE comic.genre.GenreName= %s"
        value = (genre.__getattribute__("genre_name"),)
        cursor.execute(query, value)
        return cursor.fetchone()[0]
        pass

    pass


if __name__ == '__main__':
    print(GenreTable().insert(Genre("hoạt hình")))
    print(GenreTable().insert(Genre("kinh dị")))
    pass
