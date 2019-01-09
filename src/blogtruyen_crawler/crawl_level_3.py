import requests
from bs4 import BeautifulSoup
from blogtruyen_crawler.crawl_level_2 import CrawlLevel2
from database import ComicDatabase
import traceback
from bs4 import BeautifulSoup


class CrawlLevel3:
    def __init__(self):
        pass

    def crawl(self, thread_no=0, thread_count=1):
        self._crawl_level_3(thread_no=thread_no, thread_count=thread_count)
        pass

    def _crawl_level_3(self, thread_no=0, thread_count=1):
        """

        :type thread_count: int
        :type thread_no: int
        """
        href_list = list("asdf")
        page = 113 + thread_no
        comic = 1
        while len(href_list) != 0:
            href_list = self._get_link(page)
            for href in href_list:
                try:
                    data = CrawlLevel2().crawl("https://blogtruyen.com" + href)
                    pass
                except Exception:
                    print(str(page) + " - " + str(comic) + ".... data error")
                    traceback.print_exc()
                    comic += 1
                    continue
                    pass

                try:
                    ComicDatabase().insert_data(data)
                    pass
                except Exception:
                    print(str(page) + " - " + str(comic) + ".... database error")
                    traceback.print_exc()
                    comic += 1
                    continue
                    pass

                print(str(page) + " - " + str(comic) + ".... zero error occurred")
                comic += 1
                pass
            page += thread_count
            pass
        pass

    @staticmethod
    def _get_link(page):
        """

        :rtype: list
        :type page: int
        """
        api_url = 'https://blogtruyen.com/ajax/Search/AjaxLoadListManga'

        data = {
            "key": "tatca",
            "orderBy": "2",
            "p": page
        }
        response = requests.post(api_url, data=data)
        soup = BeautifulSoup(response.content, "html.parser")
        title_list = soup \
            .find("div", class_="list") \
            .find_all("p", class_="")
        href_list = list()
        for title in title_list:
            href_list.append(str(title.span.a.get("href")).strip())
            pass
        return href_list
        # body > div.list > p:nth-child(2) > span.tiptip.fs-12.ellipsis > a
        pass

    pass


if __name__ == "__main__":
    print(CrawlLevel3().crawl())
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    pass
