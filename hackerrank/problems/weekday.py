class WeekDayError(Exception):
    pass


class Weeker:
    __days = 0
    __weeks = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

    def __init__(self, day):
        if day not in Weeker.__weeks:
            raise WeekDayError
        else:
            self.__day = day

    def __str__(self):
        return self.__day

    def add_days(self, n):
        Weeker.__days += n
        weekday_c = Weeker.__days % 7
        self.__day = Weeker.__weeks[weekday_c+1]

    def subtract_days(self, n):
        Weeker.__days -= n
        weekday_c = Weeker.__days % -7
        self.__day = Weeker.__weeks[weekday_c+1]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(3)
    print(weekday)

except WeekDayError:
    print("Sorry, I can't serve your request.")