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
clock = pygame.time.Clock()
fps = 15  # frames per second
direction = 'RIGHT' # snake’s initial direction
score = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # the close button
            running = False
    # Game logic, drawing code, and screen update will go here
    pygame.display.update()
    clock.tick(fps)

# snake object
snake_segments = []
snake_size = 10  # Size of each snake segment
snake_length = 5  # Initial length of the snake
for i in range(snake_length):
    x = 250 - (snake_size * i)
    y = 200
    segment = pygame.Rect(x, y, snake_size, snake_size) # single square
    snake_segments.append(segment)

# apple object


# drawing snake and apple


# controlling snake 
for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

# position updates


# collision checks


# what hapens snake eats apple


# score
font = pygame.font.Font(None, 36) 
score_text = font.render('Score: ' + str(score), True, white) # smoothing
game_screen.blit(score_text, (10, 10))

# game end / over
game_screen.fill(black)
game_over_text = font.render('Game Over', True, red)
game_screen.blit(game_over_text, (screen_width//2 - game_over_text.get_width()//2, screen_height//2))
pygame.display.update()
pygame.time.wait(2000)  # Wait two seconds before closing
pygame.quit()
