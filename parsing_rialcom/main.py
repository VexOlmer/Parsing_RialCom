from parsing_rialcom.WebParser import WebParser
from parsing_rialcom.DataExtractor import DataExtractor

if __name__ == "__main__":

    url = "https://www.rialcom.ru/internet_tariffs/"

    parser = WebParser(url)
    page_content = parser.get_page_content()

    extractor = DataExtractor(page_content)
    tariffs_data = extractor.extract_tariffs_data()