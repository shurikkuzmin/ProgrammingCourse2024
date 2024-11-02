import random

array = ["apple","orange","donkey","monkey","capibara","leopard"]
computer_word = random.choice(array)
my_word = len(computer_word)*'*'

# for attempt in range(5):
#     print(my_word)
#     letter = input("Please enter a letter: ")
#     for i in range(len(computer_word)):
#         if letter == computer_word[i]:
#             my_word[i] = letter[0]
