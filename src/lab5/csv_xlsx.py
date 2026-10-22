import csv
from pathlib import Path

from openpyxl import Workbook
from openpyxl.utils import get_column_letter

from .json_csv import proverka

CSV_PATH = 'data/samples/cities.csv'
CSV_TO_XL = 'data/out/xl_cities.xlsx'

def csv_xlsx(csv_path, xlsx_path):

    with proverka(csv_path, '.csv').open(newline="", encoding='utf-8') as f:
        rows = list(csv.reader(f))

    if not rows:
        raise ValueError('Пустой CSV')
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    for r in rows:
        ws.append(r)
    for i in range(len(rows[0])):
        width = max(8, *[len(r[i]) for r in rows if i < len(r)])
        ws.column_dimensions[get_column_letter(i+1)].width = width

    Path(xlsx_path).parent.mkdir(parents=True, exist_ok=True)
    wb.save(xlsx_path)

if __name__ == "__main__":
    csv_xlsx(CSV_PATH, CSV_TO_XL)

