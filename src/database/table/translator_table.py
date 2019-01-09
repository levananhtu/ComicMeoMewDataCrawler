from database.accessor.database_accessor import DatabaseAccessor
from mysql.connector import errors
from data_storeage_object import Translator


class TranslatorTable:
    def __init__(self):
        self.accessor = DatabaseAccessor.get_accessor()
        pass

    def insert(self, translator):
        cursor = self.accessor.cursor()
        query = "INSERT INTO comic.translator(`TranslatorName`) VALUES (%s)"
        value = (translator.__getattribute__("translator_name"),)
        try:
            cursor.execute(query, value)
            self.accessor.commit()
            return cursor.getlastrowid()
            pass
        except errors.IntegrityError:
            return self.select(translator)
            pass
        pass

    def select(self, translator):
        cursor = self.accessor.cursor()
        query = "SELECT comic.translator.TranslatorID FROM comic.translator WHERE comic.translator.TranslatorName= %s"
        value = (translator.__getattribute__("translator_name"),)
        cursor.execute(query, value)
        return cursor.fetchone()[0]
        pass

    pass


if __name__ == '__main__':
    print(TranslatorTable().insert(Translator("phiêu lưu")))
    print(TranslatorTable().insert(Translator("kinh dị")))
    pass
