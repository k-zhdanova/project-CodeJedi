import re


def is_valid_email(email):
    if email == "":
        return True

    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    else:
        return False


def is_valid_birthday(birthday):
    if birthday == "":
        return True

    if re.match(r"^\d{4}-\d{2}-\d{2}$", birthday):
        return True
    else:
        return False


def is_valid_phone(phone):
    if re.match(r"\+?1?\d{9,15}$", phone):
        return True
    else:
        return False
