from .device_fulfillment.path_manager import PathManager
from .device_fulfillment.data_manager import DataManager
from .device_fulfillment.email_manager import EmailManager


def main():
    selected_path = PathManager.from_prompt().path
    selected_workbook = DataManager.from_path(selected_path)
    selected_sheet = selected_workbook.selected_sheet
    selected_workbook.preview_sheet()
    selected_row = selected_workbook.select_row().confirm_cohort()
    selected_cohort = selected_row.to_cohort()
    email = EmailManager.from_cohort(selected_cohort)
    email.generate_email()

if __name__ == '__main__':
    main()
