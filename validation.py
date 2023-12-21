# validation.py
import re


def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None




def validate_phone(phone):
    return re.match(r"\+?1?\d{9,15}$", phone) is not None






