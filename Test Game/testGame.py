import pygame, sys
from pygame.locals import *

FLOOR = 0
WALL = 1
DOOR = 2
PLANT = 3

TILESIZE = 128
MAPWIDTH = 10
MAPHEIGHT = 8

BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
GREY = (143, 143, 143)
RED = (255, 0, 0)

#-------------------------------

textures = {
    FLOOR: BROWN,
    WALL: GREY,
    DOOR: BLACK,
    PLANT: GREEN,
}

#-------------------------------

entranceRoom = [
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
    [WALL, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
    [WALL, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
    [WALL, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
    [WALL, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
    [WALL, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
    [WALL, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]
]



#-------------------------------

PLAYER = 5
playerTileX = 5
playerTileY = 5
playerPos = [TILESIZE * playerTileX, TILESIZE * playerTileY]

#-------------------------------

curRoom = entranceRoom
curTile = FLOOR
fpsClock = pygame.time.Clock()

#-------------------------------
def interact(tile):
    if tile == FLOOR:
        pygame.draw.rect(DISPLAYSURF, BLACK, (TILESIZE *4 ,TILESIZE *4 , TILESIZE * 6, TILESIZE * 4))
        fpsClock.tick(300)

#-------------------------------
        
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE))
pygame.display.set_caption("TEST DEMO")

#-------------------------------

while True:
    DISPLAYSURF.fill(BLACK)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            if (event.key == K_RIGHT) and playerTileX < 8:
                playerTileX += 1
                playerPos = [TILESIZE * playerTileX, TILESIZE * playerTileY]
            if(event.key == K_LEFT) and playerTileX > 1:
                playerTileX -= 1
                playerPos = [TILESIZE * playerTileX, TILESIZE * playerTileY]
            if(event.key == K_UP) and playerTileY > 1:
                playerTileY -= 1
                playerPos = [TILESIZE * playerTileX, TILESIZE * playerTileY]
            if(event.key == K_DOWN) and playerTileY < 6:
                playerTileY += 1
                playerPos = [TILESIZE * playerTileX, TILESIZE * playerTileY]

            if(event.key == K_SPACE):
                interact(curTile)

    for rw in range(MAPWIDTH):
        for cl in range(MAPHEIGHT):
            pygame.draw.rect(DISPLAYSURF, textures[curRoom[cl][rw]], (TILESIZE * rw, TILESIZE * cl, TILESIZE, TILESIZE))
    pygame.draw.rect(DISPLAYSURF, RED, (playerPos[0], playerPos[1], TILESIZE, TILESIZE))
    curTile = curRoom[playerTileY][playerTileX]
    pygame.display.update()


    
        
