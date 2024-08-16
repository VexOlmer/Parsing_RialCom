"""
    This module contains a class for handling parsing data.
"""

from bs4 import BeautifulSoup
import re

from parsing_rialcom.InternetTariff import InternetTariff

class DataExtractor:
    """
        This class is responsible for extracting data about Internet tariffs from an HTML page.

        Attributes:
            _soup (BeautifulSoup): The BeautifulSoup object used for parsing HTML content.

        Methods:
            find_info_simple_tariff(): Extracts information about simple internet tariffs
                                        for apartment and private houses.
            find_info_sectional_tariff(): Extracts information about sectional internet tariffs
                                            for apartment and private houses.
            soup(): Returns the BeautifulSoup object used for parsing HTML content.
    """

    def __init__(self, html_content):
        self._soup = BeautifulSoup(html_content, 'html.parser')

    def find_info_simple_tariff(self):
        """
            Obtaining data on simple internet tariffs and dividing them into apartment buildings and private houses

            Return:
                simple_tariff: A dictionary containing two lists: 'apartment_house' and 'private_house'.
                                Each list contains InternetTariff objects.
        """

        tables_tariff = self._soup.find_all('table',
                                            class_='table table-sm table-striped table-borderless table-responsive-sm')

        simple_tariff = {
            'apartment_house': [],
            'private_house': []
        }
        is_appartment_house = True

        # We don't need the last table
        for table in tables_tariff[:2]:
            tariffs_info = []
            rows = table.find_all('tr')[1:]     # Skipping the table header

            for row in rows:
                clear_row = row.text.strip().split('\n')
                speed = int(re.search(r'\b\d+\b', clear_row[3]).group())
                price = int(re.search(r'\b\d+\b', clear_row[1]).group())

                tariffs_info.append(InternetTariff(clear_row[0], 'null', speed // 1000, price))

            if is_appartment_house:
                simple_tariff['apartment_house'] = tariffs_info
                is_appartment_house = False
            else:
                simple_tariff['private_house'] = tariffs_info

        return simple_tariff

    def find_info_sectional_tariff(self):
        """
            Extracts information about sectional internet tariffs for apartment and private houses.

            Return:
                sectional_tariff: A dictionary containing two lists: 'apartment_house' and 'private_house'.
                        Each list contains InternetTariff objects.
        """

        tables_tariff = self._soup.find_all('table',
                                            class_='table table-sm table-striped table-borderless table-responsive')

        sectional_tariff = {
            'apartment_house': [],
            'private_house': []
        }
        is_appartment_house = True
        AMOUNT_APARTMENT_TV = 4     # Used to access the corresponding tariff from an apartment building
                                    #   due to the different number of columns

        for table in tables_tariff:
            tariffs_info = []
            rows = table.find_all('tr')

            # Get the name and speed of the tariff from the column for convenient interaction with them
            names_interactive_tv = rows[0].text.strip().split('\n')
            speed_interactive_tv = [int(re.search(r'\b\d+\b', name).group()) for name in names_interactive_tv]

            # For convenient separation of private and apartment buildings we will add a suffix '_ч'
            if not is_appartment_house:
                names_interactive_tv = [elem + '_ч' for elem in names_interactive_tv]

            for i, row in enumerate(rows[1:]):
                clear_row = row.text.strip().split('\n')
                channel_re = re.search(r'\b\d+\b', clear_row[0])

                # For private houses the number of channels is not specified
                if channel_re is None:
                    channel = sectional_tariff['apartment_house'][i * AMOUNT_APARTMENT_TV].channels
                else:
                    channel = int(channel_re.group())

                # For each line with a standard tariff there are additional tariffs indicated in the columns
                for j in range(len(names_interactive_tv)):
                    tariffs_info.append(InternetTariff(clear_row[0].split(' (')[0] + ' + ' + names_interactive_tv[j],
                                                       channel, speed_interactive_tv[j], int(clear_row[j + 1])))

            if is_appartment_house:
                sectional_tariff['apartment_house'] = tariffs_info
                is_appartment_house = False
            else:
                sectional_tariff['private_house'] = tariffs_info

        return sectional_tariff

    @property
    def soup(self):
        return self._soup