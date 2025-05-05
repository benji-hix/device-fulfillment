# validators.py
from prompt_toolkit.validation import ValidationError, Validator
from pathlib import Path
from src.utils import clean

XLSX_EXT = '.xlsx' 

class WorkbookValidator(Validator):
    def __init__(self, dir_path: Path):
        self.dir_path = dir_path.expanduser().resolve()

    def validate(self, document):
        clean_str = clean(document.text)
        
        if not clean_str.endswith(XLSX_EXT):
            clean_str = document.text + XLSX_EXT

        file_path = self.dir_path / clean_str
        if not file_path.exists():
            raise ValidationError(
                message='File not found.', cursor_position=len(document.text)
            )


class PathValidator(Validator):
    def validate(self, document):
        clean_str = clean(document.text)
        user_path = Path(clean_str).expanduser().resolve()

        if not user_path.exists():
            raise ValidationError(message='Provided file or folder does not exist.')

        elif user_path.is_dir():
            if not any(file.suffix == XLSX_EXT for file in user_path.iterdir()):
                raise ValidationError(
                    message=f'Provided directory does not contain any {XLSX_EXT} files',
                    cursor_position=len(document.text),
                )

        elif user_path.is_file():
            if user_path.suffix != XLSX_EXT:
                raise ValidationError(
                    message=f'File is not an {XLSX_EXT} file',
                    cursor_position=len(document.text),
                )

        else:
            raise ValidationError(
                message=f'Path must be a directory or {XLSX_EXT} file',
                cursor_position=len(document.text),
            )


class SheetValidator(Validator):
    def __init__(self, sheet_names: list[str]):
        self.sheet_names = sheet_names

    def validate(self, document):
        clean_str = clean(document.text)

        if clean_str not in self.sheet_names:
            raise ValidationError(
                message='Worksheet not found.', cursor_position=len(document.text)
            )


class RowValidator(Validator):
    def __init__(self, total_rows: int):
        self.total_rows = total_rows

    def validate(self, document):
        if not document.text.isdigit():
            raise ValidationError(
                message='Input must be a viable row number.',
                cursor_position=len(document.text),
            )

        row = int(document.text)

        if row not in range(2, self.total_rows + 1):
            raise ValidationError(
                message='Row does not exist in worksheet.',
                cursor_position=len(document.text),
            )
