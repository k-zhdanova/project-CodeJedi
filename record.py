from fields import Name
from fields import Phone

class Record:
   def __init__(self, name, phone):
        self.name = Name(name)
        self.phone = Phone(phone)
   
   def __getname__(self):
        return self.name

   def __getphone__(self):
        return self.phone