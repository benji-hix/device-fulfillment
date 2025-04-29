from src.interface.theme import rprint
from src.interface.parser import input_dir, input_file
from pathlib import Path

class PathManager:
    def __init__(self):
        self.base_path : Path = None
        self.select_path()
        
    def __str__(self):
        return str(self.base_path.resolve())
    
    def get_path(self):
        self.base_path = input_dir()