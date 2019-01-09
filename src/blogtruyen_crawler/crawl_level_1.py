from bs4 import BeautifulSoup
import requests


class CrawlLevel1:

    def __init__(self):
        pass

    def crawl(self, link):
        """

        :type link: str
        :rtype: list
        """
        return self._crawl_level_1(link)
        pass

    @staticmethod
    def _crawl_level_1(link):
        """

        :rtype: list
        :type link: str
        """
        response = requests.get(link)
        soup = BeautifulSoup(response.__getattribute__("content"), "html.parser")
        pages = soup.find("article", id="content").find_all("img")
        result = list()
        for page in pages:
            result.append(page.get("src"))
            pass
        return result
        pass

    pass


if __name__ == '__main__':
    result_list = CrawlLevel1().crawl("https://blogtruyen.com/c332027/kaifuku-jutsushi-no-yarinaoshi-17481-chap-121")
    print(result_list)
