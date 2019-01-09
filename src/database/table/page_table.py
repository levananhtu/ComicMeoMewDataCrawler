from database.accessor.database_accessor import DatabaseAccessor
from data_storeage_object import Page
from mysql.connector import MySQLConnection


class PageTable:
    accessor: MySQLConnection

    def __init__(self):
        self.accessor = DatabaseAccessor.get_accessor()
        pass

    def insert(self, page):
        """

        :type page: Page
        """
        cursor = self.accessor.cursor()
        query = "INSERT INTO comic.page(ChapterID, PreviousPage, " \
                "PageURL) " \
                "VALUES (%s, %s, " \
                "%s)"
        value = (page.__getattribute__("chapter_id"), page.__getattribute__("previous_page"),
                 page.__getattribute__("page_url"),)
        cursor.execute(query, value)
        self.accessor.commit()
        return cursor.getlastrowid()
        pass

    pass


if __name__ == '__main__':
    print(PageTable().insert(Page(12, "adsfasdf", 20)))
    pass
