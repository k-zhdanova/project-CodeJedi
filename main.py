from helpers import parse_input
from cli_interface import CLIInterface
from address_book import AddressBook
from rich.console import Console


def main():
    console = Console()
    book = AddressBook()

    cli = CLIInterface(book)
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

            if command == "add":
                cli.add_contact()

            if command == "all":
                cli.all()

            if command == "search":
                cli.search()

        except KeyboardInterrupt:
            # cli.bye()
            console.print("\n🚀 A sudden retreat? Very well, the Force will be waiting for your return.",
                          style="bold cyan")
            return
        except ValueError as error:
            # print(error)
            console.print(f"[bold red]🔥 Disturbance in the Force: {error}")
            continue
        except Exception as error:
            console.print(f"[bold red]⚡ A great disturbance in the Force: {error}")
            print("🧐 Unexpected this error is. Meditate on your actions, you must.")
            continue


if __name__ == "__main__":
    main()
