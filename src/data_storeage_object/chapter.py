from datetime import datetime


class Chapter:
    previous_chapter: int
    comic_id: int
    submit_date: datetime
    chapter_name: str
    chapter_id: int

    def __init__(self, chapter_name, comic_id, previous_chapter, submit_date=datetime.now(),
                 chapter_id=None):
        """

        :type chapter_id: int
        :type submit_date: datetime
        :type previous_chapter: int
        :type comic_id: int
        :type chapter_name: str
        """
        self.chapter_id = chapter_id
        self.chapter_name = chapter_name
        self.submit_date = submit_date
        self.comic_id = comic_id
        self.previous_chapter = previous_chapter
        pass

    pass
