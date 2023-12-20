from constants import AVAILABLE_COMMANDS, TEST_RECORDS, SEARCH_FIELDS_LIST
from fields import Phone
from record import Record
from address_book import AddressBook
from rich.table import Table
from rich.console import Console

class CLIInterface:
    def __init__(self, book: AddressBook):
        self.book = book

        if not book.data:
            self.init_test_records()

        self.console = Console()

    def init_test_records(self):
        for name, value in TEST_RECORDS.items():
            phones = value["phones"]
            record = Record(name, phones, value["address"], value["email"], value["birthday"], value["note"])
            self.book.add_record(record)

    def welcome(self):
        self.console.print("🌌 Greetings, young Padawan. Welcome to the Galactic Address Book, your guide in the vast universe of contacts.", style="bold cyan")

    def help(self):
        self.console.print("💫 May the Force be with you. Here are the commands to navigate the stars:", style="bold cyan")
                
        for _, data in AVAILABLE_COMMANDS.items():
            print(f" - 🌟 {data['preview']}: {data['description']}")

    def bye(self):
        self.console.print("\n🌌 Farewell, and may the Force be with you always.", style="bold cyan")

    def all(self):
        self.console.print("🔭 Revealing all beings within your Galactic Address Book:", style="bold cyan")
        self.book.print_records()
    
    def search(self):
        field = input("🔍 Enter the field to search by (e.g., name, phone, email, birthday, address, note): ")

        if field not in SEARCH_FIELDS_LIST:
            raise ValueError("🚨 Invalid field. Please try again.")

        value = input("🔍 Enter the value to search by:")

        if not value.strip():
            raise ValueError("🚨 Value is required to search by. Please try again.")
        
        self.book.search(field, value)

    def add_contact(self):
        self.console.print("🌟 New Galactic Contact Entry 🌟", style="bold cyan")

        name = input("👤 Enter the contact's name (e.g., Luke Skywalker) [required]: ")
        if not name.strip():
            raise ValueError("🚨 Name is required to add a contact. Please try again.")

        phone = input("📱 Enter the contact's phone number (e.g., 1234567890) [required]: ")
        if not phone.strip():
            raise ValueError("🚨 Phone number is required to add a contact. Please try again.")

        self.console.print("🌌 The following fields are optional. Press [Enter] to skip if not applicable.", style="bold cyan")
        address = input("🏠 Enter the contact's address (e.g., 123 Jedi Temple, Coruscant): ")
        email = input("📧 Enter the contact's email (e.g., jedi@force.com): ")
        birthday = input("🎉 Enter the contact's birthday (format: YYYY-MM-DD, e.g., 1977-05-25): ")

        record = Record(name, phone, address, email, birthday)
        self.book.add_record(record)
        self.console.print(f"✅ {name} has been added to your Galactic Address Book.", style="bold cyan")

        
