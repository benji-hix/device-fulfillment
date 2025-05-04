from .device_fulfillment.path_manager import PathManager
from .device_fulfillment.data_manager import DataManager
from .device_fulfillment.email_manager import EmailManager
from .interface.session_manager import build_session


def main():
    build_session()
    selected_path = PathManager.from_prompt().path
    selected_sheet = DataManager.from_path(selected_path)
    selected_sheet.preview_sheet()
    selected_row = selected_sheet.select_row().set_cohort().confirm_cohort()
    email = EmailManager.from_cohort(selected_row.cohort)
    email.generate_email()

if __name__ == '__main__':
    main()
