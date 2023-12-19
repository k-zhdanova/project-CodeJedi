from constants import AVAILABLE_COMMANDS
from record import Record

class CLIInterface:
    def __init__(self):
        pass

    def welcome(self):
        print("Welcome to the assistant bot!")

    def help(self):
        print("Available Commands:")
                
        for _, data in AVAILABLE_COMMANDS.items():
            print(f"  - {data['preview']}: {data['description']}")

    def bye(self):
        print("\nGood bye!")

    def add(self, args):
        name, phone = args
        record = Record(name, phone)
        print(book.add_record(record))

        '''
ask name
save
ask 
if enter - no error/ not add
name+phone - required --> validation?



        '''