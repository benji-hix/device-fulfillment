from .interface.theme import rprint
from .device_fulfillment.path_manager import PathManager


def main():
    file_path = PathManager()
    rprint(str(file_path))


if __name__ == '__main__':
    main()
