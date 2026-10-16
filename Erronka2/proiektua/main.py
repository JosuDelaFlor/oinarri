from pathlib import Path
from datetime import datetime

from helper.csv_helper import CSVHelper
from model.ordenagailua_dto import OrdenagailuaDto

def main():
    file_path_csv_read = Path(__file__).parent / "data" / "ordenagailuak.csv"
    file_path_csv_write = Path(__file__).parent / "data" / "ordenagailuak_berrial.csv"
    
    read_data_from_csv(file_path_csv_read)

    ordenagailuak: list[OrdenagailuaDto] = [
        OrdenagailuaDto(1, "192.168.1.1", "Linux", datetime.now(), datetime.now(), "Oharra 1"),
        OrdenagailuaDto(2, "192.168.1.2", "Windows", datetime.now(), datetime.now(), "Oharra 2"),
    ]

    rows: list[list[object]] = [
        [
            ordenagailua.id,
            ordenagailua.ip_elbidea,
            ordenagailua.sistema_eragilea,
            ordenagailua.erosketa_data.isoformat(),
            ordenagailua.azken_errebisioa.isoformat(),
            ordenagailua.oharrak,
        ]
        for ordenagailua in ordenagailuak
    ]
    write_data_to_csv(file_path_csv_write, rows)

def read_data_from_csv(file_path: str | Path) -> None:
    data: list[list[str]] = CSVHelper.read_csv(str(file_path))
    for row in data:
        print(row)

def write_data_to_csv(file_path: str | Path, data: list[list[object]]) -> None:
    success: bool = CSVHelper.write_csv(str(file_path), data)
    if success:
        print(f"Ok csv write: {file_path}")
    else:
        print(f"Kk csv write: {file_path}")

if __name__ == "__main__":
    main()