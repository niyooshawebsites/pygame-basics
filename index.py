import pygame

# initialize pygame
pygame.init()

# setting the screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("assets/ufo.png")
pygame.display.set_icon(icon)

# player
playerImg = pygame.transform.scale(
    pygame.image.load("assets/player.png").convert_alpha(), (64, 64)
)
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# # enemy
# enemyImg = pygame.transform.scale(
#     pygame.image.load("assets/enemy.png").convert_alplha(), (64, 64)
# )


def player(x, y):
    # drawing the player on the screen
    screen.blit(playerImg, (x, y))


# game loop
running = True
while running:
    # screen color - RGB
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is presssed and check whether is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_UP:
                playerY_change = -0.5
            if event.key == pygame.K_DOWN:
                playerY_change = 0.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change

    # boundaries
    if playerX < 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    elif playerY < 0:
        playerY = 0
    elif playerY >= 534:
        playerY = 534

    player(playerX, playerY)
    pygame.display.update()
