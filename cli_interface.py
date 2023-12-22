from birthday_reminder import BirthdayReminder
from constants import AVAILABLE_COMMANDS, TEST_RECORDS, SEARCH_FIELDS_LIST
from fields import Phone
from record import Record
from address_book import AddressBook
from rich.table import Table
from rich.console import Console
from error_handler import (
    WrongFieldError,
    NotFoundError,
    ValueRequiredError,
    NameRequiredError,
    PhoneRequiredError,
    InvalidTagError,
    InvalidPhoneError,
    InvalidEmailError,
    InvalidDateError,
)


def input_error(func):
    console = Console()

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NotFoundError:
            console.print("[bold red]🚨 Contact was not found")
        except WrongFieldError:
            console.print("[bold red]🚨 Invalid field. Please try again.")
        except ValueRequiredError:
            console.print("[bold red]🚨 Value is required to search by. Please try again.")
        except NameRequiredError:
            console.print("[bold red]🚨 Name is required to add a contact. Please try again.")
        except PhoneRequiredError:
            console.print("[bold red]🚨 Phone number is required to add a contact. Please try again.")
        except InvalidTagError:
            console.print("[bold red]🚨 Invalid tag format")
        except InvalidPhoneError:
            console.print("[bold red]🚨 Invalid phone number format")
        except InvalidEmailError:
            console.print("[bold red]🚨 Invalid email format")
        except InvalidDateError:
            console.print("[bold red]🚨 Invalid birthday format. Should be Year-month-day ")

    return inner


class CLIInterface:
    def __init__(self, book: AddressBook):
        self.book = book

        if not book.data:
            self.init_test_records()

        self.console = Console()
        self.welcome()
        self.help()

    def init_test_records(self):
        for name, value in TEST_RECORDS.items():
            phones = value["phones"]
            record = Record(
                name,
                phones,
                value["address"],
                value["email"],
                value["birthday"],
                value["note"],
                value["tags"],
            )
            self.book.add_record(record)

    def welcome(self):
        self.console.print(
            "🌌 Greetings, young Padawan. Welcome to the Galactic Address Book, your guide in the vast universe of contacts.",
            style="bold cyan",
        )

    def help(self):
        self.console.print(
            "💫 May the Force be with you. Here are the commands to navigate the stars:",
            style="bold cyan",
        )

        for _, data in AVAILABLE_COMMANDS.items():
            print(f" - 🌟 {data['preview']}: {data['description']}")

    def bye(self):
        self.console.print(
            "\n🌌 Farewell, and may the Force be with you always.", style="bold cyan"
        )

    def all(self):
        self.console.print(
            "🔭 Revealing all beings within your Galactic Address Book:",
            style="bold cyan",
        )
        self.book.print_records()

    @input_error
    def search(self):
        field = input(
            "🔍 Enter the field to search by (e.g., name, phone, email, birthday, address, note): "
        )

        if field not in SEARCH_FIELDS_LIST:
            raise WrongFieldError

        value = input("🔍 Enter the value to search by:")

        if not value.strip():
            raise ValueRequiredError

        self.book.search(field, value)

    @input_error
    def add_contact(self):
        self.console.print("🌟 New Galactic Contact Entry 🌟", style="bold cyan")

        name = input("👤 Enter the contact's name (e.g., Luke Skywalker) [required]: ")
        if not name.strip():
            raise NameRequiredError

        phone = input(
            "📱 Enter the contact's phone number (e.g., 1234567890) [required]: "
        )
        if not phone.strip():
            raise PhoneRequiredError

        self.console.print(
            "🌌 The following fields are optional. Press [Enter] to skip if not applicable.",
            style="bold cyan",
        )
        address = input(
            "🏠 Enter the contact's address (e.g., 123 Jedi Temple, Coruscant): "
        )
        email = input("📧 Enter the contact's email (e.g., jedi@force.com): ")
        birthday = input(
            "🎉 Enter the contact's birthday (format: YYYY-MM-DD, e.g., 1977-05-25): "
        )
        note = input("📝 Enter the contact's note (e.g., Jedi Master): ")
        tag = input("🏷 Enter the contact's tag (e.g., friends): ")

        try:
            record = Record(name, [phone], address, email, birthday, note, [tag])
            self.book.add_record(record)
        except InvalidEmailError as e:
            self.console.print(f"[bold red]🚨 Error adding contact: {e}")
        except InvalidPhoneError as e:
            self.console.print(f"[bold red]🚨 Error adding contact: {e}")
        else:
            self.console.print(f"✅ {name} has been added to your Galactic Address Book.", style="bold cyan")

    @input_error
    def delete_contact(self):
        name = input("👤 Enter the contact's name (e.g., Luke Skywalker) [required]: ")
        self.book.delete_contact(name)
        self.console.print(f"[yellow]✅Contact {name} deleted been has")

    @input_error
    def edit_contact(self):
        name = input(f"👤 Enter the contact's name: ")
        if name in self.book:
            field_to_edit = input("🌟 Enter the field to edit: ")
            if field_to_edit not in SEARCH_FIELDS_LIST:
                raise WrongFieldError
            else:
                value = input("🌟 Enter the new value: ")
                if field_to_edit == "phone":
                    old_phone = input("📱 Enter phone which should be changed: ")
                    self.change_phone(name, old_phone, value, self.book)
                elif field_to_edit == "address":
                    self.change_address(name, value, self.book)
                elif field_to_edit == "email":
                    self.change_email(name, value, self.book)
                elif field_to_edit == "birthday":
                    self.change_birthday(name, value, self.book)
                elif field_to_edit == "note":
                    self.change_note(name, value, self.book)
                elif field_to_edit == "tag":
                    old_tag = input("🏷 Enter tag which should be changed: ")
                    self.change_tag(name, old_tag, value, self.book)

                self.save_contacts()
        else:
            raise NotFoundError

    def save_contacts(self):
        self.book.save_contacts()

    @input_error
    def change_phone(self, name, old_phone, phone, book):
        record = book.find(name)
        record.edit_phone(old_phone, phone)
        self.console.print(f"[yellow]✅ Phone edited been has")

    @input_error
    def change_address(self, name, address, book):
        record = book.find(name)
        record.edit_address(address)
        self.console.print(f"[yellow]✅ Address edited been has")

    @input_error
    def change_email(self, name, email, book):
        record = book.find(name)
        record.edit_email(email)
        self.console.print(f"[yellow]✅ Email edited been has")

    @input_error
    def change_birthday(self, name, birthday, book):
        record = book.find(name)
        record.edit_birthday(birthday)
        self.console.print(f"[yellow]✅ Birthday edited been has")

    @input_error
    def change_note(self, name, note, book):
        record = book.find(name)
        record.edit_note(note)
        self.console.print(f"[yellow]✅ Note edited been has")

    @input_error
    def change_tag(self, name, old_tag, tag, book):
        record = book.find(name)
        record.edit_tag(old_tag, tag)
        self.console.print(f"[yellow]✅ Tag edited been has")

    @input_error
    def add_phone(self):
        name = input("👤 Enter the contact's name: ")
        record = self.book.find(name)

        phone = input("Enter phone which should be added: ")
        record.add_phone(phone)
        self.console.print(f"[yellow]✅ Phone added been has")

    @input_error
    def add_tag(self):
        name = input("👤 Enter the contact's name: ")
        record = self.book.find(name)

        tag = input("Enter tag which should be added: ")
        record.add_tag(tag)
        self.console.print(f"[yellow]✅ Tag added been has")

    def show_birthday(self):
        name = input("Enter name: ")
        record = self.book.find(name)
        if not record.birthday:
            raise NotFoundError
        self.console.print(f"[spring_green2]🎉 {name}'s birthday {record.birthday} is")
        
    def print_upcoming_birthdays_contacts(self):
        days = input("👤 Enter period in days. If empty, default 7 will be used: ")
        if days == "":
            days = "7"

        try:
            days = int(days)
        except ValueError:
            raise ValueError("'days' must be a number")

        contacts = list(self.book.data.values())
        upcoming = BirthdayReminder.get_upcoming_birthdays_contacts(contacts, days)

        if not upcoming:
            print(f"No upcoming birthdays in next {days} days")
        else:
            self.book.print_records(upcoming)

