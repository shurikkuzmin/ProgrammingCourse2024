#year = int(input("Please enter the year: "))

count = 0
#for year in range(1,2025):
year = 1
while year < 2025:
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        count = count + 1
    year = year + 1
print(count)