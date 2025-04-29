from rich.console import Console
from rich.traceback import install
from rich.theme import Theme
from rich.panel import Panel
from rich.table import Table
from rich import print

install()

cli_theme = Theme(
    {
        'navigation': 'italic #0087d7',
        'receive': 'underline #99332e',
        'error': 'bold red',
        'success': 'italic yellow',
    }
)

console = Console(theme=cli_theme)


def rprint(*args, **kwargs):
    console.print(*args, **kwargs)


__all__ = ['Console', 'Theme', 'Panel', 'Table', 'rprint', 'print']
