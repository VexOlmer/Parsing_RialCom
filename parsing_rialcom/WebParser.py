"""
    This module contains a class for parsing a website page.
"""


import requests

class WebParser:
    def __init__(self, url: str):
        self._url = url

    def get_page_content(self):
        response = requests.get(self._url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception("Error loading page.")

    @property
    def url(self):
        return self._url