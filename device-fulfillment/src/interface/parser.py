from prompt_toolkit import prompt
from .theme import rprint
from pathlib import Path
from .validators import DirectoryValidator, FileValidator


def input_dir(input_message='Please enter directory path.'):
    try:
        rprint(input_message)
        user_dir = prompt(validator=DirectoryValidator(), validate_while_typing=True)
        return Path(user_dir).resolve()
    except Exception as error:
        rprint(f'Unexpected error: {error}', style='error')


def input_file(dir_path: Path, input_message='Please enter file name.'):
    try:
        rprint(input_message)
        file_str = prompt(validator=FileValidator(dir_path), validate_while_typing=True)
        file_path = dir_path / file_str
        return file_path.resolve()
    except Exception as error:
        rprint(f'Unexpected error: {error}', style='error')


def parse_sheet():
    pass


def parse_row():
    pass
