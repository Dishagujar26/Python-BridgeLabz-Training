# match-case in Python is Python's version of switch-case (introduced in Python 3.10).
# It allows you to perform different actions based on different conditions.

def get_day_of_week(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:                 # _ means default case.
            return "Invalid day"