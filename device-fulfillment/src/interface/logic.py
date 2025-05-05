from pathlib import Path
from src.device_fulfillment. path_manager import PathManager
from src.device_fulfillment.data_manager import DataManager, Cohort
from src.device_fulfillment.email_manager import EmailManager

def handle_directory_step() -> Path:
    return PathManager.from_prompt().path

def handle_workbook_step(directory_path : Path) -> DataManager:
    return DataManager.from_path(directory_path)

def handle_sheet_step(workbook : DataManager) -> DataManager:
    return workbook.select_sheet().preview_sheet()

def handle_row_step(sheet : DataManager) -> Cohort:
    cohort = sheet.select_row().set_cohort().confirm_cohort().cohort
    return cohort

def handle_email_step(cohort : Cohort):
    email = EmailManager.from_cohort(cohort)
    email.generate_email()
