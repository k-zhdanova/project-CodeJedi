import validation
from birthday_reminder import BirthdayReminder
from constants import AVAILABLE_COMMANDS, TEST_RECORDS, FIELDS_LIST
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
            console.print("[bold red]🚨 Contact not found was")
        except WrongFieldError:
            console.print("[bold red]🚨 Invalid field. Please again try.")
        except ValueRequiredError:
            console.print(
                "[bold red]🚨 Value is required to search by. Please again try."
            )
        except NameRequiredError:
            console.print(
                "[bold red]🚨 Name is required to add a contact. Please again try."
            )
        except PhoneRequiredError:
            console.print(
                "[bold red]🚨 Phone number is required to add a contact. Please again try."
            )
        except InvalidTagError:
            console.print("[bold red]🚨 Invalid tag format")
        except InvalidPhoneError:
            console.print("[bold red]🚨 Invalid phone number format")
        except InvalidEmailError:
            console.print(f"[bold red]🚨 Invalid email format")
        except InvalidDateError:
            console.print(
                "[bold red]🚨 Invalid birthday format. Should be Year-month-day "
            )

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
            "[bold cyan]🌌 Greetings, young Padawan. Welcome to the Galactic Address Book, your guide in the vast universe of contacts."
        )

    def help(self):
        self.console.print(
            "[bold cyan]💫 May the Force be with you. Here are the commands to navigate the stars:"
        )

        for key, value in AVAILABLE_COMMANDS.items():
            self.console.print(
                f"[yellow3] - 🌟 {key}: {value}"
            )

    def bye(self):
        self.console.print(
            "[bold cyan]\n🌌 Farewell, and may the Force be with you always."
        )

    def all(self):
        self.console.print(
            "[bold cyan]🔭 Revealing all beings within your Galactic Address Book:"
        )
        self.book.print_records()

    @input_error
    def search(self):
        field = input(
            "🔍 Enter the field to search by (e.g., name, phone, email, birthday, address, note): "
        )

        if field not in FIELDS_LIST:
            raise WrongFieldError

        value = input("🔍 Enter the value to search by:")

        if not value.strip():
            raise ValueRequiredError

        self.book.search(field, value)

    @input_error
    def add_contact(self):
        self.console.print("[bold cyan]🌟 New Galactic Contact Entry 🌟")

        name = input("👤 Enter the contact's name (e.g., Luke Skywalker) [required]: ")
        if not name.strip():
            raise NameRequiredError

        phone = self.phone_input_loop()

        self.console.print(
            "[bold cyan]🌌 The following fields are optional. Press [Enter] to skip if not applicable."
        )
        address = input(
            "🏠 Enter the contact's address (e.g., 123 Jedi Temple, Coruscant): "
        )

        email = self.email_input_loop()
        birthday = self.birthday_input_loop()

        note = input("📝 Enter the contact's note (e.g., Jedi Master): ")
        tag = input("🏷 Enter the contact's tag (e.g., friends): ")
        tags = [tag]
        if tag == "":
            tags = []
        record = Record(name, [phone], address, email, birthday, note, tags)
        self.book.add_record(record)
        self.console.print(
            f"[bold cyan]✅ {name} has been added to your Galactic Address Book."
        )

    def phone_input_loop(self):
        while True:
            phone = input("📱 Enter the contact's phone number (e.g., 1234567890) [required]: ")
            if not phone.strip():
                self.console.print("[bold red]🚨 Phone is required, try again")
            elif not validation.is_valid_phone(phone):
                self.console.print("[bold red]🚨 Phone is not valid, try again")
            else:
                return phone

    def email_input_loop(self):
        valid = False
        while not valid:
            email = input("📧 Enter the contact's email (e.g., jedi@force.com): ")
            valid = True
            if not validation.is_valid_email(email):
                self.console.print("[bold red]🚨 Email is not valid, try again")
                valid = False

        return email

    def birthday_input_loop(self):
        valid = False
        while not valid:
            birthday = input(
                "🎉 Enter the contact's birthday (format: YYYY-MM-DD, e.g., 1977-05-25): "
            )
            valid = True
            if not validation.is_valid_birthday(birthday):
                self.console.print("[bold red]🚨 Birthday is not valid, try again")
                valid = False

        return birthday

    @input_error
    def delete_contact(self):
        name = input("👤 Enter the contact's name (e.g., Luke Skywalker) [required]: ")
        self.book.delete_contact(name)
        self.save_contacts()
        self.console.print(f"[spring_green2]✅Contact {name} deleted been has")

    @input_error
    def edit_contact(self):
        name = input("👤 Enter the contact's name: ")
        if name in self.book:
            while True:
                field_to_edit = input("🌟 Enter the field to edit: ")
                if field_to_edit in FIELDS_LIST:
                    break
                else:
                    self.console.print("[bold red]🚨 Invalid field. Please try again.")

            if field_to_edit == "phone":
                while True:
                    old_phone = input("📱 Enter the phone number to change: ")
                    if old_phone.strip() and any(phone.value == old_phone for phone in self.book[name].phones):
                        break
                    elif not old_phone.strip():
                        self.console.print("[bold red]🚨 Phone number is required. Please try again.")
                    else:
                        self.console.print("[bold red]🚨 Phone number not found. Please try again.")

                new_phone = self.phone_input_loop()
                self.change_phone(name, old_phone, new_phone, self.book)

            elif field_to_edit == "email":
                new_email = self.email_input_loop()
                self.change_email(name, new_email, self.book)

            elif field_to_edit == "birthday":
                new_birthday = self.birthday_input_loop()
                self.change_birthday(name, new_birthday, self.book)

            elif field_to_edit == "address":
                new_address = input("🏠 Enter the new address: ")
                self.change_address(name, new_address, self.book)

            elif field_to_edit == "note":
                new_note = input("📝 Enter the new note: ")
                self.change_note(name, new_note, self.book)

            elif field_to_edit == "tag":
                while True:
                    old_tag = input("🏷 Enter the tag to change: ")
                    if old_tag.strip() and any(tag.value == old_tag for tag in self.book[name].tags):
                        break
                    elif not old_tag.strip():
                        self.console.print("[bold red]🚨 Tag is required. Please try again.")
                    else:
                        self.console.print("[bold red]🚨 Tag not found. Please try again.")

                new_tag = input("🏷 Enter the new tag: ")
                self.change_tag(name, old_tag, new_tag, self.book)

            self.save_contacts()
        else:
            raise NotFoundError

    def save_contacts(self):
        self.book.save_contacts()

    @input_error
    def change_phone(self, name, old_phone, phone, book):
        record = book.find(name)
        record.edit_phone(old_phone, phone)
        self.console.print(f"[spring_green2]✅ Phone edited been has")

    @input_error
    def change_address(self, name, address, book):
        record = book.find(name)
        record.edit_address(address)
        self.console.print(f"[spring_green2]✅ Address edited been has")

    @input_error
    def change_email(self, name, email, book):
        record = book.find(name)
        record.edit_email(email)
        self.console.print(f"[spring_green2]✅ Email edited been has")

    @input_error
    def change_birthday(self, name, birthday, book):
        record = book.find(name)
        record.edit_birthday(birthday)
        self.console.print(f"[spring_green2]✅ Birthday edited been has")

    @input_error
    def change_note(self, name, note, book):
        record = book.find(name)
        record.edit_note(note)
        self.console.print(f"[spring_green2]✅ Note edited been has")

    @input_error
    def change_tag(self, name, old_tag, tag, book):
        record = book.find(name)
        record.edit_tag(old_tag, tag)
        self.console.print(f"[spring_green2]✅ Tag edited been has")

    @input_error
    def add_phone(self):
        name = input("👤 Enter the contact's name: ")
        record = self.book.find(name)

        phone = self.phone_input_loop()
        record.add_phone(phone)
        self.console.print(f"[spring_green2]✅ Phone added been has")

    @input_error
    def add_tag(self):
        name = input("👤 Enter the contact's name: ")
        record = self.book.find(name)

        while True:
            tag = input(f"🏷 Enter tag which should be added: ")
            if tag.strip():
                record.add_tag(tag)
                self.console.print(f"[spring_green2]✅ Tag '{tag}' added been has")
                break
            else:
                self.console.print("[bold red]🚨 Tag is required. Please try again.")

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
            self.console.print(
                f"[bright_red] No upcoming birthdays in next {days} days"
            )
        else:
            self.book.print_records(upcoming)

    def suggest_command(self, user_input):
        user_input = user_input.lower().strip()
        keywords = {
            "add": ["add", "new", "create", "insert"],
            "search": ["search", "find", "lookup", "query"],
            "delete": ["delete", "remove", "discard", "erase"],
            "edit": ["edit", "modify", "change", "update"],
            "birthday": ["birthday", "birth date", "bday"],
            "help": ["help", "assist", "support", "guide"],
            "exit": ["exit", "close", "leave", "quit"],
        }

        suggested_command = None
        highest_match_count = 0

        for command, command_keywords in keywords.items():
            match_count = sum(keyword in user_input for keyword in command_keywords)
            if match_count > highest_match_count:
                highest_match_count = match_count
                suggested_command = command

        if suggested_command:
            self.console.print(
                f"[bold cyan]Suggested Command: {suggested_command}"
            )
        else:
            self.console.print(
                f"[bold red]🚨 Unfortunatelly, we can't suggest any command for you"
            )
