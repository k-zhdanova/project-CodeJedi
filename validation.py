import re


class Validator:
    def validate_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    def validate_phone(self, phone):
        return re.match(r"\+?1?\d{9,15}$", phone)


