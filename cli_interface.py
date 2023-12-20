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

    def all(self, book):
        return book

    def add_contact(self, book):
        self.name = input("Input name: ")
        if self.name:
            self.phone = input("Input phone: ")
        else:
            raise ValueError("Name is required. Input name to add a contact")
        
        self.address = input("Input address: ")
        self.email = input("Input email: ")
        self.birthday = input("Input birthday: ")  
        record = Record(self.name, self.phone, self.address, self.email, self.birthday)
        book.add_record(record)
        