from datetime import datetime


class BirthdayReminder:
    def get_upcoming_birthdays_contacts(self, contacts, days=30):
        upcoming = []
        current_date = datetime.now()
        for contact in contacts:
            birthday = datetime.strptime(contact.birthday, "%Y-%m-%d")
            if 0 <= (birthday - current_date).days <= days:
                upcoming.append(contact)
        return upcoming
