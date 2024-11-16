import pygame
import pygame.display
import pygame.image
import pygame.transform

pygame.init()

background = pygame.image.load("h0.png")
background = pygame.transform.scale(background,(1000, 1000))

screen_width = background.get_width()
screen_height = background.get_height()
screen = pygame.display.set_mode((screen_width, screen_height))

while True:
    screen.fill((102,2,60))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    screen.blit(background,(0,0))
    pygame.display.update()
# import tkinter
# from PIL import Image, ImageTk

# window = tkinter.Tk()  
# window.geometry('600x600')  
# window.title('Hangman')



# background = tkinter.PhotoImage(file = "h0.png")
# background=background.zoom(0.5, 0.5) 
# # Show image using label 
# background_label = tkinter.Label(window, image=background) 
# background_label.place(x = 0, y = 0) 

# window.mainloop()

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