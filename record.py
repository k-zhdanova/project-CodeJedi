from fields import Name
from fields import Phone

class Record:
   def __init__(self, name, phone, address, email, birthday):
        self.name = Name(name)
        self.phones = []
        if phone:
            self.phones.append(phone)
        self.address = address
        self.email = email
        self.birthday = birthday


   
   
   def __getname__(self):
        return self.name

   def __getphone__(self):
        return self.phones