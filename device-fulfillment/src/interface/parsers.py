# parsers.py
from prompt_toolkit import prompt
from pathlib import Path
from .theme import rprint
from .validators import PathValidator, FileValidator
from src.utils import clean


def parse_user_path(input_message='Please enter directory path.'):
    try:
        rprint(input_message)
        user_dir = prompt(validator=PathValidator(), validate_while_typing=True)
        user_dir = clean(user_dir)
        return Path(user_dir).expanduser().resolve()
    except Exception as error:
        rprint(f'Unexpected error: {error}', style='error')


def parse_user_file(dir_path: Path, input_message='Please select a file.'):
    try:
        rprint(input_message)
        file_str = prompt(validator=FileValidator(dir_path), validate_while_typing=True)
        file_str = clean(file_str)
        file_path = dir_path / file_str
        return file_path.expanduser().resolve()
    except Exception as error:
        rprint(f'Unexpected error: {error}', style='error')


def parse_user_sheet():
    pass


def parse_user_row():
    pass
