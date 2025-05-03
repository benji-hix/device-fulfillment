import win32com.client
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from .contact_info import NETWORK_CONTACTS as contacts
from .contact_info import ADDRESSEES
from .data_manager import Cohort
from src.interface.theme import rprint

class EmailManager:
    def __init__(self, cohort: Cohort = None):
        self.outlook = win32com.client.Dispatch('Outlook.Application')
        self.mail = self.outlook.CreateItem(0)
        self.cohort: Cohort = cohort
        self.device_type = ''
        self.addressee = ''
        self.formatted_date = ''

    @classmethod
    def from_cohort(cls, cohort):
        instance = cls(cohort)
        instance._set_recipient()
        instance._set_device_type()
        instance._set_subject()
        instance._set_body()
        return instance

    def generate_email(self):
        rprint('Generating email from cohort data...')
        self.mail.Display()

    def _set_recipient(self):
        match self.cohort.network:
            case 'TPLA':
                self.mail.To = self.cohort.instructor
                self.mail.CC = contacts['TPLA']['CC']
                instructor_email = self.cohort.instructor
                instructor_first = instructor_email.split('@')[0].split('.')[0].capitalize()
                self.addressee = instructor_first
                return self
            case 'CWCE':
                self.mail.To = contacts['CWCE']['To']
                self.mail.CC = contacts['CWCE']['CC']
                self.addressee = ADDRESSEES['CWCE']
                return self
            case 'CCS':
                self.mail.To = contacts['CCS']['To']
                self.addressee = ADDRESSEES['CCS']
                return self
            case 'CPTC':
                self.mail.To = contacts['CPTC']['To']
                self.mail.CC = contacts['CPTC']['CC']
                self.addressee = ADDRESSEES['CPTC']
                return self
            case _:
                return self

    def _set_device_type(self):
        if self.cohort.type == 'ATv2' or self.cohort.type == 'BTv4':
            self.device_type = 'iPad'
        else:
            self.device_type = 'Chromebook'
        return self

    def _set_subject(self):
        raw_date = self.cohort.start_date
        self.formatted_date = f'{raw_date.month}-{raw_date.day}-{raw_date.year}'
        network = self.cohort.network
        cohort_type = self.cohort.type
        location = self.cohort.location
        subject_str = (
            f'Device Ordering | {cohort_type} {network} {location} {self.formatted_date}'
        )
        self.mail.subject = subject_str
        return self

    def _set_body(self):
        # self.mail.body = 'Test email, please disregard.'
        current_dir = Path(__file__).parent
        env = Environment(loader=FileSystemLoader(current_dir))
        # Current issue: how to directly link correct dir/path
        template = env.get_template('check_inventory.html')
        html_content = template.render(
            addressee = self.addressee,
            course_id = self.cohort.course_id,
            date = self.formatted_date,
            instructor = self.cohort.instructor,
            location = self.cohort.location,
            enrollment = self.cohort.enrollment,
            device_type = self.device_type
        )
        self.mail.HTMLbody = html_content
