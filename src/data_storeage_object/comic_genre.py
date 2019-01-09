class ComicGenre:
    genre_id: int
    comic_id: int
    comic_genre_id: int

    def __init__(self, comic_id, genre_id, comic_genre_id=None):
        """

        :type comic_genre_id: int
        :type genre_id: int
        :type comic_id: int
        """
        self.comic_genre_id = comic_genre_id
        self.comic_id = comic_id
        self.genre_id = genre_id
        pass

    pass
