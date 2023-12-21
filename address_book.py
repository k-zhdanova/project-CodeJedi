from record import Record
from collections import UserDict
from rich.table import Table
from rich.console import Console
from collections import UserDict

from validation import validate_email, validate_phone


class AddressBook(UserDict):
    def __init__(self):
        self.data = {}
        self.console = Console()

    def add_record(self, record: Record):
        if record.email and not validate_email(record.email.value):
            return "🚨 Invalid email. Record not added."
        if any(phone for phone in record.phones if not validate_phone(phone.value)):
            return "🚨 Invalid phone number. Record not added."
        self.data[record.name.value] = record
        return f"{record.name.value} added to address book"

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            raise ValueError(f"🚨 {name} was not found")

    def delete_contact(self, name):
        if name in self.data:
            del self.data[name]
        else:
            return f"{name} was not found"

    def search(self, field, value):
        result = None
        if field == "name":
            result = self.search_by_name(value)
        elif field == "phone":
            result = self.search_by_phone(value)
        elif field == "email":
            result = self.search_by_email(value)
        elif field == "birthday":
            result = self.search_by_birthday(value)
        elif field == "address":
            result = self.search_by_address(value)
        elif field == "note":
            result = self.search_by_note(value)
        elif field == "tag":
            result = self.search_by_tag(value)
        else:
            raise ValueError("🚨 Invalid field. Please try again.")

        if not result:
            self.console.print(f"🔍 No records found for {field} = {value}.")
            return ""

        self.console.print(
            f"🔍 {len(result)} {'records' if len(result) > 1 else 'record'} found for {field} = {value}",
            style="bold cyan",
        )

        self.print_records(result)

    def search_by_name(self, name):
        return [
            record
            for record in self.data.values()
            if name.lower() in record.name.value.lower()
        ]

    def search_by_phone(self, phone):
        return [
            record
            for record in self.data.values()
            if any(phone in p.value for p in record.phones)
        ]

    def search_by_email(self, email):
        return [
            record
            for record in self.data.values()
            if email.lower() in record.email.value.lower()
        ]

    def search_by_birthday(self, birthday):
        return [
            record for record in self.data.values() if birthday in record.birthday.value
        ]

    def search_by_address(self, address):
        return [
            record
            for record in self.data.values()
            if address.lower() in record.address.value.lower()
        ]

    def search_by_note(self, note):
        return [
            record
            for record in self.data.values()
            if note.lower() in record.note.value.lower()
        ]

    def search_by_tag(self, tag):
        return [
            record
            for record in self.data.values()
            if any(tag in t.value for t in record.tags)
        ]

    def print_records(self, records=None):
        if not records:
            records = self.data.values()

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Name", style="dim", width=15, justify="center")
        table.add_column("Phones", justify="center")
        table.add_column("Email", justify="center")
        table.add_column("Birthday", justify="center")
        table.add_column("Address", justify="center")
        table.add_column("Note", justify="center")
        table.add_column("Tags", justify="center")

        for record in records:
            phones = "; ".join(p.value for p in record.phones)
            email = record.email.value if record.email else "N/A"
            birthday = record.birthday.value if record.birthday else "N/A"
            address = record.address.value if record.address else "N/A"
            note = record.note.value if record.note else "N/A"
            tags = "; ".join(t.value for t in record.tags)

            table.add_row(
                record.name.value, phones, email, birthday, address, note, tags
            )

        self.console.print(table)

    def __str__(self):
        return self.print_records(self)
