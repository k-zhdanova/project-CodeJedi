from fields import Name, Phone, Address, Email, Birthday, Note


class Record:
    def __init__(self, name, phone, address, email, birthday, note=None):
        self.name = Name(name)
        self.phones = []
        if phone:
            self.phones.append(Phone(phone))

        self.address = Address(address)
        self.email = Email(email)
        self.birthday = Birthday(birthday)
        self.note = Note(note)

    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone))
        except ValueError:
            return "Invalid phone number format"
        return f"{phone} is added"

    def delete_phone(self, phone):
        self.phones.remove(self.phones[self.get_index(phone)])

    def find_phone(self, phone):
        return str(self.phones[self.get_index(phone)])

    def edit_phone(self, old_phone, phone):
        self.phones[self.get_index(old_phone)] = Phone(phone)

    def get_index(self, phone):
        index = 0
        for i in self.phones:
            if i.value == phone:
                return index
            index += 1

    # error handler - IndexError

    def delete_address(self):
        self.address = None

    def edit_address(self, address):
        self.address = address

    def edit_email(self, email):
        self.email = email

    def delete_email(self):
        self.email = None

    def edit_birthday(self, birthday):
        self.birthday = birthday

    def delete_birthday(self):
        self.birthday = None

    def edit_note(self, note):
        self.note = note

    def delete_note(self):
        self.note = None

    def __getname__(self):
        return self.name

    def __getphone__(self):
        return self.phones

    def __getaddress__(self):
        return self.address

    def __getemail__(self):
        return self.email

    def __getbirthday__(self):
        return self.birthday

    def __getnote__(self):
        return self.note
