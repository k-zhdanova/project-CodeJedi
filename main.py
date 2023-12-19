from helpers import parse_input
from cli_interface import CLIInterface

def main():
    cli = CLIInterface()
    cli.welcome()

    while True:
        try: 
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command == "help":
                cli.help()

            if command in ["close", "exit", "bye"]:
                cli.bye()
                break

        except KeyboardInterrupt:
            cli.bye()
            return


if __name__ == "__main__":
    main()