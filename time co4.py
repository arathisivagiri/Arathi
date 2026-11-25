class Time:
    def __init__(self):
        self.__h = int(input("Enter the time in hour: "))
        self.__m = int(input("Enter the time in minute: "))
        self.__s = int(input("Enter the time in second: "))

    def __add__(self, tob2):
        hour = self.__h + tob2.__h
        minute = self.__m + tob2.__m
        second = self.__s + tob2.__s

        minute = minute + second // 60
        second = second % 60

        hour = hour + minute // 60
        minute = minute % 60

        hour = hour % 24

        return hour, minute, second


print("Enter the time of first object:")
tob1 = Time()

print("Enter the time of second object:")
tob2 = Time()

print("Sum of two times (Hour, Minute, Second):", tob1 + tob2)
