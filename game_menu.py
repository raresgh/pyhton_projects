import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pygame
import time
import random

players = {}
pygame.mixer.init()
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.load("C:/Users/rares/OneDrive/Desktop/python_curs/lectia 15(modul 2)/background.mp3")
pygame.mixer.music.play(start = 35)
def menu():
    global play_bt, control_bt, instruction_bt, exit_bt, window
    window = tk.Tk()
    window.geometry("500x370+520+200")

    bg = PhotoImage(file = "C:/Users/rares/OneDrive/Desktop/python_curs/lectia 15(modul 2)/cityskyline.png")
    my_label = tk.Label(window,image = bg)
    my_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

    play_bt = tk.Button(
        window,
        text = "Play",
        width = 25,
        height = 2,
        command = play,
        font = (10),
        bg = "#00e3df",
        fg = "black",
        relief = tk.FLAT
    )
    play_bt.pack(pady = 30)

    control_bt = tk.Button(
        window,
        text = "Controls",
        width = 25,
        height = 2,
        command = control,
        font = (10),
        bg= "#00e3df",
        fg = "black",
        relief = tk.FLAT
    )
    control_bt.pack(pady = 0 )

    instruction_bt = tk.Button(
        window,
        text = "Intructions",
        width = 25,
        height = 2,
        command = instruction,
        font = (10),
        bg = "#00e3df",
        fg = "black",
        relief = tk.FLAT
    )
    instruction_bt.pack(pady = 30)

    exit_bt = tk.Button(
        window,
        text = "Exit",
        width = 25,
        height = 2,
        command = exit_func,
        font = (10),
        bg = "#00e3df",
        fg = "black",
        relief = tk.FLAT
    )
    exit_bt.pack(pady = 0)

    window.mainloop()

def play():
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



    while True:
        #assigning keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
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
        pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

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


    

def control():
    ctrl = tk.Toplevel()
    ctrl.geometry("350x370+169+200")
    bg1 = PhotoImage(file = "C:/Users/rares/OneDrive/Desktop/python_curs/lectia 15(modul 2)/cityskyline.png")
    my_label1 = tk.Label(ctrl,image = bg1)
    my_label1.place(x = 0, y = 0, relwidth = 1, relheight = 1)

    up = tk.Button(
        ctrl,
        text = "↑", 
        font = (30),
        width = 15,
        bg = "#00e3df",
        relief = tk.FLAT
    )
    up.grid(row = 0, column = 0, padx = 20, pady = 20)

    left = tk.Button(
        ctrl,
        text = "←", 
        font = (30),
        width = 15,
        bg = "#00e3df",
        relief = tk.FLAT
    )
    left.grid(row = 1, column = 0, padx = 20, pady = 20)

    right = tk.Button(
        ctrl,
        text = "→", 
        font = (30),
        width = 15,
        bg = "#00e3df",
        relief = tk.FLAT
    )
    right.grid(row = 2, column = 0, padx = 20, pady = 20)

    down = tk.Button(
        ctrl,
        text = "↓", 
        font = (30),
        width = 15,
        bg = "#00e3df",
        relief = tk.FLAT
    )
    down.grid(row = 3, column = 0, padx = 20, pady = 20)

    space = tk.Button(
        ctrl,
        text = "Space", 
        font = (30),
        width = 15,
        bg = "#00e3df",
        relief = tk.FLAT
    )
    space.grid(row = 4, column = 0, padx = 20, pady = 20)

    up_label = tk.Label(ctrl, text = "Move forward", bg = "#7376cf")
    left_label = tk.Label(ctrl, text = "Move left", bg = "#7376cf")
    right_label = tk.Label(ctrl, text = "Move right", bg = "#7376cf")
    down_label = tk.Label(ctrl, text = "Move back", bg = "#7376cf")
    space_label = tk.Label(ctrl, text = "Jump", bg = "#7376cf")
    up_label.grid(row = 0, column = 1, padx = 20, pady = 20)
    left_label.grid(row = 1, column = 1, padx = 20, pady = 20)
    right_label.grid(row = 2, column = 1, padx = 20, pady = 20)
    down_label.grid(row = 3, column = 1, padx = 20, pady = 20)
    space_label.grid(row = 4, column = 1, padx = 20, pady = 20)

    ctrl.mainloop()


def instruction():
    instr = tk.Toplevel()
    instr.geometry("500x180+520+600")

    bg2 = PhotoImage(file = "C:/Users/rares/OneDrive/Desktop/python_curs/lectia 15(modul 2)/cityskyline.png")
    my_label2 = tk.Label(instr,image = bg2)
    my_label2.place(x = 0, y = 0, relwidth = 1, relheight = 1)


    label = tk.Label(
        instr,
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ac tincidunt vitae semper quis lectus nulla at volutpat diam. Sit amet purus gravida quis blandit turpis. Vestibulum morbi blandit cursus risus at ultrices. Felis eget nunc lobortis mattis aliquam faucibus purus. Amet nulla facilisi morbi tempus iaculis urna id volutpat. Nibh mauris cursus mattis molestie a iaculis at erat pellentesque. Ultrices dui sapien eget mi proin sed libero enim sed. Id diam vel quam elementum pulvinar. Eget sit amet tellus cras adipiscing enim eu. Scelerisque eu ultrices vitae auctor eu augue. Massa sed elementum tempus egestas sed. At in tellus integer feugiat scelerisque varius morbi enim nunc. Pulvinar mattis nunc sed blandit libero volutpat sed cras. Ac tortor dignissim convallis aenean et tortor at.",
        wraplength = 490,
        justify = CENTER,
        bg = "#7376cf"
    )
    label.pack()

    instr.mainloop()


def exit_func():
    msg = messagebox.askquestion("Exit","Are you sure you want to exit?")
    if msg == "yes":
        exit()


menu()



