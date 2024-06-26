'''
Author: peterdavydov
Project: Ping Pong Game
Tools: Python 3
Version: 1.0
'''


import pygame
import time

WIDTH, HEIGHT = 1000, 650
fps = 60

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 80)
text1 = font.render("FAIL PLAYER1 WINNER!", True, pygame.Color("Red"))
text2 = font.render("FAIL PLAYER2 WINNER!", True, pygame.Color("Red"))

player1 = pygame.Rect(100, HEIGHT // 2 - 72, 20, 150)
player2 = pygame.Rect(WIDTH - 100, HEIGHT // 2 - 72, 20, 150)
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)
speed_x = 3
speed_y = 3

game = True
while game:
    clock.tick(fps)
    screen.fill(pygame.Color("Black"))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and player2.top > 3:
        player2.top -= 4
    if key[pygame.K_DOWN] and player2.bottom < HEIGHT - 3:
        player2.bottom += 4
    if key[pygame.K_w] and player1.top > 3:
        player1.top -= 4
    if key[pygame.K_s] and player1.bottom < HEIGHT - 3:
        player1.bottom += 4

    if ball.x + 10 == player1.x + 10 and  player1.y - 140 <= ball.y <= player1.y + 140:
        speed_x = -speed_x
    if ball.x + 10 == player2.x - 10 and  player2.y - 140 <= ball.y <= player2.y + 140:
        speed_x = -speed_x

    if ball.x >= WIDTH:
        speed_x = -4
        game = False
        screen.blit(text1, [200, 325])
    if ball.x <= 0:
        speed_x = 4
        game = False
        screen.blit(text2, [200, 325])
    if ball.y >= HEIGHT:
        speed_y = -4
    if ball.y <= 0:
        speed_y = 4

    ball.x += speed_x
    ball.y += speed_y

    pygame.draw.rect(screen, pygame.Color("White"), player1)
    pygame.draw.rect(screen, pygame.Color("White"), player2)
    pygame.draw.circle(screen, pygame.Color("White"), ball.center, 10)

    pygame.display.flip()

pygame.display.flip()
time.sleep(2)
pygame.quit()