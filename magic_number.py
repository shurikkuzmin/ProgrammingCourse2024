number = 56

sum_dividers = 0
for i in range(1,number):
   if number%i == 0:
       sum_dividers = sum_dividers + i
       print("Divider", i)
print("Sum_dividers", sum_dividers)