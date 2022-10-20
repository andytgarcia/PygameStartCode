import pygame

# start of program
pygame.init()  # start engine
FPS = 60  # 60 frames per second
fpsClock = pygame.time.Clock
screen = pygame.display.set_mode((1280, 720))
gameOver = False

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    pygame.display.flip()
 