from parsing_rialcom.WebParser import WebParser
from parsing_rialcom.DataExtractor import DataExtractor

if __name__ == "__main__":

    url = "https://www.rialcom.ru/internet_tariffs/"

    parser = WebParser(url)
    page_content = parser.get_page_content()

    extractor = DataExtractor(page_content)
    tariffs_data = extractor.find_info_sectional_tariff()

    # for tariff in tariffs_data:
    #     print(tariff, end='\n' * 2)

    print('\n\n')
    for key, value in tariffs_data.items():
        print(key)
        for elem in value:
            print(elem)
        print('\n\n')

    print(tariffs_data)

    #print(extractor.soup)