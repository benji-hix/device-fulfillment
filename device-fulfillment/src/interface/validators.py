from prompt_toolkit.validation import ValidationError, Validator
from pathlib import Path


class DirectoryValidator(Validator):
    def validate(self, document):
        dir_path = Path(document.text)

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
        self.dir_path = dir_path

    def validate(self, document):
        file_str = document.text
        if not file_str.endswith('.xlsx'):
            file_str = document.text + '.xlsx'

        file_path = self.dir_path / file_str
        if not file_path.exists():
            raise ValidationError(
                message='File not found.', cursor_position=len(document.text)
            )
