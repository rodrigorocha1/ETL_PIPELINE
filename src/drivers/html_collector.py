from bs4 import BeautifulSoup
from typing import List, Dict


class HtmlColector:

    @classmethod
    def collect_essential_information(cls, html: str) -> List[Dict[str, str]]:

        soup = BeautifulSoup(html, 'html.parser')
        artist_name_list = soup.find(class_='BodyText')
        artist_name_list_itens = artist_name_list.find_all('a')

        essential_information = []
        for artist_name in artist_name_list_itens:
            names = artist_name_list.contents[0]
            links = 'http://web.archive.org' + artist_name.get('href')
            essential_information.append({
                'name': names,
                'link': links
            })

        return essential_information
