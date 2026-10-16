import csv
from pathlib import Path

from typing import Iterable

class CSVHelper:
    
    @staticmethod
    def read_csv(file_path: str) -> Iterable[list[str]]:
        with open(file_path, 'r', newline='') as csv_file:
            reader: csv.reader = csv.reader(csv_file, delimiter=',', quotechar='|')

            return list(reader)

    @staticmethod
    def write_csv(file_path: str, data: Iterable[Iterable[object]]) -> bool:
        output_path = Path(file_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with output_path.open('w', newline='') as csv_file:
            writer: csv.writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerows(data)
            
            return True