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

            elif command in ["close", "exit", "bye"]:
                cli.bye()
                break

            elif command == "add":
                cli.add_contact()

            elif command == "all":
                cli.all()

            elif command == "search":
                cli.search()

            elif command == "delete":
                cli.delete_contact()

            elif command == "edit":
                cli.edit_contact()

            elif command == "add_phone":
                cli.add_phone()

            elif command == "add_tag":
                cli.add_tag()

        except KeyboardInterrupt:
            # cli.bye()
            console.print(
                "\n🚀 A sudden retreat? Very well, the Force will be waiting for your return.",
                style="bold cyan",
            )
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
