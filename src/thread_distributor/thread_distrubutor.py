import threading
from blogtruyen_crawler import CrawlLevel3


class CrawlerThread(threading.Thread):
    thread_count: int
    thread_id: int

    def run(self):
        super().run()
        CrawlLevel3().crawl(self.thread_id, self.thread_count)
        pass

    def __init__(self, thread_id, thread_count):
        """

        :type thread_count: int
        :type thread_id: int
        """
        super().__init__()
        self.thread_count = thread_count
        self.thread_id = thread_id

    pass
