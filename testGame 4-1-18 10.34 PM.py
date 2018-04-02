import pygame, sys
from pygame.locals import *
import time
import random

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

    if tile == EMPTYDRESSER:
        displayMessage('*An empty dresser', room)
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def displayMessage(message, room):
    
    for rw in range(MAPWIDTH):
        for cl in range(MAPHEIGHT):
            pygame.draw.rect(DISPLAYSURF, textures[room[cl][rw]], (TILESIZE * rw, TILESIZE * cl, TILESIZE, TILESIZE))

    if(room != fightRoom):
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

def displayStatsMessage(message, room, selection):
    
    for rw in range(MAPWIDTH):
        for cl in range(MAPHEIGHT):
            pygame.draw.rect(DISPLAYSURF, textures[room[cl][rw]], (TILESIZE * rw, TILESIZE * cl, TILESIZE, TILESIZE))

    if(room != fightRoom):
        pygame.draw.rect(DISPLAYSURF, RED, (playerPos[0], playerPos[1], TILESIZE, TILESIZE))
    
    pygame.draw.rect(DISPLAYSURF, BLACK, (TILESIZE * 3, TILESIZE * (MAPHEIGHT - 2), TILESIZE * 4, TILESIZE / 2))

    textSurface = textFont.render(message, False, WHITE)
    DISPLAYSURF.blit(textSurface,((TILESIZE * 3) + (TILESIZE / 8), (TILESIZE * (MAPHEIGHT - 2)) + (TILESIZE / 8)))

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

    levelText = invFont.render('Level = ' + str(playerStats['Level']), False, WHITE)
    DISPLAYSURF.blit(levelText, (TILESIZE * 7.5, TILESIZE * 4))

    xpText = invFont.render('XP = ' + str(playerStats['XP']), False, WHITE)
    DISPLAYSURF.blit(xpText, (TILESIZE * 7.5, TILESIZE * 4.25))


    backText = menuFont.render('Back', False, WHITE)
    DISPLAYSURF.blit(backText, (TILESIZE * 7.5, TILESIZE * 4.5))
    
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

def displayFightMessage(message, room, monster):
    
    for rw in range(MAPWIDTH):
        for cl in range(MAPHEIGHT):
            pygame.draw.rect(DISPLAYSURF, textures[room[cl][rw]], (TILESIZE * rw, TILESIZE * cl, TILESIZE, TILESIZE))

    

    fightMessage = fightFont.render(message, False, WHITE)
    DISPLAYSURF.blit(fightMessage, (TILESIZE * 3.5, (TILESIZE * (MAPHEIGHT - 3)) + (TILESIZE / 2)))
    pygame.draw.rect(DISPLAYSURF, monster['color'], ((TILESIZE * 4 + 64), (TILESIZE * 2 + 64), TILESIZE, TILESIZE))

    fightButton = fightFont.render('FIGHT', False, WHITE)
    DISPLAYSURF.blit(fightButton,(TILESIZE, (TILESIZE * (MAPHEIGHT - 2.5)) + (TILESIZE / 2)))
    itemButton = fightFont.render('ITEM', False, WHITE)
    DISPLAYSURF.blit(itemButton, (TILESIZE * 4.5, (TILESIZE * (MAPHEIGHT - 2.5)) + (TILESIZE / 2)))
    runButton = fightFont.render('RUN', True, WHITE)
    DISPLAYSURF.blit(runButton, (TILESIZE * 8, (TILESIZE * (MAPHEIGHT - 2.5)) + (TILESIZE / 2)))
    hpCounter = fightFont.render('HP = ' + str(playerStats['Health']), False, WHITE)
    DISPLAYSURF.blit(hpCounter,(TILESIZE, (TILESIZE * (MAPHEIGHT - 3)) + (TILESIZE / 2)))
    sanityCounter = fightFont.render('Sanity = ' + str(playerStats['Sanity']), False, WHITE)
    DISPLAYSURF.blit(sanityCounter, (TILESIZE * 8,  (TILESIZE * (MAPHEIGHT - 3)) + (TILESIZE / 2)))
    
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
    if (room == entranceRoom) and (direction == 'left'):
        return diningRoom
    
    if (room == livingRoom) and (direction =='left'):
        return entranceRoom

    if(room == diningRoom) and (direction == 'right'):
        return entranceRoom
    if(room == diningRoom) and (direction == 'left'):
        return kitchenHallway

    if(room == kitchenHallway) and (direction == 'up'):
        return kitchenRoom
    if(room == kitchenHallway) and (direction == 'right'):
        return diningRoom

    if(room == kitchenRoom) and (direction == 'down'):
        return kitchenHallway
    if(room == kitchenRoom) and (direction == 'right'):
        return hiddenKitchenPassage

    if(room == hiddenKitchenPassage) and (direction == 'left'):
        return kitchenRoom
    if(room == hiddenKitchenPassage) and (direction == 'right'):
        return studyRoom

    if(room == studyRoom) and (direction == 'left'):
        return hiddenKitchenPassage
    if(room == studyRoom) and (direction == 'right'):
        return gallery
        
        
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
    
    elif (room[playerTileY][playerTileX] == LOCKEDDOOR):
        if('Living Room Key' in playerInventory) and (room == entranceRoom):
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
    
    elif(room[playerTileY][playerTileX] == TABLE):
        displayMessage('*A table', room)
        return True

    elif(room[playerTileY][playerTileX] == CHAIR):
        displayMessage('*A worn chair', room)
        return True

    elif(room[playerTileY][playerTileX] == COUNTER):
         displayMessage('*A counter top', room)
         return True
        
    elif(room[playerTileY][playerTileX] == SINK):
         displayMessage('*A sink filled with dishes', room)
         return True
        
    elif(room[playerTileY][playerTileX] == OVEN):
         displayMessage('*A dusty oven', room)
         return True
        
    elif(room[playerTileY][playerTileX] == SECRETWALL) and (room == kitchenRoom):
         displayMessage('*You push an odd tile on the wall', room)
         displayMessage('*The wall opens up!', room)
         kitchenRoom[1][9] = DOOR
         kitchenRoom [2][9] = DOOR
         return False

    elif(room[playerTileY][playerTileX] == DESK):
        displayMessage('*A writing desk', room)
        return True

    elif(room[playerTileY][playerTileX] == BOOKCASE):
        displayMessage('*A bookcase filled to the brim', room)
        return True

    elif(room[playerTileY][playerTileX] == GRAMAPHONE):
        displayMessage('*A gramaphone with no record', room)
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

    monster = random.choice(monsters)
    monsterGoesFirst = 0
    if(monster['Dexterity'] > stats['Dexterity']):
        monsterGoesFirst = 1

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
                        luckyRun = random.randint(0, 100)
                        speedRun = random.randint(0, 50)
                        speedDif = stats['Dexterity'] - monster['Dexterity']
                        if(luckyRun <= stats['Luck']):
                            intTemp = 1
                            displayFightMessage('*The monster justs disappeared',  fightRoom, monster)
                        elif(speedRun <= speedDif):
                            displayFightMessage('*You managed to run away', fightRoom, monster)
                            intTemp = 1
                        else:
                            displayFightMessage('*You couldn\'t get away', fightRoom, monster)
                            stats = monsterAttacks(stats, monster)
                            if(stats['Health'] <= 0):
                                displayFightMessage('*You died!', fightRoom, monster)
                                intTemp = 1

                    if(selection == 4.5):
                        useItem = openFightInventory(fightRoom, monster)
                        if (useItem == 1):
                            stats = monsterAttacks(stats, monster)
                            if(stats['Health'] <= 0):
                                displayFightMessage('*You died!', fightRoom, monster)
                                intTemp = 1

                    if(selection == 1):
                        monster['Health'] = playerAttack(stats, monster)
                        if(monster['Health'] <= 0):
                            displayFightMessage('*You killed the monster!', fightRoom, monster)
                            dropChance = random.randint(0, 20)
                            if(stats['Luck'] > dropChance):
                                itemDrop = random.choice(dropables)
                                displayFightMessage('*You got a ' + itemDrop + '!', fightRoom, monster)
                                if(checkFightInventory(monster)):
                                    playerInventory.append(itemDrop)

                            xpGained = random.randint(stats['Level'] - 3, stats['Level'] + 3)
                            if(xpGained < 1):
                                xpGained = 1
                            displayFightMessage('*You got ' + str(xpGained) + ' XP', fightRoom, monster)
                            stats['XP'] += xpGained
                            
                            intTemp = 1
                            
                        else:
                            stats = monsterAttacks(stats, monster)
                            if(stats['Health'] <= 0):
                                displayFightMessage('*You died!', fightRoom, monster)
                                intTemp = 1
                                                
        for rw in range(MAPWIDTH):
            for cl in range(MAPHEIGHT):
                pygame.draw.rect(DISPLAYSURF, textures[fightRoom[cl][rw]], (TILESIZE * rw, TILESIZE * cl, TILESIZE, TILESIZE))
        
        pygame.draw.rect(DISPLAYSURF, monster['color'], ((TILESIZE * 4.5), (TILESIZE * 2.5), TILESIZE, TILESIZE))

        fightButton = fightFont.render('FIGHT', False, WHITE)
        DISPLAYSURF.blit(fightButton,(TILESIZE, (TILESIZE * (MAPHEIGHT - 2.5)) + (TILESIZE / 2)))
        itemButton = fightFont.render('ITEM', False, WHITE)
        DISPLAYSURF.blit(itemButton, (TILESIZE * 4.5, (TILESIZE * (MAPHEIGHT - 2.5)) + (TILESIZE / 2)))
        runButton = fightFont.render('RUN', True, WHITE)
        DISPLAYSURF.blit(runButton, (TILESIZE * 8, (TILESIZE * (MAPHEIGHT - 2.5)) + (TILESIZE / 2)))

        hpCounter = fightFont.render('HP = ' + str(stats['Health']), False, WHITE)
        DISPLAYSURF.blit(hpCounter,(TILESIZE, (TILESIZE * (MAPHEIGHT - 3)) + (TILESIZE / 2)))
        sanityCounter = fightFont.render('Sanity = ' + str(playerStats['Sanity']), False, WHITE)
        DISPLAYSURF.blit(sanityCounter, (TILESIZE * 8,  (TILESIZE * (MAPHEIGHT - 3)) + (TILESIZE / 2)))

        monsterHp = fightFont.render('HP = ' + str(monster['Health']), False, WHITE)
        DISPLAYSURF.blit(monsterHp, (TILESIZE * 4.5, TILESIZE * 2))
        
        if(monsterGoesFirst == 1):
            monsterAttacks(stats, monster)
            monsterGoesFirst = 0
        pygame.draw.rect(DISPLAYSURF, WHITE, (TILESIZE * selection - (TILESIZE / 4), (TILESIZE *(MAPHEIGHT - 2.5)) + 72, TILESIZE / 8, TILESIZE / 8))
        
        pygame.display.update()
    
    return stats

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def gameOver():
    selection = 1
    tempInt = 0
    while tempInt == 0:
        DISPLAYSURF.fill(BLACK)
        
        for overEvent in pygame.event.get():
            if(overEvent.type == QUIT):
                pygame.quit()
                sys.exit()
                
            elif(overEvent.type == KEYDOWN):
                if(overEvent.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                if(overEvent.key == K_RIGHT):
                    selection = 8
                if(overEvent.key == K_LEFT):
                    selection = 1

                if(overEvent.key == K_SPACE):
                    if(selection == 1):
                        return 1
                    elif(selection == 8):
                        pygame.quit()
                        sys.exit()

        gameOverText = overFont.render('GAME OVER', False, WHITE)
        DISPLAYSURF.blit(gameOverText, (TILESIZE / 2, TILESIZE / 2))

        deathText = subTitleFont.render('You succumbed to the darkness', False, WHITE)
        DISPLAYSURF.blit(deathText, (TILESIZE * 2, TILESIZE * 2.5))

        againText = subTitleFont.render('Would you like to play again?', False, WHITE)
        DISPLAYSURF.blit(againText, (TILESIZE * 2, TILESIZE * 3))

        yesText = subTitleFont.render('Yes', False, WHITE)
        DISPLAYSURF.blit(yesText, (TILESIZE, TILESIZE * 4.5))

        noText = subTitleFont.render('No', False, WHITE)
        DISPLAYSURF.blit(noText, (TILESIZE * 8, TILESIZE * 4.5))

        pygame.draw.rect(DISPLAYSURF, WHITE, ((TILESIZE * selection) - 48, (TILESIZE * 4.5) + 4, TILESIZE / 4, TILESIZE / 4))

        pygame.display.update()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def playerAttack(stats, monster):
    displayFightMessage('*You attack the monster!', fightRoom, monster)
    playerDamage = (stats['Damage'] + 2) - monster['Vigor']
    if (playerDamage < 1):
        playerDamage = 1

    playerHitChance = random.randint(2, 30)
    critChance = random.randint(0, 30)
    if(playerHitChance <= monster['Dexterity']):
        displayFightMessage('*You missed!', fightRoom, monster)
        return monster['Health']
    else:
        if(stats['Luck'] <= critChance):
            displayFightMessage('*Critical Hit!', fightRoom, monster)
            playerDamage = playerDamage * 2
            monster['Health'] -= playerDamage
            displayFightMessage('*You did ' + str(playerDamage) + ' damage', fightRoom, monster)
            return monster['Health']
        else:
            displayFightMessage('*You bashed the monster!', fightRoom, monster)
            monster['Health'] -= playerDamage
            displayFightMessage('*You did ' + str(playerDamage) + ' damage', fightRoom, monster)
            return monster['Health']

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def monsterAttacks(stats, monster):
    displayFightMessage('*The monster attacks you!', fightRoom, monster)
    monsterDamage = (monster['Power'] + 2) - stats['Defense']
    if (monsterDamage < 1):
        monsterDamage = 1
        
    monsterHitChance = random.randint(0, 30)
    if(monsterHitChance <= stats['Dexterity']):
        displayFightMessage('*The monster missed!', fightRoom, monster)
        return stats
    else:
        displayFightMessage('*The monster hit you!', fightRoom, monster)
        stats['Health'] -= monsterDamage
        displayFightMessage('*It did ' + str(monsterDamage) + ' damage', fightRoom, monster)
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
                if(statEvent.key == K_SPACE) and (availablePoints == 0):
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
        'Luck': luck,
        'Level': 1,
        'XP': 0,
        'Damage': power,
        'Defense': vigor
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
                    selection -= 0.75
                if(menuEvent.key == K_DOWN) and (selection < 4.75):
                    selection += 0.75

                if(menuEvent.key == K_SPACE):
                    if(selection == 2.5):
                        openInventory()
                    if(selection == 3.25):
                        openStats()
                    if(selection == 4):
                        openEquipment()
                    if(selection == 4.75):
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
        DISPLAYSURF.blit(statsText, (TILESIZE * 7.5, TILESIZE * 3.25))

        equipmentText = menuFont.render('Equipment', False, WHITE)
        DISPLAYSURF.blit(equipmentText, (TILESIZE * 7.5, TILESIZE * 4))
        
        quitText = menuFont.render('Quit', False, WHITE)
        DISPLAYSURF.blit(quitText, (TILESIZE * 7.5, TILESIZE * 4.75))
        
        pygame.display.update()
                
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def openEquipment():
    tempInt = 0
    selection = 2.5

    while(tempInt == 0):
        for equipEvent in pygame.event.get():
            if (equipEvent.type == QUIT):
                pygame.quit()
                sys.exit()

            elif (equipEvent.type == KEYDOWN):
                if(equipEvent.key == K_ESCAPE):
                    tempInt = 1

                if(equipEvent.key == K_DOWN) and (selection < 4.5):
                    selection += 1
                if(equipEvent.key == K_UP) and (selection > 2.5):
                    selection -= 1

                if(equipEvent.key == K_SPACE):
                    if(selection == 2.5):
                        displayMessage('*Your armor and it\'s rating', curRoom)

                    if(selection == 3.5):
                        displayMessage('*Your weapon and it\s rating', curRoom)

                    if(selection == 4.5):
                        tempInt -= 1


        for rw in range(MAPWIDTH):
            for cl in range(MAPHEIGHT):
                pygame.draw.rect(DISPLAYSURF, textures[curRoom[cl][rw]], (TILESIZE * rw, TILESIZE * cl, TILESIZE, TILESIZE))
        pygame.draw.rect(DISPLAYSURF, RED, (playerPos[0], playerPos[1], TILESIZE, TILESIZE))
        pygame.draw.rect(DISPLAYSURF, textures[MENU], (TILESIZE * 7, TILESIZE * 2, TILESIZE * 1.75, TILESIZE * 3))
        pygame.draw.rect(DISPLAYSURF, WHITE, (TILESIZE * 7.25, TILESIZE * selection, TILESIZE / 8, TILESIZE / 8))

        armorText = menuFont.render(playerEquipment[0] + ': ' + str(equipment[playerEquipment[0]]), False, WHITE)
        DISPLAYSURF.blit(armorText, (TILESIZE * 7.5, TILESIZE * 2.5))

        weaponText = menuFont.render(playerEquipment[1] + ': ' + str(equipment[playerEquipment[1]]), False, WHITE)
        DISPLAYSURF.blit(weaponText, (TILESIZE * 7.5, TILESIZE * 3.5))

        backText = menuFont.render('Back', False, WHITE)
        DISPLAYSURF.blit(backText, (TILESIZE * 7.5, TILESIZE * 4.5))

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
                        invInteract(curItem, TILESIZE * selection, curRoom, monster1)

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

def openFightInventory(room, monster):
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
                    return 0

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
                       return 0
                    else:
                        usedConsumable = invInteract(curItem, TILESIZE * selection, room, monster)
                        return usedConsumable
                        

        for rw in range(MAPWIDTH):
            for cl in range(MAPHEIGHT):
                pygame.draw.rect(DISPLAYSURF, textures[room[cl][rw]], (TILESIZE * rw, TILESIZE * cl, TILESIZE, TILESIZE))
        pygame.draw.rect(DISPLAYSURF, monster['color'], ((TILESIZE * 4 + 64), (TILESIZE * 2 + 64), TILESIZE, TILESIZE))
        pygame.draw.rect(DISPLAYSURF, textures[MENU], (TILESIZE * 7, TILESIZE * 2, TILESIZE * 1.75, TILESIZE * 3))

        pygame.draw.rect(DISPLAYSURF, WHITE, (TILESIZE * 7.25, TILESIZE * selection, TILESIZE / 8, TILESIZE / 8))

        backText = menuFont.render('Back', False, WHITE)
        DISPLAYSURF.blit(backText, (TILESIZE * 7.5, TILESIZE * 4.5))

        fightButton = fightFont.render('FIGHT', False, WHITE)
        DISPLAYSURF.blit(fightButton,(TILESIZE, (TILESIZE * (MAPHEIGHT - 2.5)) + (TILESIZE / 2)))
        itemButton = fightFont.render('ITEM', False, WHITE)
        DISPLAYSURF.blit(itemButton, (TILESIZE * 4.5, (TILESIZE * (MAPHEIGHT - 2.5)) + (TILESIZE / 2)))
        runButton = fightFont.render('RUN', True, WHITE)
        DISPLAYSURF.blit(runButton, (TILESIZE * 8, (TILESIZE * (MAPHEIGHT - 2.5)) + (TILESIZE / 2)))

        hpCounter = fightFont.render('HP = ' + str(playerStats['Health']), False, WHITE)
        DISPLAYSURF.blit(hpCounter,(TILESIZE, (TILESIZE * (MAPHEIGHT - 3)) + (TILESIZE / 2)))
        sanityCounter = fightFont.render('Sanity = ' + str(playerStats['Sanity']), False, WHITE)
        DISPLAYSURF.blit(sanityCounter, (TILESIZE * 8,  (TILESIZE * (MAPHEIGHT - 3)) + (TILESIZE / 2)))
        
        distance = 0.25
        for item in playerInventory:
            itemText = invFont.render(item, False, WHITE)
            DISPLAYSURF.blit(itemText, (TILESIZE * 7.5, TILESIZE * (2 + distance)))
            distance += 0.25
            

        pygame.display.update()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def invInteract(item, yValue, room, monster):
    if(item in consumables):
        if(room == fightRoom):
            usedItem = consumeOptionFight(item, yValue, monster)
            return usedItem
        else:
            consumeOption(item, yValue, room)

    elif(item in equipment):
        if(room == fightRoom):
            displayFightMessage('*This is not the time for that!', room, monster)
            return 0
        else:
            equipOption(item, yValue, room)
    
    elif(item == 'Living Room Key'):
        if(room == fightRoom):
            displayFightMessage('*This is not the time for that!', room, monster)
            return 0
        else:
            displayMessage('*Looks like a key to a door', curRoom)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def consumeOption(item, yValue, room):
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
                        consumeItem(item, room)
                        tempInt = 1
                        break
                    if(selection == 40):
                        tempInt = 1

        for rw in range(MAPWIDTH):
            for cl in range(MAPHEIGHT):
                pygame.draw.rect(DISPLAYSURF, textures[room[cl][rw]], (TILESIZE * rw, TILESIZE * cl, TILESIZE, TILESIZE))
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

def consumeOptionFight(item, yValue, monster):
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
                    return 0
                    
                if(consumeEvent.key == K_UP):
                    selection = 0
                if(consumeEvent.key == K_DOWN):
                    selection = 40

                if(consumeEvent.key == K_SPACE):
                    if(selection == 0):
                        consumeItemFight(item, fightRoom, monster)
                        tempInt = 1
                        return 1
                    if(selection == 40):
                        tempInt = 1
                        return 0

        for rw in range(MAPWIDTH):
            for cl in range(MAPHEIGHT):
                pygame.draw.rect(DISPLAYSURF, textures[fightRoom[cl][rw]], (TILESIZE * rw, TILESIZE * cl, TILESIZE, TILESIZE))
        
        pygame.draw.rect(DISPLAYSURF, textures[MENU], (TILESIZE * 7, TILESIZE * 2, TILESIZE * 1.75, TILESIZE * 3))
        
        pygame.draw.rect(DISPLAYSURF, BLUE, (TILESIZE * 8, (yValue) - 16, TILESIZE / 2, (TILESIZE / 2) + 16))
        
        pygame.draw.rect(DISPLAYSURF, monster['color'], ((TILESIZE * 4 + 64), (TILESIZE * 2 + 64), TILESIZE, TILESIZE))
        
        useText = invFont.render('Use', False, WHITE)
        DISPLAYSURF.blit(useText, ((TILESIZE * 8) + 24, (yValue) - 8))

        backAgainText = invFont.render('Back', False, WHITE)
        DISPLAYSURF.blit(backAgainText, ((TILESIZE * 8) + 24, (yValue) + 32))

        pygame.draw.rect(DISPLAYSURF, WHITE, ((TILESIZE * 8) + 4, ((yValue) - 8) + selection, TILESIZE / 8, TILESIZE / 8))
        

        pygame.draw.rect(DISPLAYSURF, WHITE, (TILESIZE * 7.25, yValue, TILESIZE / 8, TILESIZE / 8))

        backText = menuFont.render('Back', False, WHITE)
        DISPLAYSURF.blit(backText, (TILESIZE * 7.5, TILESIZE * 4.5))

        fightButton = fightFont.render('FIGHT', False, WHITE)
        DISPLAYSURF.blit(fightButton,(TILESIZE, (TILESIZE * (MAPHEIGHT - 2.5)) + (TILESIZE / 2)))
        itemButton = fightFont.render('ITEM', False, WHITE)
        DISPLAYSURF.blit(itemButton, (TILESIZE * 4.5, (TILESIZE * (MAPHEIGHT - 2.5)) + (TILESIZE / 2)))
        runButton = fightFont.render('RUN', True, WHITE)
        DISPLAYSURF.blit(runButton, (TILESIZE * 8, (TILESIZE * (MAPHEIGHT - 2.5)) + (TILESIZE / 2)))

        hpCounter = fightFont.render('HP = ' + str(playerStats['Health']), False, WHITE)
        DISPLAYSURF.blit(hpCounter,(TILESIZE, (TILESIZE * (MAPHEIGHT - 3)) + (TILESIZE / 2)))
        sanityCounter = fightFont.render('Sanity = ' + str(playerStats['Sanity']), False, WHITE)
        DISPLAYSURF.blit(sanityCounter, (TILESIZE * 8,  (TILESIZE * (MAPHEIGHT - 3)) + (TILESIZE / 2)))
        
        distance = 0.25
        for playerItem in playerInventory:
            itemText = invFont.render(playerItem, False, WHITE)
            DISPLAYSURF.blit(itemText, (TILESIZE * 7.5, TILESIZE * (2 + distance)))
            distance += 0.25

        pygame.display.update()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def consumeItem(item, room):
    if(item == 'Snack'):
        displayMessage('*You ate the snack', room)
        displayMessage('*You gain 5 health', room)
        playerStats['Health'] += 5
        playerInventory.remove('Snack')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def consumeItemFight(item, room, monster):
    if(item == 'Snack'):
        displayFightMessage('*You ate the snack', room, monster)
        displayFightMessage('*You gain 5 health', room, monster)
        playerStats['Health'] += 5
        playerInventory.remove('Snack')

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
                    selection -= 0.25
                        
                if(menuEvent.key == K_DOWN) and (selection < 4.5):
                    selection += 0.25

                if(menuEvent.key == K_SPACE):
                    if(selection == 2.25):
                        displayStatsMessage('*Your health, don\'t let it hit zero', curRoom, selection)
                    if(selection == 2.5):
                        displayStatsMessage('*If it depletes, you will go insane', curRoom, selection)
                    if(selection == 2.75):
                        displayStatsMessage('*Helps you resist damage', curRoom, selection)
                    if(selection == 3):
                        displayStatsMessage('*Determines your damage', curRoom, selection)
                    if(selection == 3.25):
                        displayStatsMessage('*Needed to pass skill checks', curRoom, selection)
                    if(selection == 3.5):
                        displayStatsMessage('*Allows you to go first in a fight', curRoom, selection)
                    if(selection == 3.75):
                        displayStatsMessage('*Makes you lucky', curRoom, selection)
                    if(selection == 4):
                        displayStatsMessage('*Your current level', curRoom, selection)
                    if(selection == 4.25):
                        displayStatsMessage('*Needed to level up', curRoom, selection)
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

        levelText = invFont.render('Level = ' + str(playerStats['Level']), False, WHITE)
        DISPLAYSURF.blit(levelText, (TILESIZE * 7.5, TILESIZE * 4))

        xpText = invFont.render('XP = ' + str(playerStats['XP']), False, WHITE)
        DISPLAYSURF.blit(xpText, (TILESIZE * 7.5, TILESIZE * 4.25))

        
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
        pygame.draw.rect(DISPLAYSURF, WHITE, (TILESIZE * 7.25, TILESIZE * 4.75, TILESIZE / 8, TILESIZE / 8))
        pygame.draw.rect(DISPLAYSURF, BLUE, (TILESIZE * 8, (TILESIZE * 4.5) - 16, TILESIZE / 2, (TILESIZE / 2) + 16))

        pygame.draw.rect(DISPLAYSURF, WHITE, ((TILESIZE * 8), TILESIZE * 4.5 - 8 + selection, TILESIZE / 8, TILESIZE / 8))
        useText = invFont.render('Quit', False, WHITE)
        DISPLAYSURF.blit(useText, ((TILESIZE * 8) + 24, (TILESIZE * 4.5) - 8))
        backAgainText = invFont.render('Back', False, WHITE)
        DISPLAYSURF.blit(backAgainText, ((TILESIZE * 8) + 24, (TILESIZE * 4.5) + 32))

        inventoryText = menuFont.render('Inventory', False, WHITE)
        DISPLAYSURF.blit(inventoryText, (TILESIZE * 7.5, TILESIZE * 2.5))

        statsText = menuFont.render('Stats', False, WHITE)
        DISPLAYSURF.blit(statsText, (TILESIZE * 7.5, TILESIZE * 3.25))

        equipmentText = menuFont.render('Equipment', False, WHITE)
        DISPLAYSURF.blit(equipmentText, (TILESIZE * 7.5, TILESIZE * 4))
        
        quitText = menuFont.render('Quit', False, WHITE)
        DISPLAYSURF.blit(quitText, (TILESIZE * 7.5, TILESIZE * 4.75))
        
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

def checkFightInventory(monster):
    items = 0
    for item in playerInventory:
           items += 1

    if(items == inventoryMax):
           displayFightMessage('*Your inventory is too full', fightRoom, monster)
           return False
    else:
           return True

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def levelUp(stats):
    displayMessage('*You leveled up!', curRoom)

    tempInt = 0
    selection = 2.25
    while tempInt == 0:
        for menuEvent in pygame.event.get():
            if (menuEvent.type == QUIT):
                pygame.quit()
                sys.exit()
                
            elif (menuEvent.type == KEYDOWN):
                
                if(menuEvent.key == K_UP) and (selection > 2.25):
                    selection -= 0.25
                        
                if(menuEvent.key == K_DOWN) and (selection < 3.25):
                    selection += 0.25

                if(menuEvent.key == K_SPACE):
                    if(selection == 2.25):
                        stats['Vigor'] += 1
                        stats['Health'] += 5
                        tempInt = 1
                        
                    if(selection == 2.5):
                        stats['Power'] += 1
                        tempInt = 1
                        
                    if(selection == 2.75):
                        stats['Wisdom'] += 1
                        stats['Sanity'] += 5
                        tempInt = 1
                        
                    if(selection == 3):
                        stats['Dexterity'] += 1
                        tempInt = 1
                        
                    if(selection == 3.25):
                        stats['Luck'] += 1
                        tempInt = 1
                    

                
        for rw in range(MAPWIDTH):
            for cl in range(MAPHEIGHT):
                pygame.draw.rect(DISPLAYSURF, textures[curRoom[cl][rw]], (TILESIZE * rw, TILESIZE * cl, TILESIZE, TILESIZE))
        pygame.draw.rect(DISPLAYSURF, RED, (playerPos[0], playerPos[1], TILESIZE, TILESIZE))

        pygame.draw.rect(DISPLAYSURF, textures[MENU], (TILESIZE * 7, TILESIZE * 2, TILESIZE * 1.5, TILESIZE * 1.5))
        
        pygame.draw.rect(DISPLAYSURF, WHITE, (TILESIZE * 7.25, TILESIZE * selection, TILESIZE / 8, TILESIZE / 8)) 

        vigorText = invFont.render('Vigor = ' + str(playerStats['Vigor']), False, WHITE)
        DISPLAYSURF.blit(vigorText, (TILESIZE * 7.5, TILESIZE * 2.25))
        
        powerText = invFont.render('Power = ' + str(playerStats['Power']), False, WHITE)
        DISPLAYSURF.blit(powerText, (TILESIZE * 7.5, TILESIZE * 2.5))
        
        wisdomText = invFont.render('Wisdom = ' + str(playerStats['Wisdom']), False, WHITE)
        DISPLAYSURF.blit(wisdomText, (TILESIZE * 7.5, TILESIZE * 2.75))
        
        speedText = invFont.render('Dexterity = ' + str(playerStats['Dexterity']), False, WHITE)
        DISPLAYSURF.blit(speedText, (TILESIZE * 7.5, TILESIZE * 3))
        
        luckText = invFont.render('Luck = ' + str(playerStats['Luck']), False, WHITE)
        DISPLAYSURF.blit(luckText, (TILESIZE * 7.5, TILESIZE * 3.25))


        pygame.draw.rect(DISPLAYSURF, BLACK, (TILESIZE * 3, TILESIZE * (MAPHEIGHT - 2), TILESIZE * 4, TILESIZE / 2))

        textSurface = textFont.render('*Choose a stat to level up', False, WHITE)
        DISPLAYSURF.blit(textSurface,((TILESIZE * 3) + (TILESIZE / 8), (TILESIZE * (MAPHEIGHT - 2)) + (TILESIZE / 8)))
        
        pygame.display.update()
    stats['XP'] -= stats['Level'] * 5
    stats['Level'] += 1
    return stats

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def equipOption(item, yValue, room):
    tempInt = 0
    selection = 0
    
    while tempInt == 0:
        for equipEvent in pygame.event.get():
            if(equipEvent.type == QUIT):
                pygame.quit()
                sys.exit()
                
            elif(equipEvent.type == KEYDOWN):
                if(equipEvent.key == K_ESCAPE):
                    tempInt = 1
                    
                if(equipEvent.key == K_UP) and (selection > 0):
                    selection -= 20
                if(equipEvent.key == K_DOWN) and (selection < 40):
                    selection += 20
                

                if(equipEvent.key == K_SPACE):
                    if(selection == 0):
                        if(item in armor):
                            if(playerEquipment[0] == 'None'):
                                playerEquipment[0] = item
                                playerInventory.remove(item)

                            else:
                                playerInventory.append(playerEquipment[0])
                                playerEquipment[0] = item
                                playerInventory.remove(item)

                        elif(item in weapons):
                            if(playerEquipment[1] == 'None'):
                                playerEquipment[0] = item
                                playerInventory.remove(item)

                            else:
                                playerInventory.append(playerEquipment[0])
                                playerEquipment[0] = item
                                playerInventory.remove(item)
                        
                        tempInt = 1
                        
                    if(selection == 20):
                        playerInventory.remove(item)
                        tempInt = 1
                        
                    if(selection == 40):
                        tempInt = 1

        for rw in range(MAPWIDTH):
            for cl in range(MAPHEIGHT):
                pygame.draw.rect(DISPLAYSURF, textures[room[cl][rw]], (TILESIZE * rw, TILESIZE * cl, TILESIZE, TILESIZE))
        pygame.draw.rect(DISPLAYSURF, RED, (playerPos[0], playerPos[1], TILESIZE, TILESIZE))
        pygame.draw.rect(DISPLAYSURF, textures[MENU], (TILESIZE * 7, TILESIZE * 2, TILESIZE * 1.75, TILESIZE * 3))
        pygame.draw.rect(DISPLAYSURF, BLUE, (TILESIZE * 8, (yValue) - 16, TILESIZE / 2 + 32, (TILESIZE / 2) + 16))

        equipText = invFont.render('Equip', False, WHITE)
        DISPLAYSURF.blit(equipText, ((TILESIZE * 8) + 24, (yValue) - 8))

        discardText = invFont.render('Discard', False, WHITE)
        DISPLAYSURF.blit(discardText, ((TILESIZE * 8) + 24, (yValue) + 12))

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

while True:
    FLOOR = 0
    WALL = 1
    DOOR = 2
    PLANT = 3
    PLAYER = 4
    MENU = 5
    ENTRANCEDRESSER = 6
    LOCKEDDOOR = 7
    EMPTYDRESSER = 8
    CHAIR = 9
    TABLE = 10
    TILE = 11
    COUNTER = 12
    OVEN = 13
    SECRETWALL = 14
    SINK = 15
    BOOKCASE = 16
    DESK = 17
    GRAMAPHONE = 18
    

    TILESIZE = 128
    MAPWIDTH = 10
    MAPHEIGHT = 8

    BLACK = (0, 0, 0)
    BROWN = (153, 76, 0)
    GREEN = (0, 255, 0)
    GREY = (143, 143, 143)
    RED = (255, 0, 0)
    WHITE =(255, 255, 255)
    BLUE = (0, 0, 255)
    DARKGREEN = (100, 100, 0)
    DARKBROWN = (200, 50, 0)
    DARKGREY = (136, 136, 136)
    LIGHTGREY = (170, 170, 170)
    LIGHTBROWN = (250, 200, 0)
    

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    entranceRoom = [
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
        [WALL, ENTRANCEDRESSER, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
        [WALL, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
        [DOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, LOCKEDDOOR],
        [DOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, LOCKEDDOOR],
        [WALL, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
        [WALL, PLANT, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]
    ]

    livingRoom = [
        [WALL, WALL, WALL, WALL, DOOR, DOOR, WALL, WALL, WALL, WALL],
        [WALL, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, PLANT, WALL],
        [WALL, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
        [DOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, DOOR],
        [DOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, DOOR],
        [WALL, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
        [WALL, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]
    ]

    diningRoom = [
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
        [DOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
        [WALL, FLOOR, FLOOR, CHAIR, FLOOR, FLOOR, CHAIR, FLOOR, FLOOR, WALL],
        [WALL, FLOOR, FLOOR, TABLE, TABLE, TABLE, TABLE, FLOOR, FLOOR, DOOR],
        [WALL, FLOOR, FLOOR, TABLE, TABLE, TABLE, TABLE, FLOOR, FLOOR, DOOR],
        [WALL, FLOOR, FLOOR, CHAIR, FLOOR, FLOOR, CHAIR, FLOOR, FLOOR, WALL],
        [WALL, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]
        
    ]

    kitchenHallway = [
        [WALL, WALL, WALL, WALL, DOOR, DOOR, WALL, WALL, WALL, WALL],
        [LOCKEDDOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, DOOR],
        [LOCKEDDOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]
    ]

    kitchenRoom = [
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
        [WALL, TILE, TILE, TILE, TILE, TILE, TILE, TILE, TILE, SECRETWALL],
        [WALL, TILE, TILE, COUNTER, COUNTER, COUNTER, COUNTER, TILE, TILE, SECRETWALL],
        [WALL, TILE, TILE, COUNTER, COUNTER, COUNTER, COUNTER, TILE, TILE, WALL],
        [WALL, COUNTER, TILE, COUNTER, COUNTER, COUNTER, COUNTER, TILE, COUNTER, WALL],
        [WALL, SINK, TILE, TILE, TILE, TILE, TILE, TILE, OVEN, WALL],
        [WALL, COUNTER, TILE, TILE, TILE, TILE, TILE, TILE, COUNTER, WALL],
        [WALL, WALL, WALL, WALL, DOOR, DOOR, WALL, WALL, WALL, WALL, WALL]
    ]

    hiddenKitchenPassage = [
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
        [DOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, DOOR],
        [DOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, DOOR],
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]
    ]

    studyRoom = [
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
        [DOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, BOOKCASE, BOOKCASE, WALL],
        [DOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
        [WALL, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, DOOR],
        [WALL, DESK, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, DOOR],
        [WALL, DESK, CHAIR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
        [WALL, DESK, FLOOR, FLOOR, FLOOR, BOOKCASE, FLOOR, GRAMAPHONE, DESK, WALL],
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],        
    ]

    fightRoom = [
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
        [MENU, MENU, MENU, MENU, MENU, MENU, MENU, MENU, MENU, MENU],
        [MENU, MENU, MENU, MENU, MENU, MENU, MENU, MENU, MENU, MENU],
        [MENU, MENU, MENU, MENU, MENU, MENU, MENU, MENU, MENU, MENU]
    ]

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
    
    livingRoomKey = 0
    snack = 1
    glasses = 2
    ninjaSword = 3
    none = 4

    items = {
        livingRoomKey: 'Living Room Key',
        snack: 'Snack',
        glasses: 'Glasses',
        ninjaSword: 'Ninja Sword',
        none: 'None'
    }

    consumables = [items[snack]]
    dropables = [items[snack]]
    equipment = {
        'Glasses': 2,
        'Ninja Sword': 2,
        'None': 0
    }

    armor = ['Glasses']
    weapons = ['Ninja Sword']

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    textures = {
        FLOOR: BROWN,
        WALL: GREY,
        DOOR: BLACK,
        PLANT: GREEN,
        MENU: BLACK,
        ENTRANCEDRESSER: BLUE,
        LOCKEDDOOR: BLACK,
        EMPTYDRESSER: BLUE,
        CHAIR: BLACK,
        TABLE: DARKBROWN,
        TILE: WHITE,
        COUNTER: LIGHTGREY,
        OVEN: BLACK,
        SINK: BLUE,
        SECRETWALL: DARKGREY,
        BOOKCASE: DARKBROWN,
        DESK: LIGHTBROWN,
        GRAMAPHONE: BLACK
    }

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE))
    pygame.display.set_caption("TEST DEMO")
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
    
    pygame.font.init()
    textFont = pygame.font.SysFont('Comic Sans MS', 35)
    fightFont = pygame.font.SysFont('Comic Sans MS', 50)
    statFont = pygame.font.SysFont('Comic Sans MS', 40)
    titleFont = pygame.font.SysFont('Comic Sans MS', 100)
    menuFont = pygame.font.SysFont('Comic Sans MS', 30)
    invFont = pygame.font.SysFont('Comic Sans MS', 25)
    overFont = pygame.font.SysFont('Comic Sans MS', 256)
    subTitleFont = pygame.font.SysFont('Comic Sans MS', 72)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    gameOverParam = 0
    playerTileX = 5
    playerTileY = 5
    playerPos = [TILESIZE * playerTileX, TILESIZE * playerTileY]

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    curRoom = entranceRoom
    curTile = FLOOR

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    playerStats = setPlayerStats()
    playerInventory = ['Snack', 'Snack', 'Glasses']
    playerEquipment = ['None', 'None']
    inventoryMax = 9

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    while gameOverParam == 0:
        DISPLAYSURF.fill(BLACK)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------


        monster1 = {
            'Health': 1 * playerStats['Level'],
            'Vigor': 1 * playerStats['Level'],
            'Power': 1 * playerStats['Level'],
            'Dexterity': 1 * playerStats['Level'],
            'color': BLUE
        }

        monster2 = {
            'Health': 2 * playerStats['Level'],
            'Vigor': 2 * playerStats['Level'],
            'Power': 2 * playerStats['Level'],
            'Dexterity': 2 * playerStats['Level'],
            'color':GREEN
        }

        monsters = [monster1, monster2]

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

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

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

        for rw in range(MAPWIDTH):
            for cl in range(MAPHEIGHT):
                pygame.draw.rect(DISPLAYSURF, textures[curRoom[cl][rw]], (TILESIZE * rw, TILESIZE * cl, TILESIZE, TILESIZE))

        if(playerStats['Health'] <= 0):
            gameOverParam = gameOver()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

        if(playerStats['XP'] >= playerStats['Level'] * 5):
            playerStats = levelUp(playerStats)

        pygame.draw.rect(DISPLAYSURF, RED, (playerPos[0], playerPos[1], TILESIZE, TILESIZE))
        curTile = curRoom[playerTileY][playerTileX]

        playerStats = {
            'Health': playerStats['Health'],
            'Sanity': playerStats['Sanity'],
            'Vigor': playerStats['Vigor'],
            'Power': playerStats['Power'],
            'Wisdom': playerStats['Wisdom'],
            'Dexterity': playerStats['Dexterity'],
            'Luck': playerStats['Luck'],
            'Level': playerStats['Level'],
            'XP': playerStats['XP'],
            'Damage': playerStats['Power'] + equipment[playerEquipment[1]],
            'Defense': playerStats['Vigor'] + equipment[playerEquipment[0]]
        }


        playerInventory.sort()

        
        pygame.display.update()
