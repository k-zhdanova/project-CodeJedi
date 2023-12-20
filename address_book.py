from record import Record
from collections import UserDict
from rich.table import Table
from rich.console import Console

from collections import UserDict

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}


    def add_record(self, record: Record):
        self.data[record.name.value] = record
        return f"{record.name.value} added to address book"
    
    def __str__(self):
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Name", style="dim", width=12)
        table.add_column("Phones", justify="right")
        # table.add_column("Birthday", justify="center")

        for name, record in self.data.items():
            phones = '; '.join(p for p in record.phones)
            # birthday = record.birthday if record.birthday else "N/A"
            table.add_row(name, phones)

        console = Console()
        console.print(table)

        # Since we are printing using Rich, we return an empty string for __str__
        return ""