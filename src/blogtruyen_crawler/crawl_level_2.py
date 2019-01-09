import requests
from bs4 import BeautifulSoup
import bs4
from vietnamese_converter.vietnamese_converter import convert
from blogtruyen_crawler.crawl_level_1 import CrawlLevel1


class CrawlLevel2:

    def __init__(self):
        pass

    def crawl(self, link):
        """

        :rtype: dict
        :type link: str
        """
        return self._crawl_level_2(link)
        pass

    def _crawl_level_2(self, link):
        """

        :rtype: dict
        :type link: str
        """
        response = requests.post(link)
        soup = BeautifulSoup(response.content, "html.parser")
        soup.findChildren()
        comic_name = soup.find(id="breadcrumbs")
        main_section = soup.find(id="wrapper") \
            .find("section", class_="main-content") \
            .div \
            .find("div", class_="col-md-8") \
            .section
        thumbnail = main_section.find("div", class_="thumbnail") \
            .img
        description = main_section.find("div", class_="detail") \
            .find("div", class_="content")
        generic_information = main_section.find("div", class_="description")
        chapters = soup.find(id="list-chapters")

        information = self._get_generic_information(generic_information)
        result = self._get_chapters(chapters)
        chapters_link_list = result.get("chapters_link")
        chapters_name_list = result.get("chapters_name")

        chapter_page_list = list()
        for chapter_link in chapters_link_list:
            chapter_page_list.append(CrawlLevel1().crawl("https://blogtruyen.com" + chapter_link))
            pass

        # print(information)
        # print(chapters_link_list)
        # print(chapters_name_list)
        # print(self.get_comic_name(comic_name))
        # print(self.get_thumbnail(thumbnail))
        # print(self.get_description(description))
        # print(chapter_page_list)
        # print(chapters_dict)
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

        # comic_name: #breadcrumbs > span:nth-child(2)
        # thumbnail: #wrapper > section.main-content > div > div.col-md-8 > section > div.thumbnail > img
        # description: #wrapper > section.main-content > div > div.col-md-8 > section > div.detail > div.content
        # generic_information: #wrapper > section.main-content > div > div.col-md-8 > section > div.description
        # chapters: #list-chapters

        return dict(
            comicname=self._get_comic_name(comic_name),
            thumbnail=self._get_thumbnail(thumbnail),
            description=self._get_description(description),
            authors=information.get("tacgia"),
            translators=information.get("nhomdich"),
            genres=information.get("theloai"),
            finishstatus=information.get("trangthai")[0],
            chaptersname=chapters_name_list,
            chapterspage=chapter_page_list
        )
        pass

    @staticmethod
    def _get_comic_name(first_parameter):
        """

        :rtype: str
        :type first_parameter: BeautifulSoup
        """
        tag = first_parameter.find("span", class_="")
        if tag is not None:
            return str(tag.text).replace("Trang chủ >", "").strip()
            pass
        return None
        pass

    @staticmethod
    def _get_thumbnail(first_parameter):
        """

        :rtype: str
        :type first_parameter: BeautifulSoup
        """
        if first_parameter is not None:
            return first_parameter.get("src")
            pass
        return None
        pass

    @staticmethod
    def _get_description(first_parameter):
        """

        :rtype: str
        :type first_parameter: BeautifulSoup
        """
        if first_parameter is not None:
            return str(first_parameter.text).strip()
            pass
        return None
        pass

    @staticmethod
    def _get_chapters(first_parameter):
        """

        :rtype: dict
        :type first_parameter: BeautifulSoup
        """
        if first_parameter is not None:
            chapter_tags = first_parameter.find_all("p")
            if chapter_tags is not None:
                chapters_name = list()
                chapters_link = list()
                for chapter_tag in chapter_tags:
                    chapters_name.append(str(chapter_tag.find("span", class_="title").a.text).strip())
                    chapters_link.append(str(chapter_tag.find("span", class_="title").a.get("href")).strip())
                    pass
                result = dict(chapters_name=chapters_name, chapters_link=chapters_link)
                return result
                pass
            return None
            pass
        return None
        pass

    @staticmethod
    def _format_key(first_parameter):
        """

        :rtype: str
        :type first_parameter: str
        """
        return convert(str(first_parameter)).replace(":", "").replace(" ", "").lower()
        pass

    def _get_generic_information(self, first_parameter):
        """

        :rtype: dict
        :type first_parameter: BeautifulSoup
        """
        if first_parameter is not None:
            raw_information_lv1_list = first_parameter.find_all("p", class_="")
            result = dict()
            for raw_information_lv1 in raw_information_lv1_list:
                raw_information_lv2_list = raw_information_lv1.children
                key = ""
                value = list()
                for raw_information_lv2 in raw_information_lv2_list:
                    if (type(raw_information_lv2) is bs4.element.NavigableString) and (
                            str(raw_information_lv2).strip() is not ""):
                        # print("~~~~~~~")
                        key = self._format_key(raw_information_lv2.strip())
                        if key is not "":
                            result[key] = value
                            value.clear()
                            pass
                        pass
                    elif type(raw_information_lv2) is bs4.element.Tag:
                        value.append(str(raw_information_lv2.text).strip())
                        pass
                    pass
                result[key] = value
                pass
            return result
            pass
        return None
        pass


if __name__ == '__main__':
    print(CrawlLevel2().crawl("https://blogtruyen.com/9349/shingeki-no-kyojin-gaiden-kuinaki-sentaku-manga"))
