from .interface.cli import InteractiveCLI


def main():
    cli = InteractiveCLI()
    cli.run()


if __name__ == '__main__':
    main()
