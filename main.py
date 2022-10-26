import pygame

player = {"x": 640,
          "y": 360,
          "size": 10,
          "speed": .5,
          "color": pygame.Color(255, 0, 255)}


map = []


def drawMap():
    for currentRect in map:
        #draw a rectangle
        pygame.draw.rect(screen, pygame.Color(0, 255, 255), currentRect)

def createmap1():
    map.append(pygame.Rect(400, 200, 100, 250))
    map.append(pygame.Rect(300, 100, 10, 500))
    map.append(pygame.Rect(0, 0, 1280, 10))
    map.append(pygame.Rect(0, 0, 10, 720))
    map.append(pygame.Rect(900, 100, 300, 10))


def clearScreen():

    pygame.draw.rect(screen, pygame.Color(0, 0, 0), (0,0, 1280, 720))

def drawPlayer():
    pygame.draw.circle(screen, player["color"], (player["x"], player["y"]), player["size"])



def playerMovement():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player["x"] += player["speed"]
    if keys[pygame.K_s]:
        player["y"] += player["speed"]
    if keys[pygame.K_a]:
        player["x"] -= player["speed"]
    if keys[pygame.K_w]:
        player["y"] -= player["speed"]


# start of program
pygame.init()  # start engine
FPS = 60  # 60 frames per second
fpsClock = pygame.time.Clock
screen = pygame.display.set_mode((1280, 720))
gameOver = False
createmap1()

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    playerMovement()

    #draw code
    clearScreen()
    drawMap()
    drawPlayer()

    pygame.display.flip()
