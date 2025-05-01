# validators.py
from prompt_toolkit.validation import ValidationError, Validator
from pathlib import Path
from src.utils import clean


class DirectoryValidator(Validator):
    def validate(self, document):
        clean_str = clean(document.text)
        dir_path = Path(clean_str).expanduser().resolve()

        if not dir_path.exists():
            raise ValidationError(
                message='Provided directory does not exist.',
                cursor_position=len(document.text),
            )

        if not dir_path.is_dir():
            raise ValidationError(
                message=('Provided path is not a directory'),
                cursor_position=len(document.text),
            )

        if not any(file.suffix == '.xlsx' for file in dir_path.iterdir()):
            raise ValidationError(
                message='Provided directory does not contain any .xlsx files',
                cursor_position=len(document.text),
            )


class FileValidator(Validator):
    def __init__(self, dir_path: Path):
        self.dir_path = dir_path.expanduser().resolve()

    def validate(self, document):
        clean_str = clean(document.text)
        if not clean_str.endswith('.xlsx'):
            clean_str = document.text + '.xlsx'

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
            if not any(file.suffix == '.xlsx' for file in user_path.iterdir()):
                raise ValidationError(
                    message='Provided directory does not contain any .xlsx files',
                    cursor_position=len(document.text),
                )

        elif user_path.is_file():
            if user_path.suffix != '.xlsx':
                raise ValidationError(
                    message='File is not an .xlsx file',
                    cursor_position=len(document.text),
                )

        else:
            raise ValidationError(
                message='Path must be a directory or .xlsx file',
                cursor_position=len(document.text),
            )
