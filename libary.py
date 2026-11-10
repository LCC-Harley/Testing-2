import datetime

print("Hello world!")
'''
Input:   return date, member type (Adult, Student, Senior).
Logic:
Standard: £0.50/day late.
Best-Seller: £1.00/day late.
DVD: £2.00/day late.
Discounts: Seniors receive 50% off fines; Students receive 20% off fines.
Maximum fine capped at £15.00 per item.
Output: Total days late, fine amount due, and receipt summary.
'''


def parse_date(value):
    if isinstance(value, datetime.date):
        return value
    if isinstance(value, str):
        return datetime.datetime.strptime(value, "%d/%m/%y").date()
    raise TypeError("Date must be a string in DD/MM/YY format or a date object.")


def calculateDaysLate(DUE_DATE, CURRENT_DATE):
    due_date = parse_date(DUE_DATE)
    current_date = parse_date(CURRENT_DATE)
    days_late = (current_date - due_date).days
    if days_late < 0:
        days_late = 0
    return days_late


def calculateFine(BOOK_TYPE, MEMBERSHIP, DAYS_LATE):
    if BOOK_TYPE == "standard":
        daily_fine = 0.50
    elif BOOK_TYPE == "best-seller":
        daily_fine = 1.00
    elif BOOK_TYPE == "dvd":
        daily_fine = 2.00
    else:
        raise ValueError("Invalid book type!")

    fine = DAYS_LATE * daily_fine

    if MEMBERSHIP == "senior":
        fine = fine * 0.50
    elif MEMBERSHIP == "student":
        fine = fine * 0.80
    elif MEMBERSHIP != "adult":
        raise ValueError("Invalid membership type!")

    if fine > 15:
        fine = 15
    return fine


if __name__ == "__main__":
    BOOK_TYPE = input("What book type do you have (Standard, Best-Seller, DVD): ").lower()
    DUE_DATE = input("When was the book due to be returned? (DD/MM/YY): ")
    MEMBERSHIP = input("What member type are you? (Adult, Student, Senior): ").lower()
    CURRENT_DATE = datetime.date.today()

    if BOOK_TYPE not in ["standard", "best-seller", "dvd"]:
        print("Invalid book type!")
    elif MEMBERSHIP not in ["adult", "student", "senior"]:
        print("Invalid membership type!")
    else:
        DAYS_LATE = calculateDaysLate(DUE_DATE, CURRENT_DATE)
        FINE = calculateFine(BOOK_TYPE, MEMBERSHIP, DAYS_LATE)
        print("\n========== LIBRARY RECEIPT ==========")
        print("Book type:       ", BOOK_TYPE.upper())
        print("Membership:      ", MEMBERSHIP.capitalize())
        print("Due date:        ", DUE_DATE)
        print("Return date:     ", CURRENT_DATE.strftime("%d/%m/%y"))
        print("Days late:       ", DAYS_LATE)
        print("Fine due:        £{:.2f}".format(FINE))
        print("=====================================")
        if DAYS_LATE == 0:
            print("Thank you! Your book was returned on time.")
        else:
            print("Please pay your outstanding fine.")
