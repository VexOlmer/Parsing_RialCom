from parsing_rialcom.WebParser import WebParser
from parsing_rialcom.DataExtractor import DataExtractor
from parsing_rialcom.ExcelTable import ExcelTable

if __name__ == "__main__":

    url = "https://www.rialcom.ru/internet_tariffs/"

    parser = WebParser(url)
    page_content = parser.get_page_content()

    extractor = DataExtractor(page_content)

    simple_tariffs = extractor.find_info_simple_tariff()
    sectional_tariffs = extractor.find_info_sectional_tariff()

    headers = ["Название тарифа", "Количество каналов", "Скорость доступа", "Абонентная плата"]
    filename = "tariffs.xlsx"
    excel_table = ExcelTable(filename, headers, output_dir='../samples')

    excel_table.update_table(simple_tariffs['apartment_house'])
    excel_table.update_table(sectional_tariffs['apartment_house'])
    excel_table.update_table(simple_tariffs['private_house'])
    excel_table.update_table(sectional_tariffs['private_house'])

    excel_table.save_table()