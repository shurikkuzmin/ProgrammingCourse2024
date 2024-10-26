number = int(input("Please enter a number: "))

sum_all_digits = 0

while number > 0:
    sum_all_digits = sum_all_digits + number%10
    number = int((number - number%10) / 10)

print(sum_all_digits)