from thread_distributor import CrawlerThread
from blogtruyen_crawler import CrawlLevel3

# if __name__ == '__main__':
#     threads = []
#     n = 3
#     for i in range(0, n):
#         threads.append(CrawlerThread(i, n))
#         pass
#
#     for thread in threads:
#         thread.start()
#         pass
#
#     for thread in threads:
#         thread.join()
#         pass
#
#     pass

if __name__ == '__main__':
    CrawlLevel3().crawl()
    pass
