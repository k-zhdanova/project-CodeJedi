import json
import os


class Contact:
    pass


class Note:
    pass


class StorageManager:
    def __init__(self, contact_filename='contacts.json', note_filename='notes.json'):
        self.contact_filename = contact_filename
        self.note_filename = note_filename
        self.ensure_data_files_exist()

    def ensure_data_files_exist(self):
        # Створюємо файли, якщо вони не існують
        for filename in [self.contact_filename, self.note_filename]:
            if not os.path.exists(filename):
                with open(filename, 'w') as file:
                    json.dump([], file)

    def save_contacts(self, contacts):
        with open(self.contact_filename, 'w') as file:
            json.dump([contact.__dict__ for contact in contacts], file)

    def load_contacts(self):
        with open(self.contact_filename, 'r') as file:
            return [Contact(**data) for data in json.load(file)]

    def save_notes(self, notes):
        with open(self.note_filename, 'w') as file:
            json.dump([note.__dict__ for note in notes], file)

    def load_notes(self):
        with open(self.note_filename, 'r') as file:
            return [Note(**data) for data in json.load(file)]
