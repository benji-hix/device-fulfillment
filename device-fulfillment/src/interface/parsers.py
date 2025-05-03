# parsers.py
from prompt_toolkit import prompt
from pathlib import Path
from .theme import rprint
from .validators import PathValidator, WorkbookValidator, SheetValidator, RowValidator
from src.utils import clean
import pandas as pd


def prompt_for_path(input_message='Please enter folder or file path.'):
    while True:
        try:
            rprint(input_message)
            selected_dir = prompt(validator=PathValidator(), validate_while_typing=True)
            selected_dir = clean(selected_dir)
            return Path(selected_dir).expanduser().resolve()
        except Exception as error:
            rprint(f'Unexpected error: {error}.', style='error')


def prompt_for_workbook(dir_path: Path, input_message='Please select a file.'):
    def print_avail_workbooks(found_files: list) -> None:
        rprint('\nExcel files found:')
        for ind, f in enumerate(found_files):
            rprint(f'{ind + 1}.  {f.name}')
        return None

    while True:
        try:
            dir_files = [
                f
                for f in dir_path.iterdir()
                if f.is_file() and f.suffix == '.xlsx' and not f.name.startswith('~$')
            ]
            print_avail_workbooks(dir_files)
            rprint(f'\n{input_message}')
            selected_workbook = prompt(
                validator=WorkbookValidator(dir_path), validate_while_typing=True
            )
            selected_workbook = clean(selected_workbook)
            # Feature: ability to select workbook based on index?
            workbook_path = dir_path / selected_workbook
            return workbook_path.expanduser().resolve()
        except Exception as error:
            rprint(f'Unexpected error: {error}.', style='error')


def prompt_for_sheet(
    wkbk_path: Path, input_message='Please select a sheet.'
) -> pd.DataFrame:
    def print_avail_sheets(found_sheets: list):
        rprint('\nWorksheets found:')
        for ind, s in enumerate(found_sheets):
            rprint(f'{ind + 1}.  {s}')
        return None

    while True:
        try:
            wkbk_str = str(wkbk_path)
            sheets = pd.ExcelFile(wkbk_str).sheet_names
            # rprint(f' Available worksheets: {sheets}.')

            if len(sheets) <= 1:
                return pd.read_excel(wkbk_str, sheets[0]), sheets[0]

            print_avail_sheets(sheets)
            rprint(f'\n{input_message}')
            selected_sheet = prompt(
                validator=SheetValidator(sheets), validate_while_typing=True
            )
            selected_sheet: str = clean(selected_sheet)
            # Feature: ability to select sheet via index?
            return pd.read_excel(wkbk_str, selected_sheet), selected_sheet
        except Exception as error:
            rprint(f'Unexpected error: {error}.', style='error')


def prompt_for_row(dataframe: pd.DataFrame, input_message='Please select a row.'):
    while True:
        try:
            total_rows = len(dataframe) + 1
            rprint(f'Total rows: {total_rows}')
            rprint(f'\n{input_message}')
            selected_row_str = prompt(
                validator=RowValidator(total_rows), validate_while_typing=True
            )
            selected_row = int(selected_row_str) - 2
            return dataframe.iloc[selected_row]
        except Exception as error:
            rprint(f'Unexpected error: {error}.', style='error')
