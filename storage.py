import json
import os
from rich.console import Console
from record import Record


class Storage:
    def __init__(self, folder_name='AddressBookData'):
        self.console = Console()

        self.folder_name = folder_name
        self.file_path = os.path.join(os.path.expanduser('~'), folder_name)
        if not os.path.exists(self.file_path):
            os.makedirs(self.file_path)

    def _get_file(self, file_name):
        return os.path.join(self.file_path, f"{file_name}.json")

    def save_data(self, data, file_name):
        file_path = self._get_file(file_name)
        with open(file_path, 'w') as file:
            json.dump(data, file, default=self._custom_serializer, indent=4)

    def save_contacts(self, data):
        self.save_data(data, 'contacts')

    def load_data(self, file_name):
        file_path = self._get_file(file_name)
        if not os.path.exists(file_path):
            return None  # Return None if the file does not exist

        try:
            with open(file_path, 'r') as file:
                return json.load(file, object_hook=self._custom_deserializer)
        except json.JSONDecodeError as e:
            self.console.print(f"🚨 Error decoding JSON data from file {file_name}")

            return None  # Return None if there is a JSON decoding error

    @staticmethod
    def _custom_serializer(obj):
        if isinstance(obj, Record):
            serialized_record = {
                "name": obj.name.value,
                "phones": [phone.value for phone in obj.phones],
                "address": obj.address.value,
                "email": obj.email.value,
                "note": obj.note.value,
                "tags": [tag.value for tag in obj.tags],
                "birthday": obj.birthday.value
            }

            return serialized_record

        return obj.__dict__
    @staticmethod
    def _custom_deserializer(d):
        if 'name' in d:
            return Record(
                d['name'],
                d.get('phones', []),
                d.get('address', ''),
                d.get('email', ''),
                d.get('birthday', ''),
                d.get('note', ''),
                d.get('tags', [])
            )
        return d


