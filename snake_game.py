# # test pygame installation
# import pygame
# pygame.init()
# print(pygame.ver)

# game enviorment
import pygame
pygame.init()

# game window
screen_width = 600
screen_height = 400
game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# settings (colors)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# gameloop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # the close button
            running = False
            
    pygame.display.update()

# fps control


# snake object


# apple object


# drawing snake and apple


# controlling snake 


# position updates


# collision checks


# what hapens snake eats apple


# score


# game end / over