from prompt_toolkit.validation import ValidationError, Validator
from pathlib import Path


class DirectoryValidator(Validator):
    def validate(self, document):
        dir_path = Path(document.text)

        if not dir_path.exists():
            # rprint('\nProvided directory does not exist', style='error')
            raise ValidationError(
                message="Provided directory does not exist.",
                cursor_position=len(document.text),
            )

        if not dir_path.is_dir():
            # rprint('\nProvided path is not a directory', style='error')
            raise ValidationError(
                message=("Provided path is not a directory"),
                cursor_position=len(document.text),
            )

        if not any(file.suffix == ".xlsx" for file in dir_path.iterdir()):
            # rprint('\nProvided directory does not contain any .xlsx files', style='error')
            raise ValidationError(
                message=("Provided directory does not contain any .xslx files"),
                cursor_position=len(document.text),
            )
