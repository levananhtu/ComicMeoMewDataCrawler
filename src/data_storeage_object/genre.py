class Genre:
    genre_id: int
    genre_name: str

    def __init__(self, genre_name, genre_id=None):
        """

        :type genre_id: int
        :type genre_name: str
        """
        self.genre_name = genre_name
        self.genre_id = genre_id
        pass

    pass
