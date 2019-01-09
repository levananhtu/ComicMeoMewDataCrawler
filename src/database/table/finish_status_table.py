from database.accessor.database_accessor import DatabaseAccessor
from data_storeage_object import FinishStatus
from mysql.connector import errors


class FinishStatusTable:
    def __init__(self):
        self.accessor = DatabaseAccessor.get_accessor()
        pass

    def insert(self, finish_status):
        """

        :type finish_status: FinishStatus
        """
        cursor = self.accessor.cursor()
        query = "INSERT INTO comic.finish_status(`FinishStatusName`) VALUES (%s)"
        value = (finish_status.__getattribute__("finish_status_name"),)
        try:
            cursor.execute(query, value,)
            self.accessor.commit()
            return cursor.getlastrowid()
            pass
        except errors.IntegrityError:
            return self.select(finish_status)
            pass
        pass

    def select(self, finish_status):
        cursor = self.accessor.cursor()
        query = "SELECT comic.finish_status.FinishStatusID FROM comic.finish_status WHERE comic.finish_status.FinishStatusName= %s"
        value = (finish_status.__getattribute__("finish_status_name"),)
        cursor.execute(query, value)
        return cursor.fetchone()[0]
        pass

    pass


if __name__ == '__main__':
    print(FinishStatusTable().insert(FinishStatus("hoạt hình")))
    print(FinishStatusTable().insert(FinishStatus("kinh dị")))
    pass
