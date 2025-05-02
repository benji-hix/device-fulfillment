from .interface.theme import rprint
from .device_fulfillment.path_manager import PathManager
from .device_fulfillment.data_manager import DataManager


def main():
    user_wkbk = PathManager()
    data_manager = DataManager(user_wkbk.path)
    dataframe = data_manager.dataframe
    rprint(f'{dataframe.head()}')
    row_data = data_manager.select_row()


if __name__ == '__main__':
    main()
