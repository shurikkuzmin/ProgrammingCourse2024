import pygame
import pygame.display
import pygame.image
import pygame.transform
import pygame.font
import random

pygame.init()
pygame.font.init() 

font = pygame.font.SysFont('Comic Mono', 150)
font_end = pygame.font.SysFont('Ariel',200)

background = pygame.image.load("h0.png")
background = pygame.transform.scale(background,(1000, 1000))

screen_width = background.get_width()
screen_height = background.get_height()
screen = pygame.display.set_mode((screen_width, screen_height))

array = ["apple","orange","donkey","monkey","capibara","leopard"]
computer_word = random.choice(array)
my_word = len(computer_word)*'*'
number_of_attempts = int(1.4*len(computer_word))
attempt = 0
end_of_game = False
while True:
    screen.fill((102,2,60))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN and (not end_of_game):
            letter = pygame.key.name(event.key)
            for i in range(len(computer_word)):
                if letter == computer_word[i]:
                    my_word = my_word[:i]+letter+my_word[i+1:]
            attempt = attempt + 1
    text = font.render(my_word,True,(255,69,0))
    screen.blit(background,(0,0))
    screen.blit(text,(450,120))
    text = font.render(str(attempt) + " out of " + str(number_of_attempts), True, (0,255,0))
    screen.blit(text,(20,20))

    if attempt >= number_of_attempts:
        text = font_end.render("YOU LOST!", True, (0,255,0))
        text_rect = text.get_rect()
        text_rect.center = (int(screen_width/2), int(screen_height/2))
        screen.blit(text,text_rect)
        end_of_game = True
    elif my_word == computer_word:
        text = font_end.render("YOU WON!", True, (0,255,0))
        text_rect = text.get_rect()
        text_rect.center = (int(screen_width/2), int(screen_height/2))
        screen.blit(text,text_rect)
        end_of_game = True
    
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