from datetime import datetime

class BirthdayReminder:
    def __init__(self, contacts):
        self.contacts = contacts

    def upcoming_birthdays(self, days=30):
        upcoming = []
        current_date = datetime.now()
        for contact in self.contacts:
            birthday = datetime.strptime(contact.birthday, '%Y-%m-%d')
            if 0 <= (birthday - current_date).days <= days:
                upcoming.append(contact)
        return upcoming
