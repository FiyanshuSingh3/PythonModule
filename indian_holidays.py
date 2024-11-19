from datetime import date, timedelta

class IndianHolidayCalendar:
    def __init__(self, year=None):
        
        self.year = year if year else date.today().year
        self.fixed_holidays = {
            "Republic Day": date(self.year, 1, 26),
            "Independence Day": date(self.year, 8, 15),
            "Gandhi Jayanti": date(self.year, 10, 2),
            "Christmas": date(self.year, 12, 25),
            "Holi":date(self.year, 3, 25),
            "Good Friday":date(self.year, 3, 29),
            "Id-ul-Fitr":date(self.year, 4, 11),
            "Gandhi Jayanti":date(self.year, 10, 2),
            "Diwali":date(self.year, 10, 31),
        }
        self.movable_holidays = self.calculate_movable_holidays()

    def calculate_movable_holidays(self):
                                   """Calculate movable holidays based on the year."""
       
        diwali = date(self.year, 11, 12)  
        eid = date(self.year, 6, 17)  
        
        return {
            "Diwali": diwali,
            "Eid al-Fitr": eid,
        }

    def get_all_holidays(self):
                                  """Return a dictionary of all holidays."""
        return {**self.fixed_holidays, **self.movable_holidays}

    def is_holiday(self, check_date):
                                 """Check if a specific date is a holiday."""
        holidays = self.get_all_holidays()
        return check_date in holidays.values()

    def add_custom_holiday(self, name, holiday_date):
                                     """Add a custom holiday."""
        if isinstance(holiday_date, date):
            self.fixed_holidays[name] = holiday_date
        else:
            raise ValueError("Holiday date must be a valid `date` object.")


if __name__ == "__main__":
    calendar = IndianHolidayCalendar(2024)
    all_holidays = calendar.get_all_holidays()
    for name, holiday_date in all_holidays.items():
        print(f"{name}: {holiday_date}")
