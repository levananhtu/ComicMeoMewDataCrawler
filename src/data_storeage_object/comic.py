from datetime import datetime


class Comic:
    comic_id: int
    thumbnail: str
    finish_status_id: int
    view: int
    rate: int
    description: str
    created_date: datetime
    comic_name: str

    def __init__(self, comic_name, finish_status_id, thumbnail, description, created_date=datetime.now(), rate=0,
                 view=0, comic_id=None):
        """

        :type view: int
        :type finish_status_id: int
        :type rate: int
        :type created_date: datetime
        :type comic_id: int
        :type thumbnail: str
        :type description: str
        :type comic_name: str
        """

        self.comic_name = comic_name
        self.created_date = created_date
        self.description = description
        self.rate = rate
        self.view = view
        self.finish_status_id = finish_status_id
        self.thumbnail = thumbnail
        self.comic_id = comic_id
        pass

    pass
