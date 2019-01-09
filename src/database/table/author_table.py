from database.accessor.database_accessor import DatabaseAccessor
from data_storeage_object import Author
from mysql.connector import errors


class AuthorTable:
    def __init__(self):
        self.accessor = DatabaseAccessor.get_accessor()
        pass

    def insert(self, author):
        """

        :type author: Author
        """
        cursor = self.accessor.cursor()
        query = "INSERT INTO comic.author(`AuthorName`) VALUES (%s)"
        value = (author.__getattribute__("author_name"),)
        try:
            cursor.execute(query, value)
            self.accessor.commit()
            return cursor.getlastrowid()
            pass
        except errors.IntegrityError:
            return self.select(author)
            pass
        return author_id_list
        pass

    def select(self, author):
        cursor = self.accessor.cursor()
        query = "SELECT comic.author.AuthorID FROM comic.author WHERE comic.author.AuthorName= %s"
        value = (author.__getattribute__("author_name"),)
        cursor.execute(query, value)
        return cursor.fetchone()[0]
        pass

    pass


if __name__ == '__main__':
    print(AuthorTable().insert(Author("hoạt hình")))
    print(AuthorTable().insert(Author("kinh dị")))
    pass
