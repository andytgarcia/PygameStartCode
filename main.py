import random

import pygame

import time

player1 = {"x": 640,
          "y": 360,
          "oldx": 640,
          "oldy": 360,
          "size": 10,
          "speed": .5,
          "color": pygame.Color(255, 0, 0),
           "lastDir": "right",
           "shotTimeStamp": 0,
           "nextShot": 0,
           "score": 0}


player2 =  {"x": 840,
          "y": 160,
          "oldx": 840,
          "oldy": 160,
          "size": 10,
          "speed": .5,
          "color": pygame.Color(0, 0, 255),
            "lastDir": "right",
            "shotTimeStamp": 0,
            "nextShot": 0,
            "score": 0}

map = []

bullets = [] #list of bullets in the game
"""
bullets[0] = x
bullets[1] = y
bullets[2] = size
bullets[3] = player
bullets[4] = color
bullets[5] = x velocity
bullets[6] = y velocity
"""


def getPlayerCollisionRectangle(player):
    return pygame.Rect(player["x"] - player["size"], player["y"] - player["size"], player["size"] * 2, player["size"] * 2)

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

def drawPlayers():
    pygame.draw.circle(screen, player1["color"], (player1["x"], player1["y"]), player1["size"])
    pygame.draw.circle(screen, player2["color"], (player2["x"], player2["y"]), player2["size"])


def drawBullets():
    for b in bullets:
        pygame.draw.circle(screen, b["color"], (b["x"], b["y"]), b["size"])


def playerMovement():
    keys = pygame.key.get_pressed()
    player1["oldx"] = player1["x"]
    player1["oldy"] = player1["y"]

    player2["oldx"] = player2["x"]
    player2["oldy"] = player2["y"]

    if keys[pygame.K_d]:
        player1["x"] += player1["speed"]
        player1["lastDir"] = "right"
    if keys[pygame.K_s]:
        player1["y"] += player1["speed"]
        player1["lastDir"] = "down"
    if keys[pygame.K_a]:
        player1["x"] -= player1["speed"]
        player1["lastDir"] = "left"
    if keys[pygame.K_w]:
        player1["y"] -= player1["speed"]
        player1["lastDir"] = "up"
    if keys[pygame.K_f] and player1["nextShot"] < time.time_ns():
        if player1["lastDir"] == "right":
            bullets.append({"x": player1["x"],
                            "y": player1["y"],
                            "size": 5,
                            "owner": "p1",
                            "color": player1["color"],
                            "xvel": 20,
                            "yvel": 0})
            player1["nextShot"] = time.time_ns() + 100000000

        elif player1["lastDir"] == "left":
            bullets.append({"x": player1["x"],
                                "y": player1["y"],
                                "size": 5,
                                "owner": "p1",
                                "color": player1["color"],
                                "xvel": -20,
                                "yvel": 0})
            player1["nextShot"] = time.time_ns() + 100000000
        elif player1["lastDir"] == "up":
            bullets.append({"x": player1["x"],
                            "y": player1["y"],
                            "size": 5,
                            "owner": "p1",
                            "color": player1["color"],
                            "xvel": 0,
                            "yvel": -20})
            player1["nextShot"] = time.time_ns() + 100000000

        elif player1["lastDir"] == "down":
            bullets.append({"x": player1["x"],
                            "y": player1["y"],
                            "size": 5,
                            "owner": "p1",
                            "color": player1["color"],
                            "xvel": 0,
                            "yvel": 20})
            player1["nextShot"] = time.time_ns() + 100000000





    #p2
    if keys[pygame.K_RIGHT]:
        player2["x"] += player2["speed"]
        player2["lastDir"] = "right"
    if keys[pygame.K_DOWN]:
        player2["y"] += player2["speed"]
        player2["lastDir"] = "down"
    if keys[pygame.K_LEFT]:
        player2["x"] -= player2["speed"]
        player2["lastDir"] = "left"
    if keys[pygame.K_UP]:
        player2["y"] -= player2["speed"]
        player2["lastDir"] = "up"
    if keys[pygame.K_m] and player2["nextShot"] < time.time_ns():
        if player2["lastDir"] == "right":
            bullets.append({"x": player2["x"],
                            "y": player2["y"],
                            "size": 5,
                            "owner": "p2",
                            "color": player2["color"],
                            "xvel": 20,
                            "yvel": 0})
            player2["nextShot"] = time.time_ns() + 100000000

        elif player2["lastDir"] == "left":
            bullets.append({"x": player2["x"],
                                "y": player2["y"],
                                "size": 5,
                                "owner": "p2",
                                "color": player2["color"],
                                "xvel": -20,
                                "yvel": 0})
            player2["nextShot"] = time.time_ns() + 100000000
        elif player2["lastDir"] == "up":
            bullets.append({"x": player2["x"],
                            "y": player2["y"],
                            "size": 5,
                            "owner": "p2",
                            "color": player2["color"],
                            "xvel": 0,
                            "yvel": -20})
            player2["nextShot"] = time.time_ns() + 100000000

        elif player2["lastDir"] == "down":
            bullets.append({"x": player2["x"],
                            "y": player2["y"],
                            "size": 5,
                            "owner": "p2",
                            "color": player2["color"],
                            "xvel": 0,
                            "yvel": 20})
            player2["nextShot"] = time.time_ns() + 100000000



def updateBullets():
    for b in bullets:
        b["x"] += b["xvel"] #x += x velocity
        b["y"] += b["yvel"] #y += y velocity
        if ifOffScreen(b["x"], b["y"]):
            bullets.remove(b)

        player1Rectangle = getPlayerCollisionRectangle(player1)
        player2Rectangle = getPlayerCollisionRectangle(player2)
        bulletRect = pygame.Rect(b["x"] - b["size"], b["y"] - b["size"], b["size"] * 2, b["size"] * 2)
        if pygame.Rect.colliderect(bulletRect, player1Rectangle) and b["owner"] == "p2":
            player2["score"] += 100
            newRound()
        if pygame.Rect.colliderect(bulletRect, player2Rectangle) and b["owner"] == "p1":
            player1["score"] += 100
            newRound()

        #check this bullet for collision in every wall
        for wall in map:
            bulletRect = pygame.Rect(b["x"] - b["size"], b["y"] - b["size"], b["size"] * 2, b["size"] * 2)
            if pygame.Rect.colliderect(wall, bulletRect):
                b["xvel"] *= -1
                b["yvel"] *= -1


def ifOffScreen(x, y):
    if x <0 or x > 1280 or y < 0 or y > 720:
        return True
    else:
        return False

def checkPlayerCollision(player):
    playRect = getPlayerCollisionRectangle(player)
    for wall in map:
        if pygame.Rect.colliderect(playRect, wall):
            player["x"] = player["oldx"]
            player["y"] = player["oldy"]
            print("Collision")
            #player["color"] = (random.randint(0, 255),
             #                   random.randint(0, 255),
              #                  random.randint(0, 255))




def drawPlayerCollisionBox(player):
    pygame.draw.rect(screen, pygame.Color(255, 0, 255), getPlayerCollisionRectangle(player), 1)


def newRound():
    bullets.clear()
    player1["x"] = 100
    player1["y"] = 100
    player2["x"] = 900
    player2["y"] = 600


def drawHUD():
    textSurface = myfont.render("Player 1 Score: " + str(player1["score"]), True, (255, 255, 255))
    screen.blit(textSurface, (50, 30))
    textSurface = myfont.render("Player 2 Score: " + str(player2["score"]), True, (255, 255, 255))
    screen.blit(textSurface, (1050, 30))

# start of program
pygame.init()  # start engine
pygame.font.init()
myfont = pygame.font.SysFont('Times New Roman', 23)
FPS = 60  # 60 frames per second
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))
gameOver = False
createmap1()

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    playerMovement()


    updateBullets()
    checkPlayerCollision(player1)
    checkPlayerCollision(player2)


    #draw code
    clearScreen()
    drawMap()
    drawBullets()
    drawPlayers()
    drawPlayerCollisionBox(player1)
    drawPlayerCollisionBox(player2)
    drawHUD()


    pygame.display.flip()
