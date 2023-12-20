class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        self.value = value
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        self.value - value
        super().__init__(value)

    def __getvalue__(self):
        return self.value

class Birthday(Field):
    def __init__(self, value):
        self.value - value
        super().__init__(value) 

class Address(Field):
    def __init__(self, value):
        self.value - value
        super().__init__(value)

class Email(Field):
    def __init__(self, value):
        self.value - value
        super().__init__(value)  

class Notes(Field):
    pass