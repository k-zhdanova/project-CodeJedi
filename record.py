from fields import Name
from fields import Phone
from fields import Address
from fields import Email
from fields import Birthday

class Record:
   def __init__(self, name, phone, address, email, birthday):
        self.name = Name(name)
        self.phones = []
        if phone:
            self.phones.append(phone)
        self.address = Address(address)
        self.email = Email(email)
        self.birthday = Birthday(birthday)
 
   def __getname__(self):
        return self.name

   def __getphone__(self):
        return self.phones