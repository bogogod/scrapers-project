import pygame

pygame.init()

# Set up the display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_CAPTION = "Lool"
SCREEN_ICON = pygame.image.load("Assets\submachine-gun.png")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_CAPTION)
pygame.display.set_icon(SCREEN_ICON)

# Player
PLAYER_ICON = pygame.image.load("Assets\caveman.png")
STARTING_PLAYER_X = 370
STARTING_PLAYER_Y = 270
playerX = STARTING_PLAYER_X
playerY = STARTING_PLAYER_Y
playerSpeed = 0.1

def draw_player(x, y):
    screen.blit(PLAYER_ICON, (x, y))

# Game Loop
run = True
while run:
    screen.fill((0, 0, 0))  # Fill the screen
    draw_player(playerX, playerY) # Draw the player

    # Player movement
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        playerX += -playerSpeed
    elif key[pygame.K_d]:
        playerX += playerSpeed
    elif key[pygame.K_w]:
        playerY += -playerSpeed
    elif key[pygame.K_s]:
        playerY += playerSpeed
    if playerX < 0: playerX = 0
    if playerX > SCREEN_WIDTH - 64: playerX = SCREEN_WIDTH - 64
    if playerY < 0: playerY = 0
    if playerY > SCREEN_HEIGHT - 64: playerY = SCREEN_HEIGHT - 64

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If the user clicks the close button
            run = False

    # Update the display
    pygame.display.update()

pygame.quit()
