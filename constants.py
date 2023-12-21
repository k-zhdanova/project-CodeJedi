AVAILABLE_COMMANDS = {
    "hello": {
        "preview": "hello",
        "description": "Greet the bot",
    },
    "all": {
        "preview": "all",
        "description": "Get all contacts",
    },
    "add": {
        "preview": "add",
        "description": "Add a new contact",
    },
    "add_phone": {
        "preview": "add_phone",
        "description": "Add a new phone",
    },
    "add_tag": {
        "preview": "add_tag",
        "description": "Add a new tag",
    },
    "edit": {
        "preview": "edit",
        "description": "Editing existing contacts",
    },
    "delete": {
        "preview": "delete",
        "description": "Delete an existing contact",
    },
    "help": {
        "preview": "help",
        "description": "Show all available commands",
    },
    "exit": {
        "preview": "exit",
        "description": "Exit the assistant bot",
    },
    "close": {
        "preview": "close",
        "description": "Exit the assistant bot",
    },
    "bye": {
        "preview": "bye",
        "description": "Exit the assistant bot",
    },
}

# Temporary test records
TEST_RECORDS = {
    "John": {
        "phones": ["111222333", "444555666"],
        "birthday": "01-01-1970",
        "address": "USA",
        "email": "john@gmail.com",
        "note": "Kitchen service",
        "tags": ["family"],
    },
    "Bob": {
        "phones": ["000444555"],
        "birthday": "01-01-1980",
        "address": "Ukraine",
        "email": "bob@gmail.com",
        "note": "New year party",
        "tags": ["friends", "family", "work"],
    },
    "Alice": {
        "phones": ["777888999", "000444555", "111222333"],
        "birthday": "01-01-1990",
        "address": "Poland",
        "email": "alice@gmail.com",
        "note": "Birthday party",
        "tags": ["friends"],
    },
}

SEARCH_FIELDS_LIST = [
    "name",
    "phone",
    "email",
    "birthday",
    "address",
    "note",
    "tag",
]
