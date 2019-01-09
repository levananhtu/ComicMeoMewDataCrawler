from mysql import connector


class DatabaseAccessor:
    _accessor: connector.connection.MySQLConnection = None

    @staticmethod
    def get_accessor() -> connector.MySQLConnection:
        if DatabaseAccessor._accessor is None:
            DatabaseAccessor()
        return DatabaseAccessor._accessor

    def __init__(self):
        if DatabaseAccessor._accessor is not None:
            raise Exception("This class is a singleton!")
        else:
            DatabaseAccessor._accessor = connector.connect(
                host="localhost",
                user="root",
                passwd="",
            )


if __name__ == '__main__':
    print(type(DatabaseAccessor.get_accessor()))
    pass
