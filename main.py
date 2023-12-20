from helpers import parse_input
from cli_interface import CLIInterface
from address_book import AddressBook

def main():
    cli = CLIInterface()
    cli.welcome()
    book = AddressBook()

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
                result = cli.add_contact(book)
                print(result)

            if command == "all":
                result = cli.all(book)
                print(result)

        except KeyboardInterrupt:
            cli.bye()
            return
        except ValueError as error:
            print(error)
            continue
        except Exception as error:
            print(f"Error: {error}")
            continue


if __name__ == "__main__":
    main()