# path_manager.py
from src.interface.theme import rprint
from interface.parsers import parse_user_path, parse_user_file
from pathlib import Path


class PathManager:
    def __init__(self):
        self.file_str: None
        self.select_path()

    def __str__(self):
        return self.file_str

    def select_path(self):
        input_path = parse_user_path()
        if input_path.is_file():
            self.file_str = str(input_path)
        elif input_path.is_dir():
            self.file_str = str(self.select_file(input_path))
        return self

    def select_file(self, dir_path: Path):
        def print_dir_files(dir: Path) -> None:
            dir_files = [
                f
                for f in dir.iterdir()
                if f.is_file() and f.suffix == '.xlsx' and not f.name.startswith('~$')
            ]
            for f in dir_files:
                print(f'|  {f.name}')
            return None

        rprint('Files found:')
        print_dir_files(dir_path)
        input_file = parse_user_file(dir_path)
        if input_file.suffix != '.xlsx':
            input_file = input_file.with_suffix('.xlsx')
        return input_file
