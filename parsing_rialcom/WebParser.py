import requests

class WebParser:
    def __init__(self, url):
        self.url = url

    def get_page_content(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception("Error loading page.")