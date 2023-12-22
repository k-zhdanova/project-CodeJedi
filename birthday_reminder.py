from datetime import datetime


class BirthdayReminder:

    @staticmethod
    def get_upcoming_birthdays_contacts(contacts, days=7):
        upcoming = []
        current_date = datetime.now()

        for contact in contacts:
            birthday_this_year = datetime.strptime(contact.birthday.value, "%Y-%m-%d").replace(year=current_date.year)

            delta = (birthday_this_year - current_date).days

            if delta < 0:
                birthday_next_year = birthday_this_year.replace(year=current_date.year + 1)
                delta = (birthday_next_year - current_date).days

            if 0 <= delta <= days:
                upcoming.append(contact)

        return upcoming
