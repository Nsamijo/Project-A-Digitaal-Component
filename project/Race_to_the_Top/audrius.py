import random
import copy

eventList = ['Aardbeving', 'Binnenweg', 'Explosieven', 'Goudmijn', 'Lawine', 'Medic', 'Overval', 'Schatkist', 'Storm', 'Windvlaag']
specialItems = ['boat.png', 'machete.png', 'water.png', 'axe.png']
toeristen = PImage
levels = ['Voet van de Berg', 'Rivier', 'Jungle', 'Woestijn', 'Gletsjer']
dices = []
eventImages = []
itemsImages = []
eventImage = PImage
selectedEvent = ''

#player data
usernames = []
positions = []
level = []
items = []
levelItems = []
trigger = 0
turn = 0

#to keep track of what is rolled
rolled = 0
rolledList = []

#loading event
xSize = 270
ySize = 375
x = 825
y = 400

#last player
last = ''

#description || scenes
load = True
eventScreen = False
describe = False

goldRobber = False
treasure = False
boom = False
flyOrFall = False
help = False


#binnenweg en aardbeving
shaky = False
shortcut = False
first = True
seconD = False
rollAgain = False
thunder = False

#to only execute once
once = True

#dices
start = 0
runTime = 20
rolled = None
next = False

def audriusSetup():
    global eventList, eventImages, dices, toeristen, specialItems, itemsImages
    for x in eventList:
        eventImages.append(loadImage(x + '.jpg'))
    eventImages.append(loadImage('eventphoto.jpg'))
    
    for x in range(1, 7):
        dices.append(loadImage('dice' + str(x) + '.png') )
    dices.append(loadImage('roll.png'))
    for x in dices:
        x.resize(150, 150)
    
    #load the images in voor de toeristen || die houden toch ervan om foto's te maken || #justasianstuff
    toeristen = loadImage('Tbackground.png')
    for x in specialItems:
        itemsImages.append(loadImage(x))
    for x in itemsImages:
        x.resize(150, 150)
    toeristen.resize(width, height)
    
#This is for the dices
def checkPoint():
    '''have a starting point || reset it'''
    global start
    start = frameCount
    
def displayDice(x, y):
    '''display the dice where the user will do the clicky thing with the mouse'''
    global dices
    fill(255)
    rect(x, y, 150, 150)
    image(dices[-1], x, y)
    
def rollingDice(x, y):
    '''display a rolling dice at a certain location'''
    global dices
    fill(255)
    rect(x, y, 150, 150)
    image(dices[random.randint(0, 5)], x, y)
    
def displayRolled(x, y):
    '''display the correct dice that has been rolled'''
    global rolled
    fill(255)
    rect(x, y, 150, 150)
    image(dices[rolled - 1], x, y)
    
def roll():
    '''roll the dice'''
    global rolled
    rolled = random.choice(range(1, 7))

def loading():
    '''loading to the Event'''
    global xSize, ySize, x, y, selectedEvent, eventImages
    global goldRobber, treasure, boom, flyOrFall, help, shortcut, first, shaky, thunder
    selectedEvent = random.choice(eventList)
    
    #filter which screen
    goldRobber = selectedEvent in ['Goudmijn', 'Overval']
    treasure = selectedEvent == 'Schatkist'
    boom = selectedEvent == 'Explosieven'
    flyOrFall = selectedEvent in [ 'Lawine', 'Windvlaag']
    help = selectedEvent == 'Medic'
    shortcut = selectedEvent == 'Binnenweg'
    shaky = selectedEvent == 'Aardbeving'
    thunder = selectedEvent == 'Storm'
    first = shortcut or shaky or thunder
    
    if frameCount % 5 == 0:
        img = random.choice(eventImages)
        img.resize(xSize, ySize)
        image(img, x, y)
    if xSize < 500 and ySize < 694:
        xSize += 6
        ySize += 9
        x -= 3
        y -= 6
        
    if xSize > 270 and ySize > 375:
        fill(255)
        textSize(40)
        textAlign(CENTER)
        text('Klik op de eventkaart!', width / 2, 120)
        
def title(pos=500):
    '''put the event that has been chosen'''
    global selectedEvent
    textAlign(CENTER)
    fill(240)
    rect(width / 2 - (textWidth(selectedEvent) / 2), pos, textWidth(selectedEvent), 80)
    fill(0)
    text(selectedEvent, width / 2, pos + 60)

def nextButton():
    '''next button'''
    rectMode(CORNER)
    textAlign(LEFT)
    fill(255, 0, 0)
    rect(1700, 900, 155, 70, 10)
    fill(0)
    textSize(64)
    text('Next', 1705, 960)
    
def descriptionButton():
    '''Button for description of the event'''
    rectMode(CORNER)
    textAlign(LEFT)
    fill(200)
    rect(1290, 900, 400, 70, 10)
    fill(0)
    textSize(64)
    text('Beschrijving', 1305, 955)
    
def description():
    '''description of the event'''
    global selectedEvent
    rectMode(CORNER)
    textAlign(LEFT)
    fill(255)
    rect(360, 300, 1200, 550, 5)
    fill(255, 0, 0)
    rect(1500, 790, 50, 50)
    
    #text
    fill(0)
    textSize(45)
    text(selectedEvent, 380, 380)
    textSize(35)
    text('X', 1515, 830)
    line(360, 400, 1560, 400)
    lines = []
    lines = loadStrings(selectedEvent + '.txt')
    textSize(24)
    
    #description
    startY = 500
    for x in lines:
        text(x, 390, startY)
        startY += 30
        
def setData(users, pos, lvl, itms, lvlitms):
    '''get the data from the players'''
    global usernames, positions, level, items, levelItems
    usernames = users
    positions = pos
    level = lvl
    items = itms
    levelItems = lvlitms

def setTriggerMan(triggerman):
    '''get the guy that has triggered the event || CONSEQUENCES'''
    global trigger
    trigger = triggerman

def event():
    '''function for our event'''
    global selectedEvent, eventImage
    eventImage = loadImage(selectedEvent + '.jpg')
    eventImage.resize(width, height)
    background(eventImage)
    
    #text || Event display name || Also some buttons for you know discription.. Yeah... >_<
    nextButton()
    descriptionButton()
    title()
    
    if describe:
        description()
        
def nextPlayerButton():
    '''ga naar de volgende speler'''
    if width - 350 < mouseX < width - 50 and height - 200 < mouseY < height - 125:
        fill(0, 255, 0)
    else:
        fill(0, 200, 0)
    rect(width - 350, height - 200, 300, 75)
    fill(0)
    textSize(32)
    textAlign(LEFT)
    text('Volgende Speler', width - 325, height - 150)

def exitButton():
    '''Exit Button'''
    if width - 350 < mouseX < width - 50 and height - 200 < mouseY < height - 125:
        fill(255, 0, 0)
    else:
        fill(200, 0, 0)
    rect(width - 350, height - 200, 300, 75)
    fill(0)
    textSize(32)
    textAlign(LEFT)
    text('Event Eindigen', width - 315, height - 150)
    
def showStats(r=0, g=0, b=0):
    '''show the player stats IN A BOX || now aint that cool? '''
    global positions, level, levels, turn
    
    updateLevels()
    textSize(45)
    #position and levels
    pos = 'Huidige positie (na verplaatsing): ' + str(positions[turn])
    lvl = 'Huidige level : ' + str(level[turn]) + ' (' + levels[level[turn]] + ')'
    #boxes to but the data in || lovely aint it?
    fill(r, g, b)
    
    if textWidth(pos) > textWidth(lvl):
        rect(width/2 - textWidth(pos)/2, height / 2 + 75, textWidth(pos), 200)
    else:
        rect(width/2 - textWidth(lvl)/2, height / 2 + 75, textWidth(lvl), 200)
    fill(0)
    #position our text somewhat correctly || as I said
    textAlign(LEFT)
    if textWidth(pos) > textWidth(lvl):
        text(pos, width / 2 - textWidth(pos)/2, height / 2 + 125)
        text(lvl, width / 2 - textWidth(pos)/2, height / 2 + 225)
    else:
        text(pos, width / 2 - textWidth(lvl)/2, height / 2 + 125)
        text(lvl, width / 2 - textWidth(lvl)/2, height / 2 + 225)

def showCustomStats(player, r=0, g=0, b=0):
    '''show the stats of a given player'''
    global positions, level, levels
    rectMode(CORNER)
    updateLevels()
    textSize(45)
    #position and levels
    pos = 'Huidige positie (na verplaatsing): ' + str(positions[player])
    lvl = 'Huidige level : ' + str(level[player]) + ' (' + levels[level[player]] + ')'
    #boxes to but the data in || lovely aint it?
    fill(r, g, b)
    
    if textWidth(pos) > textWidth(lvl):
        rect(width/2 - textWidth(pos)/2, height / 2 + 75, textWidth(pos), 200)
    else:
        rect(width/2 - textWidth(lvl)/2, height / 2 + 75, textWidth(lvl), 200)
    fill(0)
    #position our text somewhat correctly || as I said
    textAlign(LEFT)
    if textWidth(pos) > textWidth(lvl):
        text(pos, width / 2 - textWidth(pos)/2, height / 2 + 125)
        text(lvl, width / 2 - textWidth(pos)/2, height / 2 + 225)
    else:
        text(pos, width / 2 - textWidth(lvl)/2, height / 2 + 125)
        text(lvl, width / 2 - textWidth(lvl)/2, height / 2 + 225)
        
def updateLevels():
    '''update the levels because yeah'''
    global level, positions
    #UPDATE THE LEVELS || PLS WORK
    temp = 0
    while temp <= len(positions) - 1:
        for x in [21, 41, 61, 81]:
            if positions[temp] > x:
                level[temp] = x // 20
        temp += 1

def lawineEnWindvlaag():
    '''falling snow || Very dangerous, not a joking matter || Lawine'''
    '''the breath of the wild || will carry you || literally || you move like 5 steps forward || hecking nice right? || Windvlaag'''
    global level, positions, selectedEvent, usernames, once
    global turn
    #LOGIC
    #edit the positions for the players
    if once:
        x = 0
        while x < len(positions):
            if selectedEvent == 'Lawine':
                positions[x] -= 5
                if positions[x] < 0:
                    positions[x] = 0
            elif selectedEvent == 'Windvlaag':
                positions[x] += 5
            x += 1
        once = False

    #edit the player level if these have been downgraded to another level
    player = 0
    while player < len(level):
        lvl = 0
        for x in [21, 41, 61, 81]:
            if positions[player] > x:
                level[player] = lvl
                break
            lvl += 1
        player += 1
        
    #SCREEN
    textSize(64)
    background(eventImage)
    title(80)
    
    if selectedEvent == 'Windvlaag':
        data = 'Speler ' + usernames[turn] + ': Ga 5 vakken vooruit'
    else:
        data = 'Speler ' + usernames[turn] + ': Ga 5 vakken terug'
    #boxes to but the data in || lovely aint it? || Tis copy past || could probably have written a function for dis
    fill(255)
    rect(width/2 - textWidth(data)/2, height / 2 - 50, textWidth(data), 100)
    fill(0)
    text(data, width / 2, height / 2 + 20)
    showStats(255, 255, 255)
    
    if turn  + 1 == len(usernames):
        exitButton()
    else:
        nextPlayerButton()

def ba_BOOM():
    '''this one is hecking danger || it literally explodes || like really || this is the function for "Explosieven" '''
    global trigger, positions, level, usernames, levels
    global eventImage, turn
    #LOGIC
    #get the data from the player and change that first
    startLvls = [0, 21, 41, 61, 81]
    if level[trigger] == 0: 
        positions[trigger] = 0
    else:
        positions[trigger] = level[trigger] * 20 + 21
    #change all of the players in the same level
    temp = 0
    for x in level:
        if level[trigger] == x:
            positions[temp] = positions[trigger]
        temp += 1
            
    #SCREEN
    #display the stuff ya know and with stuff we mean data
    textSize(64)
    textAlign(CENTER)
    background(eventImage)
    title(80)
    
    #Kijken of een event effect heeft op een speler of niet
    if level[turn] == level[trigger]:
        data = 'Speler ' + usernames[turn] + ': Ga terug naar het begin van de level'
    else:
        data = 'Speler ' + usernames[turn] + ': Deze event heeft geen effect op jou'
    #data from a player || level and position tis the remix from ignition
    pos = 'Huidige positie: ' + str(positions[turn])
    lvl = 'Huidige level : ' + str(level[turn]) + ' (' + levels[level[turn]] + ')'
    
    #boxes to but the data in || lovely aint it?
    fill(200, 20, 0)
    rect(width/2 - textWidth(data)/2, height / 2 - 50, textWidth(data), 100)
    fill(0)
    text(data, width / 2, height / 2 + 20)
    showStats(200, 20)
    
    #buttons || hehe butt
    if turn  + 1 == len(usernames):
        exitButton()
    else:
        nextPlayerButton()
            
def goudmijnOverval():
    '''this is the code || either you find gold or die poor '''
    global selectedEvent, eventImage, start
    global usernames, next, rolled, turn
    
    #For the gold-diggers and the robbers || Who doesn't love gold
    textSize(64)
    background(eventImage)
    title(80)
    textAlign(CENTER)
    #status of the player
    if not next:
        data = 'Speler ' + usernames[turn] + ': Rol om aantal munten te bepalen'
    else:
        if rolled == 1:
            m = ' munt'
        else:
            m = ' munten'
        if selectedEvent == 'Goudmijn':
            data = 'Speler ' + usernames[turn] + ': Ontvangt ' + str(rolled) + m
        elif selectedEvent == 'Overval':
            data = 'Speler ' + usernames[turn] + ': Verliest ' + str(rolled) + m
    if selectedEvent == 'Goudmijn':
        fill(255, 250, 0)
    else:
        fill(200)
    rect(width / 2 - (textWidth(data) / 2), height / 2 - 60, textWidth(data), 100)
    fill(0)
    text(data, width / 2, height / 2)
    
    #leaves a dice || rolling dice
    if not next:
        displayDice(width / 2 - 75, height / 2 + 75)
    elif next and frameCount - start < runTime:
        rollingDice(width / 2 - 75, height / 2 + 75)
    elif next:
        displayRolled(width / 2 - 75, height / 2 + 75)
        #buttons here || exit or next player
        if turn  + 1 == len(usernames):
            exitButton()
        else:
            nextPlayerButton()
        
def schatKist():
    '''screen for out treasure || YEAH WE RICH BOI'''
    global eventImage, turn, usernames, once, items
    background(eventImage)
    textSize(64)
    title(80)
    
    #Player get to take a item || probably the shortest function that has a screen
    if items[turn] < 3:
        data = 'Speler ' + usernames[turn] + ': Pak een voorwerp'
    else:
        data = 'Speler ' + usernames[turn] + ': Item limiet bereikt'
    fill(255, 215, 0)
    rect(width/2 - textWidth(data)/2, height / 2 - 50, textWidth(data), 100)
    fill(0)
    text(data, width / 2, height / 2 + 20)
    
    if once and items[turn] < 3:
        items[turn] += 1
        once = False
    
    #buttons || exit or next player
    if turn  + 1 == len(usernames):
        exitButton()
    else:
        nextPlayerButton()
        
def determineLast():
    '''determine who the last player is'''
    global last
    last = usernames[ positions.index(min(positions)) ]
        
def medic():
    '''this is the medic event || carry the last player || now aint that a b*tch || life's unfair DEAL WITH IT!'''
    global positions, usernames, level, levels, rolledList, once, last
    global next, eventImage
    background(eventImage)
    textSize(64)
    title(80)
    textAlign(LEFT)

    #setup the text real good
    rule = 'Iedereen rolt voor ' + last
    data = 'Speler ' + usernames[turn] + ': Rol de dobbelsteen voor ' + last
    
    if len(rolledList) < len(usernames):
        toMove = 'Aantal hulp tot nu toe: ' + str( sum(rolledList) )
    else:
        toMove = 'Speler ' + last + ': Ga ' + str( sum(rolledList) ) + ' stappen vooruit'
    
    #draw the rectangles for our data
    if len(rolledList) < len(usernames):
        fill(255)
        if textWidth(rule) > textWidth(data):
            rect(width / 2 - textWidth(rule) / 2, height / 2 - 100, textWidth(rule), 200)
        else:
            rect(width / 2 - textWidth(data) / 2, height / 2 - 100, textWidth(data), 200)
            
        rect(width / 2 - textWidth(toMove) / 2, height / 2 + 120, textWidth(toMove) , 75)
    else:
        fill(255)
        rect(width / 2 - textWidth(toMove) / 2, height / 2 - 100, textWidth(toMove) , 75)
            
    if len(rolledList) < len(usernames):
        fill(255, 0, 0)
        if textWidth(rule) > textWidth(data):
            text( rule, width / 2 - textWidth(rule) / 2, height / 2 - 40)
            text(data, width / 2 - textWidth(rule) / 2, height / 2, + 40)
        else:
            text( rule, width / 2 - textWidth(data) / 2, height / 2 - 40)
            text(data, width / 2 - textWidth(data) / 2, height / 2 + 40)
        text(toMove, width / 2 - textWidth(toMove) / 2, height / 2 + 180)
    else:
        fill(255, 0, 0)
        text(toMove, width / 2 - textWidth(toMove) / 2, height / 2 - 40)
        if once:
            #update the position
            if positions[ positions.index( min(positions) ) ] + sum(rolledList) in positions:
                positions[positions.index(positions[ positions.index( min(positions) ) ] + sum(rolledList)) ] -= 1
            positions[ positions.index( min(positions) ) ] += sum(rolledList)
            once = False
    if not once:
        showCustomStats(usernames.index(last), 255)
        
    #the dices and the buttons
    if not next:
        displayDice(width / 2 - 75, height / 2 + 200)
    elif next and frameCount - start < runTime:
        rollingDice(width / 2 - 75, height / 2 + 200)
    elif next and once:
        displayRolled(width / 2 - 75, height / 2 + 200)
    #buttons here || exit or next player
    if next:
        if turn  + 1 == len(usernames):
            exitButton()
        else:
            nextPlayerButton()
            
def binnenWeg():
    '''shortcut for everyone'''
    global positions, once, turn, eventImage, usernames, rolled, rolledList, positions
    global next, first, seconD
    
    #settings
    textSize(64)
    background(eventImage)
    title(80)
    textAlign(LEFT)
    
    #player that has to throw || contains of 2 parts
    if first and not seconD:
        #this part the players throw
        rule = 'Iedereen gaat ' + str(sum(rolledList)) + ' stappen vooruit'
        if not next:
            data = 'Speler ' + usernames[turn] + ': Rol de dobbelsteen'
        else:
            data = 'Speler ' + usernames[turn] + ': ' + str(rolled) + ' gerold'
            
        fill(220, 0, 0)
        if len(data) > len(rule):
            rect(width / 2 - textWidth(data) / 2, height / 2 - 50, textWidth(data), 200)
        else:
            rect(width / 2 - textWidth(rule) / 2, height / 2 - 50, textWidth(rule), 200)
            
        fill(0)
        if len(data) > len(rule):
            text(rule, width / 2 - textWidth(data) / 2, height / 2  + 20)
            text(data, width / 2 - textWidth(data) / 2, height / 2 + 100)
        else:
            text(rule, width / 2 - textWidth(rule) / 2, height / 2 + 20)
            text(data, width / 2 - textWidth(rule) / 2, height / 2 + 100)
            
        if once and len(rolledList) == len(usernames):
            for x in range(len(usernames)):
                positions[x] += sum(rolledList)
                updateLevels()
            once = False
    elif seconD:
        #this part the player sees where they have to be || which is very lit fam
        data = 'Speler ' + usernames[turn]
        fill(220, 0,0)
        rect(width / 2 - textWidth(data) / 2, height / 2 - 50, textWidth(data), 100)
        fill(0)
        text(data, width / 2 - textWidth(data) / 2, height / 2 + 20) 
        showCustomStats(turn, 220)
    
    #dices and buttons
    if first:
        if not next:
            displayDice(width / 2 - 75, height / 2 + 200)
        elif next and frameCount - start < runTime:
            rollingDice(width / 2 - 75, height / 2 + 200)
        elif next:
            displayRolled(width / 2 - 75, height / 2 + 200)
            #buttons here || exit or next player
            nextPlayerButton()
    elif seconD:
        if turn + 1 == len(usernames):
            exitButton()
        else:
            nextPlayerButton()
        
def earthDoesTheMacarena():
    '''earthquake || this causes disrupture'''
    global eventimage, usernames, turn
    global positions, turn, rolled, rolledList, first, seconD, rollAgain, next, once
    #settings
    textSize(64)
    background(eventImage)
    title(80)
    textAlign(LEFT)
    
    if first:
        if not rollAgain:
            data = 'Speler ' + usernames[turn] + ': Rol om te bepalen welke plaats je krijgt'
        else:
            data = 'Speler ' + usernames[turn] + ': Je hebt evenveel gerold! Rol opieuw!'
            
        fill(200, 0, 25)
        rect(width / 2 - textWidth(data) / 2, height / 2 - 50, textWidth(data), 100)
        fill(255)
        text(data, width / 2 - textWidth(data) / 2, height / 2 + 20)
    elif seconD:
        if once:
            #create a duplicate of the list and sort them
            sortedPositions = copy.deepcopy(positions)
            sortedRolled = copy.deepcopy(rolledList)
            sortedPositions.sort()
            sortedRolled.sort()
            
            #link them to the proper people
            temp = 0
            for x in rolledList:
                temp2 = 0
                for y in sortedRolled:
                    if x == y:
                        positions[temp] = sortedPositions[temp2]
                    temp2 += 1
                temp += 1 
            once = False
            updateLevels()
            
        data = 'Speler ' + usernames[turn]
        fill(200, 0, 25)
        rect(width / 2 - textWidth(data) / 2, height / 2 - 50, textWidth(data), 100)
        fill(255)
        text(data, width / 2 - textWidth(data) / 2, height / 2 + 20)
        showCustomStats(turn, 200, 0, 25)
        
    #dices and buttons
    if first:
        if not next:
            displayDice(width / 2 - 75, height / 2 + 200)
        elif next and frameCount - start < runTime:
            rollingDice(width / 2 - 75, height / 2 + 200)
        elif next:
            displayRolled(width / 2 - 75, height / 2 + 200)
            #buttons here || exit or next player
            nextPlayerButton()
    elif seconD:
        if turn + 1 == len(usernames):
            exitButton()
        else:
            nextPlayerButton()  
            
def lightningMcQueen():
    '''this is the storm || KA-CHOW || Fast like lightning'''
    global positions, usernames, level, levels, rolledList, once
    global next, eventImage, turn
    background(eventImage)
    textSize(64)
    title(80)
    textAlign(LEFT)

    #setup the text real good
    rule = 'Iedereen rolt om terug te gaan'
    data = 'Speler ' + usernames[turn] + ': Rol de dobbelsteen om terug the gaan :) '
    
    if first:
        toMove = 'Aantal posities terug tot nu toe: ' + str( sum(rolledList) )
    else:
        toMove = 'Speler ' + usernames[turn] + ': Ga ' + str( sum(rolledList) ) + ' posities achteruit'
    
    #draw the rectangles for our data
    if first:
        fill(255)
        if textWidth(rule) > textWidth(data):
            rect(width / 2 - textWidth(rule) / 2, height / 2 - 100, textWidth(rule), 200)
        else:
            rect(width / 2 - textWidth(data) / 2, height / 2 - 100, textWidth(data), 200)
            
        rect(width / 2 - textWidth(toMove) / 2, height / 2 + 120, textWidth(toMove) , 75)
    elif seconD:
        fill(255)
        rect(width / 2 - textWidth(toMove) / 2, height / 2 - 100, textWidth(toMove) , 75)
            
    if first:
        fill(255, 0, 0)
        if textWidth(rule) > textWidth(data):
            text( rule, width / 2 - textWidth(rule) / 2, height / 2 - 40)
            text(data, width / 2 - textWidth(rule) / 2, height / 2, + 40)
        else:
            text( rule, width / 2 - textWidth(data) / 2, height / 2 - 40)
            text(data, width / 2 - textWidth(data) / 2, height / 2 + 40)
        text(toMove, width / 2 - textWidth(toMove) / 2, height / 2 + 180)
    elif seconD:
        fill(255, 0, 0)
        text(toMove, width / 2 - textWidth(toMove) / 2, height / 2 - 40)
        if once:
            #update the position
            for x in usernames:
                positions[usernames.index(x)] -= sum(rolledList)
                if positions[usernames.index(x)] < 0:
                    positions[usernames.index(x)] = 0
                updateLevels()
            once = False
            
    if not once:
        showCustomStats(turn, 255)
        
    #the dices and the buttons
    if not next:
        displayDice(width / 2 - 75, height / 2 + 200)
    elif next and frameCount - start < runTime:
        rollingDice(width / 2 - 75, height / 2 + 200)
    elif next and first:
        displayRolled(width / 2 - 75, height / 2 + 200)
    #buttons here || exit or next player
    if next:
        if turn  + 1 == len(usernames) and not first:
            exitButton()
        else:
            nextPlayerButton()

def exit():
    '''user to return back to the players screens'''
    reset()
    return False

def reset():
    '''reset all the values for a new event'''
    global load, eventScreen, describe
    global xSize, ySize, x, y, selectedEvent
    global turn, rolled, next, once, last, rolledList, first, seconD
    turn = 0

    rolled = ''
    rolledList = []
    
    #loading event
    xSize = 270
    ySize = 375
    x = 825
    y = 400

    #description || scenes
    load = True
    eventScreen = False
    describe = False
    
    #screens binnenweg
    first = True
    seconD = False
    
    #last
    last = ''
    
    #only do the logic once
    once = True

    #dices
    start = 0
    runTime = 20
    rolled = None
    next = False    
        
def mouseEvent():
    '''all the mouse fuhnctionality for events'''
    global usernames, turn
    global load, eventScreen, describe
    global goldRobber, next, turn
    global treasure, boom, flyOrFall, help, shortcut, first, seconD, shaky, thunder
    global rolled, rolledList
    if load:
        load = False
        eventScreen = True
    if eventScreen:
        if 1290 < mouseX < 1690 and 900 < mouseY < 970:
            describe = True
        elif 1500 < mouseX < 1550 and 790 < mouseY < 840 :
            describe = False
        elif 1700 < mouseX < 1855 and 900 < mouseY < 970:
            eventScreen = False
            if help:
                determineLast()
    elif goldRobber:
        if width / 2 - 75 < mouseX < width / 2 + 75 and height / 2 + 75 < mouseY < height / 2 + 225 and not next:
            next = True
            checkPoint()
            roll()
        elif next and width - 350 < mouseX < width - 50 and height - 200 < mouseY < height - 125:
            next = False
            if turn < len(usernames) - 1:
                turn += 1
                next = False
            else:
                next = False
                turn = 0
                return exit()
    elif treasure or boom or flyOrFall:
        if width - 350 < mouseX < width - 50 and height - 200 < mouseY < height - 125:
            if turn < len(usernames) - 1:
                turn += 1
                if treasure:
                    once = True
            else:
                turn = 0
                return exit()
    elif help:
        if width / 2 - 75 < mouseX < width / 2 + 75 and height / 2 + 200 < mouseY < height / 2 + 350 and not next:
            next = True
            checkPoint()
            roll()
            rolledList.append(rolled)
        elif next and width - 350 < mouseX < width - 50 and height - 200 < mouseY < height - 125:
            next = False
            if turn < len(usernames) - 1:
                turn += 1
                next = False
            else:
                next = False
                turn = 0
                return exit()
    elif shortcut:
        if first:
            if width / 2 - 75 < mouseX < width / 2 + 75 and height / 2 + 200 < mouseY < height / 2 + 350 and not next:
                next = True
                checkPoint()
                roll()
                rolledList.append(rolled)
            elif next and width - 350 < mouseX < width - 50 and height - 200 < mouseY < height - 125:
                if turn < len(usernames) - 1:
                    turn += 1
                    next = False
                elif turn + 1 == len(usernames):
                    turn = 0
                    first = False
                    seconD = True
        elif seconD:
            if width - 350 < mouseX < width - 50 and height - 200 < mouseY < height - 125:
                if turn < len(usernames) - 1:
                    turn += 1
                else:
                    turn = 0
                    return exit()
    elif shaky:
        if first:
            if width / 2 - 75 < mouseX < width / 2 + 75 and height / 2 + 200 < mouseY < height / 2 + 350 and not next:
                next = True
                checkPoint()
                roll()
                rollAgain = rolled in rolledList
                if not rollAgain:
                    rolledList.append(rolled)
            elif next and width - 350 < mouseX < width - 50 and height - 200 < mouseY < height - 125:
                if turn < len(usernames) - 1:
                    turn += 1
                    next = False
                elif turn + 1 == len(usernames):
                    turn = 0
                    first = False
                    seconD = True
        elif seconD:
            if width - 350 < mouseX < width - 50 and height - 200 < mouseY < height - 125:
                if turn < len(usernames) - 1:
                    turn += 1
                else:
                    turn = 0
                    return exit()
    elif thunder:
        if first:
            if width / 2 - 75 < mouseX < width / 2 + 75 and height / 2 + 200 < mouseY < height / 2 + 350 and not next:
                next = True
                checkPoint()
                roll()
                rolledList.append(rolled)
            elif next and width - 350 < mouseX < width - 50 and height - 200 < mouseY < height - 125:
                if turn < len(usernames) - 1:
                    turn += 1
                    next = False
                elif turn + 1 == len(usernames):
                    turn = 0
                    first = False
                    seconD = True
        elif seconD:
            if width - 350 < mouseX < width - 50 and height - 200 < mouseY < height - 125:
                if turn < len(usernames) - 1:
                    turn += 1
                else:
                    turn = 0
                    return exit()
            
def eventScreens():
    '''event screens || all will be linked here'''
    global load, eventScreen, selectedEvent
    global goldRobber,  treasure, boom, flyOrFall, help, shortcut, shaky, thunder
    if load:
        loading()
    elif eventScreen:
        event()
    elif goldRobber:
        goudmijnOverval()
    elif treasure:
         schatKist()
    elif boom:
        ba_BOOM()
    elif flyOrFall:
        lawineEnWindvlaag()
    elif help:
        medic()
    elif shortcut:
        binnenWeg()
    elif shaky:
        earthDoesTheMacarena()
    elif thunder:
        lightningMcQueen()
        
#einde events ---------------------------------------------------------------------------------- nu voor de toeristen
def toeristScreen():
    '''this here will be the shop for toerists'''
    global level, trigger, toeristen, usernames, levels, itemsImages, once
    global first
    #settings
    background(toeristen)
    rectMode(CORNER)
    textAlign(CENTER)
    
    #check if the user has not exceeded items max limit
    if items[trigger] == 3:
        once = False
    #title--------------------------------------------------------------------------------------
    textSize(64)
    if level[trigger] == 0:
        fill(0, 0, 255)
    elif level[trigger] == 1:
        fill(0, 255, 0)
    elif level[trigger] == 2:
        fill(255, 51, 255)
    else:
        fill(255)
    rect(width / 2 - textWidth(levels[trigger]) / 2, 80, textWidth(levels[trigger]), 80)
    fill(0)
    text(levels[level[trigger] + 1], width / 2, 140)
    #-------------------------------------------------------------------------------------------
    #item placement || show which item they can buy
    if level[trigger] == 0:
        fill(0, 0, 255)
    elif level[trigger] == 1:
        fill(0, 255, 0)
    elif level[trigger] == 2:
        fill(255, 51, 255)
    else:
        fill(255)
    textSize(60)
    itemList = ['Boat', 'Machete', 'Waterfles', 'IJsbijl']
    prijzen = ['5 munten', '10 munten', '15 munten', '20 munten']
    if items[trigger] == 3:
        lvl = 'Voorwerp limit bereikt'
    else:
        lvl = 'Level item: ' + itemList[level[trigger]]
    prize = prijzen[level[trigger]]
    #boxes for the item image and buy option
    rect(width / 2 - 300, height / 2 - 50, 300, 300)
    rect(width / 2, height / 2 - 50, 300, 300)
    rect(width / 2 - textWidth(lvl) / 2, height / 2 - 200, textWidth(lvl), 80)
    
    #for the big boxes text and a image and level item------------------------------------
    fill(0)
    text(lvl, width / 2, height / 2 - 140, 140)
    image(itemsImages[level[trigger]] , width / 2 + 75, height / 2 + 20)
    
    #koop knop---------------------------------------------------------------------------
    textSize(45)
    if once:
        fill(255, 0, 0)
    else:
        fill(200)
    rect(width / 2 - 150 - textWidth('Koop') / 2, height / 2 + 185, textWidth('Koop'), 60)
    fill(0)
    text('Koop', width / 2 - 150, height / 2 + 225)
    text('Prijs:', width / 2 - 150, height / 2 + 40)
    text(prize, width / 2 - 150, height / 2 + 80)
    
    #confirmation || so that people don't cheat-----------------------------------------
    if not first:
       fill(255)
       textSize(45)
       rect(width / 2 - 300, height / 2 - 50, 600, 300)
       fill(0)
       text('Genoeg geld?', width / 2, height / 2 + 10)
       
       #not enough money----------------------------------------------------------------
       fill(255, 0, 0)
       rect(width / 2 - 250, height / 2 + 180, textWidth('I lied'), 55) 
       fill(0)
       text('I lied', width / 2 - 250 + textWidth('I lied') / 2, height / 2 + 220)
       
       #rich gang || *throws money* ----------------------------------------------------
       fill(0, 255, 0)
       rect(width / 2 + 3, height / 2 + 180, textWidth('Gucci Gang'), 55) 
       fill(0)
       text('Gucci Gang', width / 2 + 3 + textWidth('Gucci Gang') / 2, height / 2 + 220)
    
    #exit button-------------------------------------------------------------------------
    if first:
        textAlign(LEFT)
        if width - 300 < mouseX < width - 100 and height - 200 < mouseY < height - 145:
            fill(255, 0, 0)
        else:
            fill(200, 0, 0)
        rect(width - 300, height - 200, 200, 55)
        fill(0)
        text('Exit Shop', width - 300, height - 160)
    
def mouseToerist():
    '''mouse functionality voor de toeristenwinkel'''
    global first, levelItems, seconD, trigger, once, items
    if first:
        if width - 300 < mouseX < width - 100 and height - 200 < mouseY < height - 145:
            first = True
            return exit()
        if width / 2 - 150 - textWidth('Koop') / 2 < mouseX < width / 2 - 150 + textWidth('Koop') and height / 2 + 185 < mouseY < height / 2 + 245 and once:
            first = False
    elif not first:
        textSize(30)
        if width / 2 + 3 < mouseX < width / 2 + 250 and height / 2 + 180 < mouseY < height / 2 + 235:
            if once and items[trigger] + 1 <= 3:
                levelItems[trigger].append(['Boat', 'Machete', 'Waterfles', 'IJsbijl'][level[trigger]])
                items[trigger] += 1
                once = False
            first = True
        if width / 2 - 250 < mouseX < width / 2 - 250 + 106 and height / 2 + 180 < mouseY < height / 2 + 235:
            first = True
