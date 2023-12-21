import json
import os
from datetime import datetime
from record import Record


class Storage:
    def __init__(self, folder_name='AddressBookData'):
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

    def load_data(self, file_name):
        file_path = self._get_file(file_name)
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return json.load(file, object_hook=self._custom_deserializer)
        return {}

    @staticmethod
    def _custom_serializer(obj):
        if isinstance(obj, Record):
            return {
                "name": obj.name.value,
                "phones": [phone.value for phone in obj.phones],
                "address": obj.address.value,
                "email": obj.email.value,
                "birthday": obj.birthday.value.strftime('%Y-%m-%d') if obj.birthday.value else None,
                "note": obj.note.value,
                "tags": [tag.value for tag in obj.tags]
            }
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d')
        return obj.__dict__

    @staticmethod
    def _custom_deserializer(d):
        if 'name' in d:
            return Record(
                d['name'],
                d.get('phones', []),
                d.get('address', ''),
                d.get('email', ''),
                datetime.strptime(d['birthday'], '%Y-%m-%d').date() if d['birthday'] else None,
                d.get('note', ''),
                d.get('tags', [])
            )
        return d


