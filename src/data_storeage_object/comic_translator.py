class ComicTranslator:
    translator_id: int
    comic_id: int
    comic_translator_id: int

    def __init__(self, comic_id, translator_id, comic_translator_id=None):
        """

        :type comic_id: int
        :type translator_id: int
        :type comic_translator_id: int
        """
        self.comic_translator_id = comic_translator_id
        self.comic_id = comic_id
        self.translator_id = translator_id
        pass

    pass
