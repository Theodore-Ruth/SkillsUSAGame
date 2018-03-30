import pygame, sys
from pygame.locals import *
import time
import random

FLOOR = 0
WALL = 1
DOOR = 2
PLANT = 3
PLAYER = 4
MENU = 5
ENTRANCEDRESSER = 6
LOCKEDLIVINGROOMDOOR = 7
EMPTYDRESSER = 8



TILESIZE = 128
MAPWIDTH = 10
MAPHEIGHT = 8

BLACK = (0, 0, 0, 255)
BROWN = (153, 76, 0, 255)
GREEN = (0, 255, 0, 255)
GREY = (143, 143, 143, 255)
RED = (255, 0, 0, 255)
WHITE =(255, 255, 255, 255)
BLUE = (0, 0, 255, 255)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

textures = {
    FLOOR: BROWN,
    WALL: GREY,
    DOOR: BLACK,
    PLANT: GREEN,
    MENU: BLACK,
    ENTRANCEDRESSER: BLUE,
    LOCKEDLIVINGROOMDOOR: BLACK,
    EMPTYDRESSER: BLUE
}

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

entranceRoom = [
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
    [WALL, ENTRANCEDRESSER, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
    [WALL, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
    [WALL, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, LOCKEDLIVINGROOMDOOR],
    [WALL, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, LOCKEDLIVINGROOMDOOR],
    [WALL, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
    [WALL, PLANT, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]
]

livingRoom = [
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
    [WALL, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, PLANT, WALL],
    [WALL, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
    [DOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
    [DOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
    [WALL, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
    [WALL, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]
]

fightRoom = [
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
    [MENU, MENU, MENU, MENU, MENU, MENU, MENU, MENU, MENU, MENU],
    [MENU, MENU, MENU, MENU, MENU, MENU, MENU, MENU, MENU, MENU]
]

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
livingRoomKey = 0
snack = 1

items = {
    livingRoomKey: 'Living Room Key',
    snack: 'Snack'
}

consumables = [items[snack]]

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

monster1 = {
    'Health': 1,
    'Damage': 1,
    'Speed': 1
}

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

playerTileX = 5
playerTileY = 5
playerPos = [TILESIZE * playerTileX, TILESIZE * playerTileY]

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

curRoom = entranceRoom
curTile = FLOOR

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def interact(tile, room):
    if tile == FLOOR:
        displayMessage('* Just a boring, wood floor', room)

    if tile == ENTRANCEDRESSER:
        displayMessage('*There was a key in the dresser', room)
        if(checkInventory()):
            displayMessage('*Got living room key', room)
            entranceRoom[playerTileY][playerTileX] = EMPTYDRESSER
            playerInventory.append(items[livingRoomKey])
        print(playerInventory)
    if tile == EMPTYDRESSER:
        displayMessage('*An empty dresser', room)
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def displayMessage(message, room):
    
    for rw in range(MAPWIDTH):
        for cl in range(MAPHEIGHT):
            pygame.draw.rect(DISPLAYSURF, textures[room[cl][rw]], (TILESIZE * rw, TILESIZE * cl, TILESIZE, TILESIZE))
    pygame.draw.rect(DISPLAYSURF, RED, (playerPos[0], playerPos[1], TILESIZE, TILESIZE))
    
    pygame.draw.rect(DISPLAYSURF, BLACK, (TILESIZE * 3, TILESIZE * (MAPHEIGHT - 2), TILESIZE * 4, TILESIZE / 2))

    textSurface = textFont.render(message, False, WHITE)
    DISPLAYSURF.blit(textSurface,((TILESIZE * 3) + (TILESIZE / 8), (TILESIZE * (MAPHEIGHT - 2)) + (TILESIZE / 8)))
    
    pygame.display.update()

    tempInt = 0
    while tempInt == 0:
        for textEvent in pygame.event.get():
            if textEvent.type == QUIT:
                pygame.quit()
                sys.exit()
            
            elif(textEvent.type == KEYDOWN):
                if(textEvent.key == K_SPACE):
                    tempInt = 1
                if(textEvent.key == K_ESCAPE):
                    tempInt = 1
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def changeRoom(room, direction):
    if (room == entranceRoom) and (direction == 'right'):
        return livingRoom
    
    if (room == livingRoom) and (direction =='left'):
        return entranceRoom
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def nextToDoor(room):
    if (room[playerTileY][playerTileX] == DOOR):
        return True
    else:
        return False

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def nextToWall(room):
    if (room[playerTileY][playerTileX] == WALL):
        return True
    
    elif (room[playerTileY][playerTileX] == LOCKEDLIVINGROOMDOOR):
        if('Living Room Key' in playerInventory):
            displayMessage('*Unlocked door with living room key', room)
            displayMessage('*Discarded living room key', room)
            entranceRoom[3][9] = DOOR
            entranceRoom[4][9] = DOOR
            playerInventory.remove('Living Room Key')
            return False
        else:
            displayMessage('*The door is locked', room)
            return True

    elif (room[playerTileY][playerTileX] == PLANT):
        displayMessage('*A lively plant', room)
        return True

    else:
        return False

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def fadeOut(room):
    for rw in range(MAPWIDTH):
        for cl in range(MAPHEIGHT):
            pygame.draw.rect(DISPLAYSURF, textures[room[cl][rw]], (TILESIZE * rw, TILESIZE * cl, TILESIZE, TILESIZE))
            pygame.display.update()
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def checkForRandomEncounter(stats, room):
    if (room == livingRoom):
        randomChance = random.randint(0, 1)
    else:
        randomChance = random.randint(0, 20)
        
    if(randomChance == 0):
        stats = initiateFight(stats)
        return stats
    else:
        return stats

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def initiateFight(stats):
    fadeOut(fightRoom)
    selection = 1
    intTemp = 0
    while intTemp == 0:
        for fightEvent in pygame.event.get():
            if fightEvent.type == QUIT:
                pygame.quit()
                sys.exit()
            
            elif(fightEvent.type == KEYDOWN):
                if(fightEvent.key == K_LEFT):
                    if(selection == 4.5):
                        selection = 1
                    elif(selection == 8):
                        selection = 4.5

                if(fightEvent.key == K_RIGHT):
                    if(selection == 1):
                        selection = 4.5
                    elif(selection == 4.5):
                        selection = 8

                if(fightEvent.key == K_SPACE):
                    if(selection == 8):
                        intTemp = 1
                    if(selection == 1):
                        stats['Health'] = stats['Health'] - 1
                        print (stats['Health'])

                        
        for rw in range(MAPWIDTH):
            for cl in range(MAPHEIGHT):
                pygame.draw.rect(DISPLAYSURF, textures[fightRoom[cl][rw]], (TILESIZE * rw, TILESIZE * cl, TILESIZE, TILESIZE))

    
        pygame.draw.rect(DISPLAYSURF, BLUE, ((TILESIZE * 4 + 64), (TILESIZE * 2 + 64), TILESIZE, TILESIZE))

        fightButton = fightFont.render('FIGHT', False, WHITE)
        DISPLAYSURF.blit(fightButton,(TILESIZE, (TILESIZE * (MAPHEIGHT - 2)) + (TILESIZE / 2)))
        itemButton = fightFont.render('ITEM', False, WHITE)
        DISPLAYSURF.blit(itemButton, (TILESIZE * 4.5, (TILESIZE * (MAPHEIGHT - 2)) + (TILESIZE / 2)))
        runButton = fightFont.render('RUN', True, WHITE)
        DISPLAYSURF.blit(runButton, (TILESIZE * 8, (TILESIZE * (MAPHEIGHT - 2)) + (TILESIZE / 2)))
    
        pygame.draw.rect(DISPLAYSURF, WHITE, (TILESIZE * selection - (TILESIZE / 4), (TILESIZE *(MAPHEIGHT - 2)) + 72, TILESIZE / 8, TILESIZE / 8))
        pygame.display.update()
    
    return stats

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def setPlayerStats():   
    tempInt = 0
    selection = 2
    
    vigor = 1
    power = 1
    wisdom = 1
    dexterity = 1
    luck = 1
    availablePoints = 25
    
    while (tempInt == 0):
        for statEvent in pygame.event.get():
            if statEvent.type == QUIT:
                pygame.quit()
                sys.exit()
            
            elif(statEvent.type == KEYDOWN):
                if(statEvent.key == K_SPACE):
                    tempInt = 1

                if(statEvent.key == K_DOWN) and (selection < 4):
                    selection += 0.5
                if(statEvent.key == K_UP) and (selection > 2):
                    selection -= 0.5

                if(statEvent.key == K_RIGHT):
                    if(selection == 2) and (vigor < 20) and (availablePoints > 0):
                        vigor += 1
                        availablePoints -=1
                    elif(selection == 2.5) and (power < 20) and (availablePoints > 0):
                        power += 1
                        availablePoints -= 1
                    elif(selection == 3) and (wisdom < 20) and (availablePoints > 0):
                        wisdom += 1
                        availablePoints -= 1
                    elif(selection == 3.5) and (dexterity < 20) and (availablePoints > 0):
                        dexterity += 1
                        availablePoints -= 1
                    elif(selection == 4) and (luck < 20) and (availablePoints > 0):
                        luck += 1
                        availablePoints -= 1

                if(statEvent.key == K_LEFT):
                    if(selection == 2) and (vigor > 1):
                        vigor -= 1
                        availablePoints +=1
                    elif(selection == 2.5) and (power > 1):
                        power -= 1
                        availablePoints += 1
                    elif(selection == 3) and (wisdom > 1):
                        wisdom -= 1
                        availablePoints += 1
                    elif(selection == 3.5) and (dexterity > 1):
                        dexterity -= 1
                        availablePoints += 1
                    elif(selection == 4) and (luck > 1):
                        luck -= 1
                        availablePoints += 1
                    
                
        DISPLAYSURF.fill(BLACK)

        titleText = titleFont.render('Choose Your Stats', False, WHITE)
        DISPLAYSURF.blit(titleText, (TILESIZE * (MAPWIDTH / 3.5), TILESIZE / 2))

        availableText = statFont.render('Available Points = ' + str(availablePoints), False, WHITE)
        DISPLAYSURF.blit(availableText, (TILESIZE * (MAPWIDTH / 3.5), TILESIZE * 1.25))
        
        healthText = statFont.render('Vigor = ' + str(vigor), False, WHITE)
        DISPLAYSURF.blit(healthText, (TILESIZE * (MAPWIDTH / 3.5), TILESIZE * 2))
        
        powerText = statFont.render('Power = ' + str(power), False, WHITE)
        DISPLAYSURF.blit(powerText, (TILESIZE * (MAPWIDTH / 3.5), TILESIZE * 2.5))
        
        wisdomText = statFont.render('Wisdom = ' + str(wisdom), False, WHITE)
        DISPLAYSURF.blit(wisdomText, (TILESIZE * (MAPWIDTH / 3.5), TILESIZE * 3))
        
        speedText = statFont.render('Dexterity = ' + str(dexterity), False, WHITE)
        DISPLAYSURF.blit(speedText, (TILESIZE * (MAPWIDTH / 3.5), TILESIZE * 3.5))
        
        luckText = statFont.render('Luck = ' + str(luck), False, WHITE)
        DISPLAYSURF.blit(luckText, (TILESIZE * (MAPWIDTH / 3.5), TILESIZE * 4))

        pygame.draw.rect(DISPLAYSURF, WHITE, (TILESIZE * 2, TILESIZE * selection, TILESIZE / 8, TILESIZE / 8))
        pygame.display.update()

    stats = {
        'Health': vigor * 5,
        'Sanity': wisdom * 5,
        'Vigor': vigor,
        'Power': power,
        'Wisdom': wisdom,
        'Dexterity': dexterity,
        'Luck': luck
    }
    return stats

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def openMenu():
    tempInt = 0
    selection = 2.5
    while tempInt == 0:
        for menuEvent in pygame.event.get():
            if (menuEvent.type == QUIT):
                pygame.quit()
                sys.exit()
                
            elif (menuEvent.type == KEYDOWN):
                if(menuEvent.key == K_ESCAPE):
                    tempInt = 1
                    
                if(menuEvent.key == K_UP) and (selection > 2.5):
                    selection -= 1
                if(menuEvent.key == K_DOWN) and (selection < 4.5):
                    selection += 1

                if(menuEvent.key == K_SPACE):
                    if(selection == 2.5):
                        openInventory()
                    if(selection == 3.5):
                        openStats()
                    if(selection == 4.5):
                        quitOption()
                
        for rw in range(MAPWIDTH):
            for cl in range(MAPHEIGHT):
                pygame.draw.rect(DISPLAYSURF, textures[curRoom[cl][rw]], (TILESIZE * rw, TILESIZE * cl, TILESIZE, TILESIZE))
        pygame.draw.rect(DISPLAYSURF, RED, (playerPos[0], playerPos[1], TILESIZE, TILESIZE))

        pygame.draw.rect(DISPLAYSURF, textures[MENU], (TILESIZE * 7, TILESIZE * 2, TILESIZE * 1.5, TILESIZE * 3))
        pygame.draw.rect(DISPLAYSURF, WHITE, (TILESIZE * 7.25, TILESIZE * selection, TILESIZE / 8, TILESIZE / 8)) 
        
        inventoryText = menuFont.render('Inventory', False, WHITE)
        DISPLAYSURF.blit(inventoryText, (TILESIZE * 7.5, TILESIZE * 2.5))

        statsText = menuFont.render('Stats', False, WHITE)
        DISPLAYSURF.blit(statsText, (TILESIZE * 7.5, TILESIZE * 3.5))

        quitText = menuFont.render('Quit', False, WHITE)
        DISPLAYSURF.blit(quitText, (TILESIZE * 7.5, TILESIZE * 4.5))
        
        pygame.display.update()
                
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def openInventory():
    tempInt = 0
    selection = 2.25

    while (tempInt == 0):
        
        numOfItems = 0
        for item in playerInventory:
            numOfItems += 1
        selectionMax = 2.25 + ((numOfItems - 1) * 0.25)
        
        if(selectionMax < 2.25):
            selection = 4.5
    
        testedSelection = 2.25
        for item in playerInventory:
            if(testedSelection == selection):
                curItem = item
            testedSelection += 0.25
            
        for invEvent in pygame.event.get():
            if(invEvent.type == QUIT):
                pygame.quit()
                sys.exit()

            elif(invEvent.type == KEYDOWN):
                if(invEvent.key == K_ESCAPE):
                    tempInt = 1

                if(invEvent.key == K_DOWN) and (selection <= selectionMax):
                    if (selection == selectionMax):
                        selection = 4.5
                    else:
                        selection += 0.25
                        
                if(invEvent.key == K_UP) and (selection > 2.25):
                    if(selection == 4.5):
                        selection = selectionMax
                    else:
                        selection -= 0.25

                if(invEvent.key == K_SPACE):
                    if(selection == 4.5):
                       tempInt = 1
                    else:
                        invInteract(curItem, TILESIZE * selection)

        for rw in range(MAPWIDTH):
            for cl in range(MAPHEIGHT):
                pygame.draw.rect(DISPLAYSURF, textures[curRoom[cl][rw]], (TILESIZE * rw, TILESIZE * cl, TILESIZE, TILESIZE))
        pygame.draw.rect(DISPLAYSURF, RED, (playerPos[0], playerPos[1], TILESIZE, TILESIZE))
        pygame.draw.rect(DISPLAYSURF, textures[MENU], (TILESIZE * 7, TILESIZE * 2, TILESIZE * 1.75, TILESIZE * 3))

        pygame.draw.rect(DISPLAYSURF, WHITE, (TILESIZE * 7.25, TILESIZE * selection, TILESIZE / 8, TILESIZE / 8))

        backText = menuFont.render('Back', False, WHITE)
        DISPLAYSURF.blit(backText, (TILESIZE * 7.5, TILESIZE * 4.5))
        
        distance = 0.25
        for item in playerInventory:
            itemText = invFont.render(item, False, WHITE)
            DISPLAYSURF.blit(itemText, (TILESIZE * 7.5, TILESIZE * (2 + distance)))
            distance += 0.25
            

        pygame.display.update()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def invInteract(item, yValue):
    if(item in consumables):
        consumeOption(item, yValue)
    elif(item == 'Living Room Key'):
        displayMessage('*Looks like a key to a door', curRoom)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def consumeOption(item, yValue):
    tempInt = 0
    selection = 0
    
    while tempInt == 0:
        for consumeEvent in pygame.event.get():
            if(consumeEvent.type == QUIT):
                pygame.quit()
                sys.exit()
                
            elif(consumeEvent.type == KEYDOWN):
                if(consumeEvent.key == K_ESCAPE):
                    tempInt = 1
                    
                if(consumeEvent.key == K_UP):
                    selection = 0
                if(consumeEvent.key == K_DOWN):
                    selection = 40

                if(consumeEvent.key == K_SPACE):
                    if(selection == 0):
                        consumeItem(item)
                        tempInt = 1
                    if(selection == 40):
                        tempInt = 1

        for rw in range(MAPWIDTH):
            for cl in range(MAPHEIGHT):
                pygame.draw.rect(DISPLAYSURF, textures[curRoom[cl][rw]], (TILESIZE * rw, TILESIZE * cl, TILESIZE, TILESIZE))
        pygame.draw.rect(DISPLAYSURF, RED, (playerPos[0], playerPos[1], TILESIZE, TILESIZE))
        pygame.draw.rect(DISPLAYSURF, textures[MENU], (TILESIZE * 7, TILESIZE * 2, TILESIZE * 1.75, TILESIZE * 3))
        pygame.draw.rect(DISPLAYSURF, BLUE, (TILESIZE * 8, (yValue) - 16, TILESIZE / 2, (TILESIZE / 2) + 16))

        useText = invFont.render('Use', False, WHITE)
        DISPLAYSURF.blit(useText, ((TILESIZE * 8) + 24, (yValue) - 8))

        backAgainText = invFont.render('Back', False, WHITE)
        DISPLAYSURF.blit(backAgainText, ((TILESIZE * 8) + 24, (yValue) + 32))

        pygame.draw.rect(DISPLAYSURF, WHITE, ((TILESIZE * 8) + 4, ((yValue) - 8) + selection, TILESIZE / 8, TILESIZE / 8))
        

        pygame.draw.rect(DISPLAYSURF, WHITE, (TILESIZE * 7.25, yValue, TILESIZE / 8, TILESIZE / 8))

        backText = menuFont.render('Back', False, WHITE)
        DISPLAYSURF.blit(backText, (TILESIZE * 7.5, TILESIZE * 4.5))
        
        distance = 0.25
        for playerItem in playerInventory:
            itemText = invFont.render(playerItem, False, WHITE)
            DISPLAYSURF.blit(itemText, (TILESIZE * 7.5, TILESIZE * (2 + distance)))
            distance += 0.25

        pygame.display.update()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def consumeItem(item):
    if(item == 'Snack'):
        displayMessage('*You ate the snack', curRoom)
        displayMessage('*You gain 5 health', curRoom)
        playerStats['Health'] += 5
        playerInventory.remove('Snack')
        print (playerStats)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def openStats():
    tempInt = 0
    selection = 2.25
    while tempInt == 0:
        for menuEvent in pygame.event.get():
            if (menuEvent.type == QUIT):
                pygame.quit()
                sys.exit()
                
            elif (menuEvent.type == KEYDOWN):
                if(menuEvent.key == K_ESCAPE):
                    tempInt = 1
                    
                if(menuEvent.key == K_UP) and (selection > 2.25):
                    if(selection == 4.5):
                        selection = 3.75
                    else:
                        selection -= 0.25
                        
                if(menuEvent.key == K_DOWN) and (selection < 4.5):
                    if(selection == 3.75):
                        selection = 4.5
                    else:
                        selection += 0.25

                if(menuEvent.key == K_SPACE):
                    if(selection == 2.25):
                        displayMessage('*Your health, don\'t let it hit zero', curRoom)
                    if(selection == 2.5):
                        displayMessage('*If it depletes, you will go insane', curRoom)
                    if(selection == 2.75):
                        displayMessage('*Helps you resist damage', curRoom)
                    if(selection == 3):
                        displayMessage('*Determines your damage', curRoom)
                    if(selection == 3.25):
                        displayMessage('*Needed to pass skill checks', curRoom)
                    if(selection == 3.5):
                        displayMessage('*Allows you to go first in a fight', curRoom)
                    if(selection == 3.75):
                        displayMessage('*Makes you lucky', curRoom)
                    if(selection == 4.5):
                        tempInt = 15

                
        for rw in range(MAPWIDTH):
            for cl in range(MAPHEIGHT):
                pygame.draw.rect(DISPLAYSURF, textures[curRoom[cl][rw]], (TILESIZE * rw, TILESIZE * cl, TILESIZE, TILESIZE))
        pygame.draw.rect(DISPLAYSURF, RED, (playerPos[0], playerPos[1], TILESIZE, TILESIZE))

        pygame.draw.rect(DISPLAYSURF, textures[MENU], (TILESIZE * 7, TILESIZE * 2, TILESIZE * 1.5, TILESIZE * 3))
        
        pygame.draw.rect(DISPLAYSURF, WHITE, (TILESIZE * 7.25, TILESIZE * selection, TILESIZE / 8, TILESIZE / 8)) 

        healthText = invFont.render('Health = ' + str(playerStats['Health']), False, WHITE)
        DISPLAYSURF.blit(healthText, (TILESIZE * 7.5, TILESIZE * 2.25))

        sanityText = invFont.render('Sanity = ' + str(playerStats['Sanity']), False, WHITE)
        DISPLAYSURF.blit(sanityText, (TILESIZE * 7.5, TILESIZE * 2.5))
        
        vigorText = invFont.render('Vigor = ' + str(playerStats['Vigor']), False, WHITE)
        DISPLAYSURF.blit(vigorText, (TILESIZE * 7.5, TILESIZE * 2.75))
        
        powerText = invFont.render('Power = ' + str(playerStats['Power']), False, WHITE)
        DISPLAYSURF.blit(powerText, (TILESIZE * 7.5, TILESIZE * 3))
        
        wisdomText = invFont.render('Wisdom = ' + str(playerStats['Wisdom']), False, WHITE)
        DISPLAYSURF.blit(wisdomText, (TILESIZE * 7.5, TILESIZE * 3.25))
        
        speedText = invFont.render('Dexterity = ' + str(playerStats['Dexterity']), False, WHITE)
        DISPLAYSURF.blit(speedText, (TILESIZE * 7.5, TILESIZE * 3.5))
        
        luckText = invFont.render('Luck = ' + str(playerStats['Luck']), False, WHITE)
        DISPLAYSURF.blit(luckText, (TILESIZE * 7.5, TILESIZE * 3.75))


        backText = menuFont.render('Back', False, WHITE)
        DISPLAYSURF.blit(backText, (TILESIZE * 7.5, TILESIZE * 4.5))
        
        pygame.display.update()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def quitOption():
    tempInt = 0
    selection = 0
    while tempInt == 0:
        for quitEvent in pygame.event.get():
            if (quitEvent.type == QUIT):
                pygame.quit()
                sys.exit()
                
            elif (quitEvent.type == KEYDOWN):
                if(quitEvent.key == K_ESCAPE):
                    tempInt = 1
                    
                if(quitEvent.key == K_UP):
                    selection = 0
                if(quitEvent.key == K_DOWN):
                    selection = 48

                if(quitEvent.key == K_SPACE):
                    if(selection == 0):
                        pygame.quit()
                        sys.exit()
                    elif(selection == 48):
                        tempInt = 1
                

                
        for rw in range(MAPWIDTH):
            for cl in range(MAPHEIGHT):
                pygame.draw.rect(DISPLAYSURF, textures[curRoom[cl][rw]], (TILESIZE * rw, TILESIZE * cl, TILESIZE, TILESIZE))
        pygame.draw.rect(DISPLAYSURF, RED, (playerPos[0], playerPos[1], TILESIZE, TILESIZE))

        pygame.draw.rect(DISPLAYSURF, textures[MENU], (TILESIZE * 7, TILESIZE * 2, TILESIZE * 1.5, TILESIZE * 3))
        pygame.draw.rect(DISPLAYSURF, WHITE, (TILESIZE * 7.25, TILESIZE * 4.5, TILESIZE / 8, TILESIZE / 8))
        pygame.draw.rect(DISPLAYSURF, BLUE, (TILESIZE * 8, (TILESIZE * 4.5) - 16, TILESIZE / 2, (TILESIZE / 2) + 16))

        pygame.draw.rect(DISPLAYSURF, WHITE, ((TILESIZE * 8), TILESIZE * 4.5 - 8 + selection, TILESIZE / 8, TILESIZE / 8))
        useText = invFont.render('Quit', False, WHITE)
        DISPLAYSURF.blit(useText, ((TILESIZE * 8) + 24, (TILESIZE * 4.5) - 8))
        backAgainText = invFont.render('Back', False, WHITE)
        DISPLAYSURF.blit(backAgainText, ((TILESIZE * 8) + 24, (TILESIZE * 4.5) + 32))

        
        
        inventoryText = menuFont.render('Inventory', False, WHITE)
        DISPLAYSURF.blit(inventoryText, (TILESIZE * 7.5, TILESIZE * 2.5))

        statsText = menuFont.render('Stats', False, WHITE)
        DISPLAYSURF.blit(statsText, (TILESIZE * 7.5, TILESIZE * 3.5))

        quitText = menuFont.render('Quit', False, WHITE)
        DISPLAYSURF.blit(quitText, (TILESIZE * 7.5, TILESIZE * 4.5))
        
        pygame.display.update()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def checkInventory():
    items = 0
    for item in playerInventory:
           items += 1

    if(items == inventoryMax):
           displayMessage('*Your inventory is too full', curRoom)
           return False
    else:
           return True

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
        
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE))
pygame.display.set_caption("TEST DEMO")
pygame.font.init()
textFont = pygame.font.SysFont('Comic Sans MS', 35)
fightFont = pygame.font.SysFont('Comic Sans MS', 50)
statFont = pygame.font.SysFont('Comic Sans MS', 40)
titleFont = pygame.font.SysFont('Comic Sans MS', 100)
menuFont = pygame.font.SysFont('Comic Sans MS', 30)
invFont = pygame.font.SysFont('Comic Sans MS', 25)

playerStats = setPlayerStats()
playerInventory = ['Snack', 'Snack']
inventoryMax = 9

print(playerStats)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

while True:
    DISPLAYSURF.fill(BLACK)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            if (event.key == K_RIGHT):
                playerTileX += 1
                if(nextToWall(curRoom)):
                    playerTileX -= 1
                    continue
                
                if(nextToDoor(curRoom)):
                    curRoom = changeRoom(curRoom, 'right')
                    fadeOut(curRoom)
                    playerTileX = 1
                    playerPos = [TILESIZE * playerTileX, TILESIZE * playerTileY]
                    continue
                
                playerPos = [TILESIZE * playerTileX, TILESIZE * playerTileY]
                playerStats = checkForRandomEncounter(playerStats, curRoom)
            
            if(event.key == K_LEFT):
                playerTileX -= 1
                if(nextToWall(curRoom)):
                    playerTileX += 1
                    continue
                
                if(nextToDoor(curRoom)):
                    curRoom = changeRoom(curRoom, 'left')
                    fadeOut(curRoom)
                    playerTileX = 8
                    playerPos = [TILESIZE * playerTileX, TILESIZE * playerTileY]
                    continue
                
                playerPos = [TILESIZE * playerTileX, TILESIZE * playerTileY]
                playerStats = checkForRandomEncounter(playerStats, curRoom)

            
            if(event.key == K_UP):
                playerTileY -= 1
                if(nextToWall(curRoom)):
                    playerTileY += 1
                    continue
                
                if(nextToDoor(curRoom)):
                    curRoom = changeRoom(curRoom, 'up')
                    fadeOut(curRoom)
                    playerTileY = 6
                    playerPos = [TILESIZE * playerTileX, TILESIZE * playerTileY]
                    continue
                
                playerPos = [TILESIZE * playerTileX, TILESIZE * playerTileY]
                playerStats = checkForRandomEncounter(playerStats, curRoom)
                
            if(event.key == K_DOWN):
                playerTileY += 1
                if(nextToWall(curRoom)):
                    playerTileY -= 1
                    continue
                
                if(nextToDoor(curRoom)):
                    curRoom = changeRoom(curRoom, 'down')
                    fadeOut(curRoom)
                    playerTileY = 1
                    playerPos = [TILESIZE * playerTileX, TILESIZE * playerTileY]
                    continue
                
                playerPos = [TILESIZE * playerTileX, TILESIZE * playerTileY]
                
                playerStats = checkForRandomEncounter(playerStats, curRoom)
                
            if(event.key == K_SPACE):
                interact(curTile, curRoom)

            if(event.key == K_ESCAPE):
                openMenu()
                

    for rw in range(MAPWIDTH):
        for cl in range(MAPHEIGHT):
            pygame.draw.rect(DISPLAYSURF, textures[curRoom[cl][rw]], (TILESIZE * rw, TILESIZE * cl, TILESIZE, TILESIZE))
    
    pygame.draw.rect(DISPLAYSURF, RED, (playerPos[0], playerPos[1], TILESIZE, TILESIZE))
    curTile = curRoom[playerTileY][playerTileX]
    playerInventory.sort()
    pygame.display.update()
