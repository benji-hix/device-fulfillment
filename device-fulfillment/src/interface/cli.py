from enum import Enum, auto
from .theme import rprint

class Step(Enum):
    DIRECTORY = auto()
    WORKBOOK = auto()
    SHEET = auto()
    ROW_NUMBER = auto()
    END_MENU = auto()


class InteractiveCLI:
    def __init__(self):
        self.state = {
            Step.DIRECTORY: None,
            Step.WORKBOOK: None,
            Step.SHEET: None,
            Step.ROW_NUMBER: None
        }
        self.steps = list(Step)
        self.step_index : int = 0

        self.commands = {
            'go back': self.go_back,
            'start over': self.start_over,
            'exit': self.exit_cli
        }

    def go_back(self):
        if self.step_index > 0:
            self.state[self.step_index] = None
            self.step_index -= 1
            rprint('Going back...')
        else:
            rprint('You are already at the first step.')

    def start_over(self):
        self.state = {step: None for step in self.state}
        self.step_index = 0
        rprint('Starting over...')

    def exit_cli(self):
        rprint('Exiting...')
        raise SystemExit
    
    def run(self):
        while True:
            step = self.steps[self.step_index]
            match step:
                case Step.DIRECTORY:
                    continue
                case Step.WORKBOOK:
                    continue
                case Step.SHEET:
                    continue
                case Step.ROW_NUMBER:
                    continue
                case Step.END_MENU:
                    continue
                case _:
                    continue
    
if __name__ == "__main__":
    cli = InteractiveCLI()
    rprint(cli.steps)
    rprint(cli.steps[cli.step_index])