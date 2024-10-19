#year = int(input("Please enter the year: "))

count = 0
for year in range(1,2025):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        count = count + 1
    #    print(year, "The year is a leap year!")
    #else:
    #    print(year, "The year is not a leap year!")
print(count)