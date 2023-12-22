from fields import Name, Phone, Address, Email, Birthday, Note, Tag


class Record:
    def __init__(self, name, phones, address, email, birthday, note, tags):
        self.name = Name(name)
        self.phones = []

        for phone in phones:
            self.phones.append(Phone(phone))

        self.address = Address(address)
        self.email = Email(email)
        self.birthday = Birthday(birthday)
        self.note = Note(note)

        self.tags = []

        for tag in tags:
            self.tags.append(Tag(tag))

    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone))
        except ValueError:
            return "Invalid phone number format"
        return f"{phone} is added"

    def delete_phone(self, phone):
        self.phones.remove(self.phones[self.get_phone_index(phone)])

    def find_phone(self, phone):
        return str(self.phones[self.get_phone_index(phone)])

    def edit_phone(self, old_phone, phone):
        self.phones[self.get_phone_index(old_phone)] = Phone(phone)

    def get_phone_index(self, phone):
        index = 0
        for i in self.phones:
            if i.value == phone:
                return index
            index += 1

    def add_tag(self, tag):
        try:
            self.tags.append(Tag(tag))
        except ValueError:
            return "Invalid tag number format"
        return f"{tag} is added"

    def delete_tag(self, tag):
        self.tags.remove(self.tags[self.get_tag_index(tag)])

    def find_tag(self, tag):
        return str(self.tags[self.get_tag_index(tag)])

    def edit_tag(self, old_tag, tag):
        self.tags[self.get_tag_index(old_tag)] = tag(tag)

    def get_tag_index(self, tag):
        index = 0
        for i in self.tags:
            if i.value == tag:
                return index
            index += 1

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def show_birthday(self):
        return self.birthday

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

    