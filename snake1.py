import pygame
import time
import random

pygame.mixer.init()
pygame.mixer.music.set_volume(0.2)

snake_speed = 15

#windowsize
window_x = 720
window_y = 480

#defining colors
black = pygame.Color(132, 93, 168)
white = pygame.Color(255, 255, 255)
red = pygame.Color(224, 201, 195)
green = pygame.Color(2, 15, 199)
blue = pygame.Color(0, 0, 255)

#constructing the pygame instance
pygame.init()

#init window
pygame.display.set_caption("S Game")
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

snake_position = [100, 50]

snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

#fruit_position = [random.randrange(40, window_x - 40), random.randrange(40, window_y - 40)]

fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]

fruit_spawn = True

#direction
direction = "RIGHT"
change_to = direction

#score
score = 0

#displaying score function

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)

    score_surface = score_font.render('Score : ' + str(score), True, color)

    score_rect = score_surface.get_rect()

    game_window.blit(score_surface, score_rect)

#game over
def game_over():
    my_font = pygame.font.SysFont("times new roman", 50)

    game_over_surface = my_font.render('Yout Score is: ' + str(score), True, red)

    game_over_rect = game_over_surface.get_rect()

    game_over_rect.midtop = (window_x/2, window_y/4)

    game_window.blit(game_over_surface, game_over_rect)

    pygame.display.flip()

    time.sleep(2)

    pygame.quit()

    quit()

while True:
    #assigning keys
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"
    
    #movement
    if direction == "UP":
        snake_position[1] -= 10
    if direction == "DOWN":
        snake_position[1] += 10
    if direction == "LEFT":
        snake_position[0] -= 10
    if direction == "RIGHT":
        snake_position[0] += 10

    #snake growing mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
        pygame.mixer.music.load("C:/Users/rares/OneDrive/Desktop/python_curs/lectia 16(modul 2)/sound.wav")
        pygame.mixer.music.play()
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]  

    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    #Game over conditions

    if snake_position[0] > window_x - 10:
        snake_position[0] = 0

    if snake_position[1] > window_y - 10:
        snake_position[1] = 0

    if snake_position[1] < 0:
        snake_position[1] = window_y-10

    if snake_position[0] < 0:
        snake_position[0] = window_x-10

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    
    #displaying score

    show_score(1, white, "times new roman", 20)

    #Refresh game screen

    pygame.display.update()

    fps.tick(snake_speed)
