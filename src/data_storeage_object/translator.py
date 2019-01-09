class Translator:
    translator_id: int
    translator_name: str

    def __init__(self, translator_name, translator_id=None):
        """

        :type translator_id: int
        :type translator_name: str
        """
        self.translator_name = translator_name
        self.translator_id = translator_id
        pass

    pass
