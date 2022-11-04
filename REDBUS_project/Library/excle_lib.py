import xlrd
from Library.config import Configuration

class ReadExcel:


    def read_locator(self, sheetname):

        wb = xlrd.open_workbook(Configuration.LOCATORS_PATH)
        ws = wb.sheet_by_name(sheetname)
        rows = ws.get_rows()
        header = next(rows)
        dict_1 = {}
        for row in rows:
            dict_1[row[0].value] = (row[1].value, row[2].value)
        return dict_1

