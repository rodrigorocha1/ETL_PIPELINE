import requests
from typing import Dict


class HttpRequester:

    def __init__(self) -> None:
        self.__url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'

    def request_from_page(self) -> Dict[int, str]:
        reponse = requests.get(self.__url)
        return {
            'status_code': reponse.status_code,
            'html': reponse.text
        }


