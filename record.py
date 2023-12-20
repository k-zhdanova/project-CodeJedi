from fields import Name
from fields import Phone
from fields import Address
from fields import Email
from fields import Birthday
from fields import Note

class Record:
    def __init__(self, name, phone, address, email, birthday, note = None):
        self.name = Name(name)
        self.phones = []
        if phone:
            self.phones.append(Phone(phone))

        self.address = Address(address)
        self.email = Email(email)
        self.birthday = Birthday(birthday)
        self.note = Note(note)
 
    def __getname__(self):
        return self.name

    def __getphone__(self):
        return self.phones