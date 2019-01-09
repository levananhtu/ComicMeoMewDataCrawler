class ComicAuthor:
    author_id: int
    comic_id: int
    comic_author_id: int

    def __init__(self, comic_id, author_id, comic_author_id=None):
        """

        :type comic_author_id: int
        :type author_id: int
        :type comic_id: int
        """
        self.comic_author_id = comic_author_id
        self.comic_id = comic_id
        self.author_id = author_id
        pass

    pass
