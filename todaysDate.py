from datetime import datetime


def set_dates():
    # set time
    todays_date = datetime.now().day
    this_month = datetime.now().month

    thirty_day_months = [4, 6, 9, 11]
    twenty_day_months = [2]

    if this_month in thirty_day_months:
        number_of_days = 30
    elif this_month in twenty_day_months:
        number_of_days = 28
    else:
        number_of_days = 31

    whole_week = todays_date + 7

    if whole_week > number_of_days:
        whole_week -= number_of_days
        this_month += 1

    booking_ending_day = whole_week
    booking_ending_month = this_month

    return booking_ending_month, booking_ending_day



