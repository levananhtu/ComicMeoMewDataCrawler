class Page:
    previous_page: int
    page_url: str
    chapter_id: int
    page_id: int

    def __init__(self, chapter_id, page_url, previous_page, page_id=None):
        """

        :type page_id: int
        :type previous_page: int
        :type page_url: str
        :type chapter_id: int
        """
        self.page_id = page_id
        self.chapter_id = chapter_id
        self.page_url = page_url
        self.previous_page = previous_page
        pass

    pass
