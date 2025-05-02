from dataclasses import dataclass
from src.interface.theme import rprint
from src.interface.parsers import parse_user_sheet, parse_user_row
from pathlib import Path
from pandas import DataFrame


class DataManager:
    def __init__(self, wkbk_path: Path):
        self.wkbk_path = wkbk_path
        self.wkbk_stem = wkbk_path.stem
        self.dataframe: DataFrame = None
        self.row = None
        self._load_sheet()

    def _load_sheet(self):
        rprint(f'Loading {self.wkbk_stem}...')
        self.dataframe = parse_user_sheet(self.wkbk_path)

    def select_row(self):
        row_data = parse_user_row(self.dataframe)
        rprint(row_data)


@dataclass
class Row:
    pass
