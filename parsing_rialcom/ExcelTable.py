"""
    This module contains a class for creating and filling an Excel table.
"""


import pandas as pd
import os

class ExcelTable:
    def __init__(self, filename: str, headers: list, output_dir='../samples'):
        """
            :param filename: The name of the Excel file to save.
            :param headers: The headers (columns) of the Excel table.
            :param output_dir: The directory where the Excel file will be saved.
        """

        self._filename = filename
        self._headers = headers
        self._df = pd.DataFrame(columns=headers)

        self._output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def update_table(self, data):
        """
            Adding new data to the table.

            :param data: List of objects each of which is represented as a class InternetTariff.
        """

        new_data = [tariff.get_list_view() for tariff in data]
        new_df = pd.DataFrame(new_data, columns=self._df.columns)

        self._df = pd.concat([self._df, new_df], ignore_index=True)

    def save_table(self):
        full_path = os.path.join(self._output_dir, self._filename)

        if self._df.empty:
            raise ValueError("DataFrame is empty. Add data before saving.")

        self._df.to_excel(full_path, index=False)
        print(f"Table saved successfully at: {full_path}")

    @property
    def filename(self):
        return self._filename

    @property
    def headers(self):
        return self._headers

    @property
    def df(self):
        return self._df

    @property
    def output_dir(self):
        return self._output_dir