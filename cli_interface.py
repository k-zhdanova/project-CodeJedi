from constants import AVAILABLE_COMMANDS
from fields import Phone
from record import Record
from address_book import AddressBook

class CLIInterface:
    
    def welcome(self):
        print("Welcome to the assistant bot!")

    def help(self):
        print("Available Commands:")
                
        for _, data in AVAILABLE_COMMANDS.items():
            print(f"  - {data['preview']}: {data['description']}")

    def bye(self):
        print("\nGood bye!")

    def add_contact(book):
        name = input("Input name: ")
        if name:
            phone = input("Input phone: ")
        else:
            raise ValueError ("Name is required. Input name to add a contact")
        
        address = input("Input address: ")
        email = input("Input email: ")
        birthday = input("Input birthday: ")  
        record = Record(name, phone, address, email, birthday)
        print(book.add_record(record))
        
