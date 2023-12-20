from record import Record
from collections import UserDict



from collections import UserDict

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}


    def add_record(self, record: Record):
        self.data[record.name.value] = record
        return f"{record.name.value} added to address book"