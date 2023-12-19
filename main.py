from collections import UserDict
from helpers import parse_input

class Field:
    pass

class Name(Field):
    pass

class Phone(Field):
    pass

class Birthday(Field):
    pass

class Notes(Field):
    pass

class Record:
   pass

class AddressBook(UserDict):
    pass

def main():
    print("Welcome to the assistant bot!")

    while True:
        try: 
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit", "bye"]:
                print("\nGood bye!")
                break

        except KeyboardInterrupt:
            print("\nGood bye!")
            return


if __name__ == "__main__":
    main()