from dataclasses import dataclass
from datetime import datetime
from src.interface.theme import rprint
from src.interface.parsers import prompt_for_sheet, prompt_for_row
from pathlib import Path
from pandas import DataFrame, Series


class DataManager:
    def __init__(self):
        self.workbook_path: Path = None
        self.workbook_stem: str = None
        self.selected_sheet: DataFrame = None
        self.sheet_name: str = None
        self.selected_row: Series = None

    @classmethod
    def from_path(cls, input_path):
        instance = cls()
        instance.workbook_path = input_path
        instance.workbook_stem = input_path.stem
        instance._select_sheet()
        return instance

    def _select_sheet(self):
        rprint(f'Loading {self.workbook_stem}...')
        self.selected_sheet, self.sheet_name = prompt_for_sheet(self.workbook_path)
        return self

    def preview_sheet(self):
        rprint(f'\nPreview of worksheet [{self.sheet_name}]')
        rprint(f'{self.selected_sheet.head()}')
        return self

    def select_row(self):
        self.selected_row = prompt_for_row(self.selected_sheet)
        return self

    def confirm_cohort(self):
        rprint('Press enter to generate email with the following data:')
        rprint(self.selected_row['Cohort ID'])
        rprint('Confirm?')
        input()
        return self

    def to_cohort(self):
        return Cohort(
            start_date=self.selected_row['Start Date'],
            course_id=self.selected_row['Cohort ID'],
            network=self.selected_row['Network'],
            location=self.selected_row['Location'],
            enrollment=self.selected_row['Enrollment'],
            type=self.selected_row['Type'],
            instructor=self.selected_row['Instructor'],
        )


@dataclass
class Cohort:
    start_date: datetime
    course_id: str
    network: str
    location: str
    enrollment: int
    type: str
    instructor: str
