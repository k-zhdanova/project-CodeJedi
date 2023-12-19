from constants import AVAILABLE_COMMANDS

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