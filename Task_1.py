from _datetime import datetime


def get_days_from_today(given_date):
    try:
        get_day = datetime.strptime(given_date, "%Y-%m-%d").date()
        current_day = datetime.today().date()
        difference_days = current_day - get_day
        return difference_days.days
    except ValueError:
        print('Invalid date!')


given_date = input('Please, enter the date in format (yyyy-mm-dd): ')
print(get_days_from_today(given_date))
