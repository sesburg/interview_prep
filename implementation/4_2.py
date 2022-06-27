# Given N (0 <= N <= 23), return the number of times that 3 is displayed.
class Time:
    def __init__(self, h = 0, m = 0, s = 0):
        self.hour = h
        self.minute = m
        self.second = s
    
    def __str__(self):
        return str(self.hour) + str(self.minute) + str(self.second)

    def __repr__(self):
        return str(self)
           
    
    def has_Three(self):
        if "3" in (str(self)):
            return True
        return False

    def increment(self):
        self.second += 1
        if self.second >= 60:
            self.second = 0
            self.minute += 1
            if self.minute >= 60:
                self.minute = 0
                self.hour += 1
    
    def is_earlier_than(self, t):
        if self.hour < t.hour:
            return True
        if self.hour == t.hour and self.minute < t.minute:
            return True
        if self.hour == t.hour and self.minute == t.minute and self.second < t.second:
            return True
        return False

def count_three(n):
    res = 0
    t = Time()
    t_end = Time(n, 59, 59)
    while t.is_earlier_than(t_end):
        if t.has_Three():
            res += 1
        t.increment()
    return res

n = int(input())
print(count_three(n))

