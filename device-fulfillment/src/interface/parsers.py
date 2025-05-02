# parsers.py
from prompt_toolkit import prompt
from pathlib import Path
from .theme import rprint
from .validators import PathValidator, FileValidator, SheetValidator, RowValidator
from src.utils import clean
import pandas as pd
from pandas import DataFrame


def parse_user_path(input_message='Please enter directory path.'):
    while True:
        try:
            rprint(input_message)
            user_dir = prompt(validator=PathValidator(), validate_while_typing=True)
            user_dir = clean(user_dir)
            return Path(user_dir).expanduser().resolve()
        except Exception as error:
            rprint(f'Unexpected error: {error}.', style='error')


def parse_user_wkbk(dir_path: Path, input_message='Please select a file.'):
    while True:
        try:
            rprint(input_message)
            wkbk_str = prompt(
                validator=FileValidator(dir_path), validate_while_typing=True
            )
            wkbk_str = clean(wkbk_str)
            wkbk_path = dir_path / wkbk_str
            return wkbk_path.expanduser().resolve()
        except Exception as error:
            rprint(f'Unexpected error: {error}.', style='error')


def parse_user_sheet(
    wkbk_path: Path, input_message='Please select a sheet.'
) -> DataFrame:
    while True:
        try:
            file_str = str(wkbk_path)
            sheets = pd.ExcelFile(file_str).sheet_names
            rprint(f'{sheets =}')

            if len(sheets) <= 1:
                return pd.read_excel(file_str, sheets[0])

            rprint(input_message)
            for sheet in sheets:
                rprint(f'  {sheet}')
            user_sheet = prompt(
                validator=SheetValidator(sheets), validate_while_typing=True
            )
            user_sheet = clean(user_sheet)
            return pd.read_excel(file_str, user_sheet)
        except Exception as error:
            rprint(f'Unpexcted error: {error}.', style='error')


def parse_user_row(dataframe: pd.DataFrame, input_message='Please select a row.'):
    while True:
        try:
            total_rows = len(dataframe) + 1
            rprint(f'Number of rows: {total_rows}')
            rprint(input_message)
            row_str = prompt(
                validator=RowValidator(total_rows), validate_while_typing=True
            )
            row_number = int(row_str) - 2
            return dataframe.iloc[row_number]
        except Exception as error:
            rprint(f'Unexpected error: {error}.', style='error')
