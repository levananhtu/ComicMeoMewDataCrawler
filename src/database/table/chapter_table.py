from database.accessor.database_accessor import DatabaseAccessor
from data_storeage_object import Chapter
from mysql.connector import MySQLConnection


class ChapterTable:
    accessor: MySQLConnection

    def __init__(self):
        self.accessor = DatabaseAccessor.get_accessor()
        pass

    def insert(self, chapter):
        """

        :type chapter: Chapter
        """
        cursor = self.accessor.cursor()
        query = "INSERT INTO comic.chapter(`ComicID`, `PreviousChapter`, " \
                "`SubmitDate`, `ChapterName`) " \
                "VALUES (%s, %s, " \
                "%s, %s)"
        value = (chapter.__getattribute__("comic_id"), chapter.__getattribute__("previous_chapter"),
                 chapter.__getattribute__("submit_date"), chapter.__getattribute__("chapter_name"),)
        cursor.execute(query, value)
        self.accessor.commit()
        return cursor.getlastrowid()
        pass

    pass


if __name__ == '__main__':
    print(ChapterTable().insert(Chapter("adsfadf", 20, 5)))
    pass
