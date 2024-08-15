from bs4 import BeautifulSoup
import re

class DataExtractor:

    def __init__(self, html_content):
        #html_content = re.sub(r'>\s+<', '><', html_content.replace('\n', ''))
        self._soup = BeautifulSoup(html_content, 'html.parser')

    def find_info_simple_tariff(self):
        tables_tariff = self._soup.find_all('table',
                                            class_='table table-sm table-striped table-borderless table-responsive-sm')

        simple_tariff = {
            'apartment_house': [],
            'private_house': []
        }
        appartment_house = True

        for table in tables_tariff[:2]:
            tariffs_info = []
            rows = table.find_all('tr')

            for row in rows[1:]:
                clear_row = row.text.strip().split('\n')
                speed = int(re.search(r'\b\d+\b', clear_row[3]).group())
                price = int(re.search(r'\b\d+\b', clear_row[1]).group())

                tariffs_info.append([clear_row[0], 'null', speed // 1000, price])

            if appartment_house:
                simple_tariff['apartment_house'] = tariffs_info
                appartment_house = False
            else:
                simple_tariff['private_house'] = tariffs_info

        return simple_tariff

    def find_info_sectional_tariff(self):
        tables_tariff = self._soup.find_all('table',
                                            class_='table table-sm table-striped table-borderless table-responsive')

        sectional_tariff = {
            'apartment_house': [],
            'private_house': []
        }
        appartment_house = True

        for table in tables_tariff:
            tariffs_info = []
            rows = table.find_all('tr')

            names_interactive_tv = rows[0].text.strip().split('\n')
            speed_interactive_tv = []

            for name in names_interactive_tv:
                speed = re.search(r'\b\d+\b', name)
                speed_interactive_tv.append(int(speed.group()))

            if not appartment_house:
                names_interactive_tv = [elem + '_ч' for elem in names_interactive_tv]

            for i, row in enumerate(rows[1:]):
                clear_row = row.text.strip().split('\n')
                channel_re = re.search(r'\b\d+\b', clear_row[0])

                if channel_re is None:
                    channel = sectional_tariff['apartment_house'][i * len(names_interactive_tv)][1]
                else:
                    channel = int(channel_re.group())

                for j in range(len(names_interactive_tv)):
                    tariffs_info.append([clear_row[0].split(' (')[0] + ' + ' + names_interactive_tv[j], channel, speed_interactive_tv[j], int(clear_row[j + 1])])

            if appartment_house:
                sectional_tariff['apartment_house'] = tariffs_info
                appartment_house = False
            else:
                sectional_tariff['private_house'] = tariffs_info

        return sectional_tariff

    @property
    def soup(self):
        return self._soup