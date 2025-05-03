# path_manager.py
from src.interface.theme import rprint
from .parsers import prompt_for_path, prompt_for_workbook
from pathlib import Path


class PathManager:
    def __init__(self):
        self.path_obj: Path = None

    def __str__(self):
        return self.path_str

    @property
    def path(self):
        return self.path_obj.expanduser().resolve()

    @classmethod
    def from_prompt(cls):
        instance = cls()
        selected_path: Path = prompt_for_path()
        if selected_path.is_file():
            instance.path_obj = selected_path
        elif selected_path.is_dir():
            instance.path_obj = instance.select_workbook(selected_path)
        return instance

    def _select_path(self):
        input_path = prompt_for_path()
        if input_path.is_file():
            self.path_obj = input_path
        elif input_path.is_dir():
            self.path_obj = self.select_workbook(input_path)
        return self

    def select_workbook(self, dir_path: Path):
        rprint(f'Loading folder \\{dir_path.name}...')
        selected_workbook = prompt_for_workbook(dir_path)
        if selected_workbook.suffix != '.xlsx':
            selected_workbook = selected_workbook.with_suffix('.xlsx')
        return selected_workbook
