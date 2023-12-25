AVAILABLE_COMMANDS = {
    "all": "Get all contacts",
    "add": "Add a new contact",
    "search": "Search contact by any field",
    "add_phone": "Add a new phone",
    "add_tag": "Add a new tag",
    "edit": "Editing existing contacts",
    "delete": "Delete an existing contact",
    "show-birthday": "Shows upcoming birthdays for given period",
    "birthdays": "Show contacts with birthdays next period",
    "help": "Show all available commands",
    "exit": "Exit the assistant bot",
    "close": "Exit the assistant bot",
    "bye": "Exit the assistant bot",
}

# Temporary test records
TEST_RECORDS = {
    "John": {
        "phones": ["111222333", "444555666"],
        "birthday": "1971-01-01",
        "address": "USA",
        "email": "john@gmail.com",
        "note": "Kitchen service",
        "tags": ["family"],
    },
    "Bob": {
        "phones": ["000444555"],
        "birthday": "1980-01-01",
        "address": "Ukraine",
        "email": "bob@gmail.com",
        "note": "New year party",
        "tags": ["friends", "family", "work"],
    },
    "Alice": {
        "phones": ["777888999", "000444555", "111222333"],
        "birthday": "1990-01-01",
        "address": "Poland",
        "email": "alice@gmail.com",
        "note": "Birthday party",
        "tags": ["friends"],
    },
}

FIELDS_LIST = [
    "name",
    "phone",
    "email",
    "birthday",
    "address",
    "note",
    "tag",
]
