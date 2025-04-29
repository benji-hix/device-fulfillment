from .interface.parser import input_dir, input_file
from .interface.theme import rprint


def main():
    user_directory = input_dir()
    user_path = input_file(user_directory)
    rprint(str(user_path))


if __name__ == '__main__':
    main()
