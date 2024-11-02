for number in range(2,10001):
    sum_dividers = 0
    for i in range(1,number):
        if number%i == 0:
            sum_dividers = sum_dividers + i
    if sum_dividers == number:
        print("This is a magic number", number)
