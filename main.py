import random
import pygame
from time import sleep

pygame.init()

screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Snake Game")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

apples = 0

font = pygame.font.SysFont(None, 50)


def num_apples():
    txt = font.render(str(apples), True, (255, 255, 255))
    screen.blit(txt, (5, 5))


font_end = pygame.font.SysFont(None, 50)

gameOver = False


def game_over():
    global gameOver
    txt_end = font_end.render("GAME OVER", True, (255, 255, 255))
    screen.blit(txt_end, (150, 250))
    gameOver = True


snake = [[200, 100], [150, 100], [100, 100]]

X = 200
Y = 100
moveX = 0
moveY = 0

Xr = random.randrange(0, 500, 50)
Yr = random.randrange(0, 500, 50)

old_X = 0
old_Y = 0

running = True
while running:

    screen.fill((0, 140, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if moveX == 1:
                    moveX = 1
                    moveY = 0
                else:
                    old_X = moveX
                    old_Y = moveY
                    moveX = -1
                    moveY = 0

            if event.key == pygame.K_RIGHT:
                if moveX == -1:
                    moveX = -1
                    moveY = 0
                else:
                    old_X = moveX
                    old_Y = moveY
                    moveX = 1
                    moveY = 0

            if event.key == pygame.K_UP:
                if moveY == -1:
                    moveX = 0
                    moveY = -1
                else:
                    old_X = moveX
                    old_Y = moveY
                    moveX = 0
                    moveY = 1

            if event.key == pygame.K_DOWN:
                if moveY == 1:
                    moveX = 0
                    moveY = 1
                else:
                    old_X = moveX
                    old_Y = moveY
                    moveX = 0
                    moveY = -1

    if moveX == -1:
        if round(Y, 2) % 50 == 0:
            X = round(X - 50, 2)
        else:
            if old_Y == 1:
                Y = round(Y - 50, 2)
            else:
                Y = round(Y + 50, 2)

    if moveX == 1:
        if round(Y, 2) % 50 == 0:
            X = round(X + 50, 2)
        else:
            if old_Y == 1:
                Y = round(Y - 50, 2)
            else:
                Y = round(Y + 50, 2)

    if moveY == -1:
        if round(X, 2) % 50 == 0:
            Y = round(Y + 50, 2)
        else:
            if old_X == 1:
                X = round(X + 50, 2)
            else:
                X = round(X - 50, 2)

    if moveY == 1:
        if round(X, 2) % 50 == 0:
            Y = round(Y - 50, 2)
        else:
            if old_X == 1:
                X = round(X + 50, 2)
            else:
                X = round(X - 50, 2)

    if X < 0:
        game_over()
    elif X > 450:
        game_over()

    if Y < 0:
        game_over()
    elif Y > 450:
        game_over()

    if X == Xr and Y == Yr:
        try_again = True
        while try_again:
            Xr = random.randrange(0, 500, 50)
            Yr = random.randrange(0, 500, 50)
            try_again = False
            for i in range(len(snake)):
                if snake[i][0] == Xr and snake[i][1] == Yr:
                    try_again = True

        pygame.draw.rect(screen, (111, 255, 0), pygame.Rect(Xr, Yr, 50, 50))
        snake.append([0, 0])
        apples = apples + 1

    if moveX != 0 or moveY != 0:
        for i in range(len(snake)-1, -1, -1):
            if i == 0:
                snake[0][0] = X
                snake[0][1] = Y
            else:
                snake[i][0] = snake[i-1][0]
                snake[i][1] = snake[i-1][1]

    for i in range(len(snake)):
        if i == 0:
            pygame.draw.rect(screen, (111, 255, 0), pygame.Rect(snake[i][0], snake[i][1], 50, 50), 20)
        else:
            pygame.draw.rect(screen, (111, 255, 0), pygame.Rect(snake[i][0], snake[i][1], 50, 50))

    pygame.draw.rect(screen, (252, 28, 3), pygame.Rect(Xr, Yr, 50, 50))
    num_apples()

    for i in range(len(snake)):
        for j in range(len(snake)):
            if i == j:
                pass
            else:
                if snake[i][0] == snake[j][0] and snake[i][1] == snake[j][1]:
                    game_over()

    pygame.display.update()
    sleep(0.15)

    if gameOver is True:
        sleep(3)
        running = False
