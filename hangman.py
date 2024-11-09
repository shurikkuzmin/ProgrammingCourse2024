import tkinter

window = tkinter.Tk()  
window.geometry('600x600')  
window.title('Hangman')
window.mainloop()

# import random

# array = ["apple","orange","donkey","monkey","capibara","leopard"]
# computer_word = random.choice(array)
# my_word = len(computer_word)*'*'

# for attempt in range(int(1.5 * len(computer_word))):
#     print(my_word)
#     letter = input("Please enter a letter: ")
#     for i in range(len(computer_word)):
#         if letter == computer_word[i]:
#             my_word = my_word[:i]+letter+my_word[i+1:]
#     if my_word == computer_word:
#         print("You've got it!")
#         break
# else:
#     print("You are loser!")