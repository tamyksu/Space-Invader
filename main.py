import pygame

pygame.init()
# Screen
screen = pygame.display.set_mode((800, 600))

# backgroung
backgroung = pygame.image.load('space1.png')

# title
pygame.display.set_caption("Best Game")
icon = pygame.image.load('pope.png')
pygame.display.set_icon(icon)

# player
playerImage = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0
speed = 0.3

# Enemy
enemyImage = pygame.image.load('alien.png')
enemyX = 300
enemyY = 10
enemyX_change = 0
enemy_speed =0.3


def player(x, y):
    screen.blit(playerImage, (x, y))


def enemy(x, y):
    screen.blit(enemyImage, (x, y))


# Game loop
run = True
while run:
    screen.fill((0, 0, 0))

    # Background
    screen.blit(backgroung,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if playerY < 536:
                    playerY_change = speed

            if event.key == pygame.K_UP:
                if playerY > 64:
                    playerY_change = -speed

            if event.key == pygame.K_LEFT:
                if playerX >= 0:
                    playerX_change = -speed

            if event.key == pygame.K_RIGHT:
                if playerX < 736:
                    playerX_change = speed

        if event.type == pygame.KEYUP:
            playerX_change = 0
            playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change
    enemyX += enemy_speed
    if enemyX >= 736:
        enemy_speed = -enemy_speed
        enemyY += 15
    elif enemyX <= 0:
        enemy_speed = -enemy_speed
        enemyY += 15

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536
    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()
