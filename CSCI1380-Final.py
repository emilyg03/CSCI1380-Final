# # Testing pygame installation
# import pygame
# pygame.init()
# print(pygame.ver)

# Enviorment
import pygame  # Library to create the game
import random  # Used for the position of the apple
from pyvirtualdisplay import Display

pygame.init()

# Game window
screen_width = 600  # Width
screen_height = 400  # Height
game_screen = pygame.display.set_mode((screen_width, screen_height))  # Setting up the game screen
pygame.display.set_caption('Snake Game_Emily & Dylan')  # Title

# Settings / Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)  # Snake
red = (255, 0, 0)  # Apple

# Size of snake
snake_size = 10  # Segments 10x10
snake_length = 5  # Snake length

# Clock object to control the frame rate of the game
clock = pygame.time.Clock()
fps = 15  # FPS to control how fast game runs (speed of snake)

# Initial direction and score
direction = 'RIGHT'
score = 0

# Empty list to store the snake's body segments
snake_segments = []
for i in range(snake_length):
    x = 250 - (snake_size * i)  # Position based on index (of each segment)
    y = 200  # Y-coordinate of all segments initially (200)
    segment = pygame.Rect(x, y, snake_size, snake_size)  # Rectangle for each snake segment
    snake_segments.append(segment)  # Adding segment to list

apple_size = 10  # Size of the apple (10x10 pixels)
apple_position = (  # Randomly position apple within bounds of game screen
    random.randrange(0, screen_width // apple_size) * apple_size,
    random.randrange(0, screen_height // apple_size) * apple_size
)
apple = pygame.Rect(apple_position[0], apple_position[1], apple_size,
                    apple_size)  # Rectangle for the apple at the random position

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If player clicks window close button
            running = False  # Exit
        elif event.type == pygame.KEYDOWN:  # If a key is pressed, Change direction
            if event.key == pygame.K_UP and direction != 'DOWN':  # Down arrow
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':  # Up arrow
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':  # Right arrow
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':  # Left arrow
                direction = 'RIGHT'

    # Moving snake based on current direction
    x, y = snake_segments[0].topleft
    if direction == 'UP':
        y -= snake_size
    elif direction == 'DOWN':
        y += snake_size
    elif direction == 'LEFT':
        x -= snake_size
    elif direction == 'RIGHT':
        x += snake_size

    # Creating a new head for the snake at the new position
    new_head = pygame.Rect(x, y, snake_size, snake_size)
    snake_segments.insert(0, new_head)  # Inserting new head at beginning f snake list

    # Checking for collision with screen boundaries or itself
    if (snake_segments[0].left < 0 or snake_segments[0].right > screen_width or
            snake_segments[0].top < 0 or snake_segments[0].bottom > screen_height or
            snake_segments[0] in snake_segments[1:]):  # Checking if the snake collides with itself
        running = False  # Game over

    # Checking for collision(eating) with apple
    if snake_segments[0].colliderect(apple):
        score += 5  # Score update
        apple_position = (random.randrange(0, screen_width // apple_size) * apple_size,
                          random.randrange(0, screen_height // apple_size) * apple_size)
        apple = pygame.Rect(apple_position[0], apple_position[1], apple_size, apple_size)  # Create new apple
    else:
        snake_segments.pop()  # Remove the last segment if no apple eaten / it moves

    # Game screen backround (black)
    game_screen.fill(black)
    # Drawing snake segment (Green)
    for segment in snake_segments:
        pygame.draw.rect(game_screen, green, segment)
    # Drawing apple (Red)
    pygame.draw.rect(game_screen, red, apple)

    # Display score
    font = pygame.font.Font(None, 36)  # font, size
    score_text = font.render('Score: ' + str(score), True, white)  # Render teh score
    game_screen.blit(score_text, (10, 10))  # Location, top-left

    # Update the screen
    pygame.display.update()
    clock.tick(fps)  # Control FPS by setting it to something

# Game over scrren
game_screen.fill(black)  # Clear screen
game_over_text = font.render('Game Over', True, red)  # Render text
game_screen.blit(game_over_text,
                 (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2))  # Location, center
pygame.display.update()  # Update screen to show 'Game Over'
pygame.time.wait(2000)  # Wait before  quiting

# Quit and close window
pygame.quit()
