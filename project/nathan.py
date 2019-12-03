add_library('minim')
import random

backGround = PImage
nameImage = 'background.jpg'
startHeight = 0
font = ''

#variables for positioning
positions = []
usernames = []
levels = []
items = {}
#special items: Boat, Machete, Water and Pickaxe
item = ['B', 'M', 'W', 'P']


def setup():
    global backGround, nameImage, music
    backGround = loadImage(nameImage)
    background(backGround)
    textAlign(CENTER)
    textFont(createFont('Serif', 64))

#background and title settings
def setBackground():
    global backGround
    background(backGround)
    
def title():
    global startHeight
    setBackground()
    fill(255)
    rect(width / 2 - 350, startHeight, 700, 100)
    startHeight += 20
    
def getHeight():
    global startHeight
    return (startHeight < (height / 2))

def titleText():
    global startHeight
    fill(0)
    text('Race to the Top', width / 2, startHeight + 50)
    
def reset():
    global startHeight
    startHeight = 0
    
#menu
def menu():
    fill(255)
    rect(width / 2 - 300, height / 2 - 100, 600, 100)
    rect(width / 2 - 300, height / 2 + 100, 600, 100)
    fill(0)
    textAlign(CENTER)
    text('Start', width / 2, height / 2 - 25)
    text('Bord Opstelling', width / 2, height / 2 + 170)

#positie functies    
def getPositions(players):
    '''return list to another module to use and display'''
    global positions, items, usernames
    usernames = players
    del(positions[:])
    for x in players:
        positions.append(0)
    items = {}
    for x in players:
        items.update({x:[]})
    for x in players:
        levels.append(1)
    return positions
        
def getPosition(currentPlayer):
    '''returns the current player position'''
    global positions
    return str(positions[currentPlayer - 1])

def forward(player, steps):
    '''moving a player to another location'''
    global positions
    if positions[player - 1] + steps > 100:
        temp = positions[player - 1] + steps
        back = temp - 100
        positions[player - 1] = 100 - back
    else:
        positions[player - 1] += steps
    getPosition(player)
    
def backwards(player, steps, levelEnd=0):
    '''move a player back'''
    global positions
    if positions[player - 1] - steps < 0:
         positions[player - 1] = levelEnd
    else:
        positions[player - 1] -= steps
    getPosition(player) 
    
def swapPlace(first, next):
    '''function to swap users from place => handy dandy for when players reach the same hex'''
    global positions
    temp = positions[first - 1]
    temp2 = positions[next - 1]
    positions[first - 1] = temp2
    positions[next - 1] = temp
    
def addItem(player, buy=False):
    '''used to add a item to the dictionary'''
    global usernames, items, levels, item
    if buy:
        username = usernames[player - 1]
        lvl = levels[player - 1]
        items[username] += item[lvl - 1]
    
#items voor de levels
def getDebuff(player, throw=0):
    '''checks the debuff for a level'''
    global levels, items, usernames, positions
    if [2, 3, 4, 5] in levels:
        current = player - 1
        username == usernames[current]
        if levels[current] == 2 and 'B' not in items[username]:
            #water level debuff
            positions[current] -= 1
            return 'Ga 1 stap terug'
        elif levels[current] == 3 and 'M' not in items[username]:
            #jungle debuff
            return 'Lever 2 munten in'
        elif levels[current] == 4 and 'W' not in items[username]:
            #desert debuff
            positions[current] -= 2
            return 'Ga twee stappen terug'
        elif levels[current] == 5 and 'P' not in items[username]:
            #mountain debuff
            if throw in [5, 6]:
                positions[current] -= 1
                return str(throw) + ' gegooid. Ga 1 stap achteruit!'
        else:
            return 'Geen conditie!'
        
def getLevel(turn):
    '''returns the current the level the player is in'''
    global levels
    return str(levels[turn -1])
