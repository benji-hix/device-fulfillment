from enum import Enum, auto
from .theme import rprint
from .session_manager import build_session
from src.device_fulfillment.data_manager import DataManager
from src.device_fulfillment.path_manager import PathManager
from src.device_fulfillment.email_manager import EmailManager


class Step(Enum):
    DIRECTORY = auto()
    WORKBOOK = auto()
    SHEET = auto()
    ROW = auto()
    EMAIL = auto()
    END_MENU = auto()

class InteractiveCLI:
    def __init__(self):
        self.state = {
            Step.DIRECTORY: None,
            Step.WORKBOOK: None,
            Step.SHEET : None,
            Step.ROW: None,
        }
        self.steps = list(Step)
        self.step_index: int = 0

        self.commands = {
            'go back': self.go_back,
            'start over': self.start_over,
            'exit': self.exit_cli,
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
            build_session()
            match step:
                case Step.DIRECTORY:
                    self.state[Step.DIRECTORY] = PathManager.from_prompt().path
                    self.step_index += 1
                case Step.WORKBOOK:
                    self.state[Step.WORKBOOK] = DataManager.from_path(
                        self.state[Step.DIRECTORY]
                    )
                    self.step_index += 1
                case Step.SHEET:
                    self.state[Step.SHEET] = (
                        self.state[Step.WORKBOOK].select_sheet().preview_sheet()
                    )
                    self.step_index += 1
                case Step.ROW:
                    self.state[Step.ROW] = (
                        self.state[Step.SHEET]
                        .select_row()
                        .set_cohort()
                        .confirm_cohort()
                        .cohort
                    )
                    self.step_index += 1
                case Step.EMAIL:
                    email = EmailManager.from_cohort(self.state[Step.ROW])
                    email.generate_email()
                    self.step_index += 1
                case Step.END_MENU:
                    input('Press enter to exit application.')
                    break
                case _:
                    continue
