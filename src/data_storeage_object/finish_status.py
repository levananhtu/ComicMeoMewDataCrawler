class FinishStatus:
    finish_status_id: int
    finish_status_name: str

    def __init__(self, finish_status_name, finish_status_id=None):
        """

        :type finish_status_id: int
        :type finish_status_name: str
        """
        self.finish_status_name = finish_status_name
        self.finish_status_id = finish_status_id
        pass

    pass
