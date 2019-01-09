from database.accessor.database_accessor import DatabaseAccessor
from data_storeage_object import Comic
# from mysql.connector import errors
from mysql.connector import MySQLConnection
import datetime


class ComicTable:
    accessor: MySQLConnection

    def __init__(self):
        self.accessor = DatabaseAccessor.get_accessor()
        pass

    def insert(self, comic):
        """

        :type comic: Comic
        """
        query = "INSERT INTO comic.comic(`FinishStatusID`, `ComicName`, " \
                "`CreatedDate`, `Description`, " \
                "`Rate`, `View`, `Thumbnail`)" \
                "VALUES (%s, %s, " \
                "%s, %s, " \
                "%s, %s, %s)"
        value = (comic.__getattribute__("finish_status_id"), comic.__getattribute__("comic_name"),
                 comic.__getattribute__("created_date"), comic.__getattribute__("description"),
                 comic.__getattribute__("rate"), comic.__getattribute__("view"), comic.__getattribute__("thumbnail"),)
        cursor = self.accessor.cursor()
        cursor.execute(query, value)
        self.accessor.commit()
        return cursor.getlastrowid()
        pass

    pass


if __name__ == '__main__':
    print(ComicTable().insert(Comic("im a cat", datetime.datetime(2018, 6, 4), "hahaha", 5, 5, 1, "adsfasdf")))
    pass
