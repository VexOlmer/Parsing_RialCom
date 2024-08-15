import pandas as pd
import os

class ExcelTable:
    def __init__(self, filename, headers, output_dir='../samples'):
        self._filename = filename
        self.df = pd.DataFrame(columns=headers)

        self._output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def update_table(self, data):
        self.df = pd.concat([self.df, pd.DataFrame(data, columns=self.df.columns)], ignore_index=True)

    def save_table(self):
        full_path = os.path.join(self._output_dir, self._filename)
        self.df.to_excel(full_path, index=False)