class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)


class Address(Field):
    def __init__(self, value):
        super().__init__(value)


class Email(Field):
    def __init__(self, value):
        super().__init__(value)


class Note(Field):
    def __init__(self, value):
        super().__init__(value)
