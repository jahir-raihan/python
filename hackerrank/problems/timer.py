
class Timer:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def next_second(self):
        self.second += 1
        self.next_min()

    def prev_second(self):
        self.second -= 1
        self.prev_min()

    def next_min(self):
        if self.second > 59:
            self.minute += 1
            self.second = self.__min_sec(self.second)
            self.next_hour()

    def next_hour(self):
        if self.minute > 59:
            self.hour += 1
            self.minute = self.__min_sec(self.minute)

    def prev_min(self):
        if self.second < 0:
            self.minute -= 1
            self.second = self.__min_sec(self.second)
            self.prev_hour()

    def check(self, time):
        return f'0{time}' if time < 10 else time

    def prev_hour(self):
        if self.minute < 0:
            self.hour -= 1
            self.minute = self.__min_sec(self.minute)

    def __min_sec(self, tm):
        return tm % 60

    def __hour(self, th):
        return th % 24

    def __str__(self):
        hour = self.check(self.__hour(self.hour))
        minute = self.check(self.minute)
        second = self.check(self.second)
        return f'{hour}:{minute}:{second}'


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()

print(timer)
for i in range(65):
    timer.prev_second()
print(timer)

