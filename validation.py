# validation.py
import re
from error_handler import InvalidEmailError, InvalidPhoneError


def validate_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise InvalidEmailError(f"Invalid email format")

def validate_phone(phone):
    if not re.match(r"\+?1?\d{9,15}$", phone):
        raise InvalidPhoneError(f"Invalid phone number format")
