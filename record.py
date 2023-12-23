from fields import Name, Phone, Address, Email, Birthday, Note, Tag
from error_handler import InvalidTagError, InvalidPhoneError


class Record:
    def __init__(self, name, phones, address, email, birthday, note, tags):
        self.name = Name(name)
        self.phones = [Phone(phone) for phone in phones]
        self.address = Address(address)
        self.email = Email(email)
        self.birthday = Birthday(birthday)
        self.note = Note(note)
        self.tags = [Tag(tag) for tag in tags]

    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone))
        except ValueError as e:
            raise InvalidPhoneError(f"Invalid phone number: {e}")

    def delete_phone(self, phone):
        index = self.get_phone_index(phone)
        if index != -1:
            del self.phones[index]
        else:
            raise InvalidPhoneError(f"Phone number not found: {phone}")

    def find_phone(self, phone):
        index = self.get_phone_index(phone)
        if index != -1:
            return str(self.phones[index])
        else:
            raise InvalidPhoneError(f"Phone number not found: {phone}")

    def edit_phone(self, old_phone, new_phone):
        index = self.get_phone_index(old_phone)
        if index != -1:
            self.phones[index] = Phone(new_phone)
        else:
            raise InvalidPhoneError(f"Old phone number not found: {old_phone}")

    def get_phone_index(self, phone):
        for index, p in enumerate(self.phones):
            if p.value == phone:
                return index
        return -1

    def add_tag(self, tag):
        try:
            if tag != "":
                self.tags.append(Tag(tag))
        except ValueError as e:
            raise InvalidTagError(f"Invalid tag: {e}")

    def delete_tag(self, tag):
        index = self.get_tag_index(tag)
        if index != -1:
            del self.tags[index]
        else:
            raise InvalidTagError(f"Tag not found: {tag}")

    def find_tag(self, tag):
        index = self.get_tag_index(tag)
        if index != -1:
            return str(self.tags[index])
        else:
            raise InvalidTagError(f"Tag not found: {tag}")

    def edit_tag(self, old_tag, new_tag):
        index = self.get_tag_index(old_tag)
        if index != -1:
            self.tags[index] = Tag(new_tag)
        else:
            raise InvalidTagError(f"Old tag not found: {old_tag}")

    def get_tag_index(self, tag):
        for index, t in enumerate(self.tags):
            if t.value == tag:
                return index
        return -1

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def show_birthday(self):
        return self.birthday

    def delete_address(self):
        self.address = None

    def edit_address(self, address):
        self.address = Address(address)

    def edit_email(self, email):
        self.email = Email(email)

    def delete_email(self):
        self.email = None

    def edit_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def delete_birthday(self):
        self.birthday = None

    def edit_note(self, note):
        self.note = Note(note)

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
