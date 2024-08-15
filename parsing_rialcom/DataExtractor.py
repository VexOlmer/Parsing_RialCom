from bs4 import BeautifulSoup

class DataExtractor:

    def __init__(self, html_content):
        self.soup = BeautifulSoup(html_content, 'html.parser')

    def extract_tariffs_data(self):
        tariff = []
        tariff_element = self.soup.find_all('tr')

        return tariff