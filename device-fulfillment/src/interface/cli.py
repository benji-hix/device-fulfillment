from enum import Enum, auto
from .theme import rprint
from .session_manager import build_session

from .logic import (
    handle_directory_step,
    handle_email_step,
    handle_row_step,
    handle_sheet_step,
    handle_workbook_step,
)


class Step(Enum):
    DIRECTORY = auto()  # 0
    WORKBOOK = auto()   # 1
    SHEET = auto()      # 3
    ROW = auto()        # 4
    EMAIL = auto()      # 5
    END_MENU = auto()   # 6


class InteractiveCLI:
    def __init__(self):
        self.state = {
            Step.DIRECTORY: None,
            Step.WORKBOOK: None,
            Step.SHEET: None,
            Step.ROW: None,
        }
        self.steps = list(Step)
        self.step_index: int = 0

        self.commands = {
            'back': self.back,
            'restart': self.restart,
            'exit': self.exit_cli,
        }

    def back(self):
        if self.step_index > 0:
            self.state[self.step_index] = None
            self.step_index -= 1
            rprint('Going back...')
        else:
            rprint('You are already at the first step.')

    def restart(self):
        self.state = {step: None for step in self.state}
        self.step_index = 0
        rprint('Starting over...')

    def exit_cli(self):
        rprint('Exiting app...')
        raise SystemExit

    def run(self):
        try:
            while True:
                step = self.steps[self.step_index]
                build_session()
                match step:
                    case Step.DIRECTORY:
                        self.state[Step.DIRECTORY] = handle_directory_step()
                        self.step_index += 1
                    case Step.WORKBOOK:
                        self.state[Step.WORKBOOK] = handle_workbook_step(self.state[Step.DIRECTORY])
                        self.step_index += 1
                    case Step.SHEET:
                        self.state[Step.SHEET] = handle_sheet_step(self.state[Step.WORKBOOK])
                        self.step_index += 1
                    case Step.ROW:
                        self.state[Step.ROW] = handle_row_step(self.state[Step.SHEET])
                        self.step_index += 1
                    case Step.EMAIL:
                        handle_email_step(self.state[Step.ROW])
                        self.step_index += 1
                    case Step.END_MENU:
                        input('Press enter to exit application.')
                        break
                    case _:
                        continue
        except KeyboardInterrupt:
            rprint('Ctrl-C input.')
            self.exit_cli()