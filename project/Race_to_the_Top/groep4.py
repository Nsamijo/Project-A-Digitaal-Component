import random
#Module voor Digitaal component

#globals hier definen aub || zet het onder je naam en dan waarvoor deze is

#nathan globals

# players data
usernames = []
positions = []
level = []
items = []
turn = 0

#title
startHeight = 0

#shift to another authors 
nathan = True
jan = False

#screen booleans
titel = True
menu = False
opstelling = False
showOpstelling = False

#screen data
backgrounds = []
logo = PImage
backImages = ['begin.jpg']

#jan globals
valkuilen = []
winkel = []
tunnels = []
vogels = []
events = []
toeristenWinkel = [21, 41, 61, 81]

#Nathan Samijo
def nathanSetup():
    global backImages, backgrounds, logo
    for x in backImages:
        backgrounds.append(loadImage(x))
    logo = loadImage('logo.png')
    logo.resize(200, 150)
        
def setBackground():
    global backgrounds, usernames, level, logo
    if len(usernames) == 0:
        background(backgrounds[0])
        image(logo, width / 2 - 100, 10)
    else:
        background(backgrounds[level[turn]])
        image(logo, width / 2 - 100, 10)
        
def title():
    '''title drop down '''
    global startHeight
    setBackground()
    
    textAlign(CENTER)
    textSize(64)
    #drop down race to the top
    fill(255)
    rect(width / 2 - 350, startHeight, 700, 100)
    if startHeight < (height / 2 + 300):
        startHeight += 20
    else:
        fill(0)
        text('Race to the Top', width / 2, startHeight + 75)
        if frameCount % 20 == 0: 
            fill(255)
            textSize(30)
            text('Klik op uw rechtermuis of linkermuis knop', width / 2, startHeight - 75)
        
def meNu():
    '''this is the menu'''
    rectMode(CORNER)
    setBackground()
    #menu rectangles
    fill(255)
    rect(width / 2 - 300, height / 2 - 100, 600, 100, 50)
    rect(width / 2 - 300, height / 2 + 100, 600, 100, 50)
    rect(width / 2 - 300, height / 2 + 300, 600, 100, 50)
    
    #text for the menu
    fill(0)
    textSize(64)
    textAlign(CENTER)
    text('Start Spel', width / 2, height / 2 - 25)
    text('Opstelling', width / 2, height / 2 + 170)
    text('Spel Regels', width / 2, height / 2 + 370)
    
def mouseNathan():
    '''to make buttons work'''
    global titel, menu, opstelling, nathan, jan
    if titel:
        menu = True
        titel = False
    elif menu:
        if width / 2 - 300 < mouseX < width / 2 + 300 and height / 2 + 100 < mouseY <  height / 2 + 200:
            menu = False
            opstelling = True
            nathan = False
            jan = True
        
        
#Jan Roozemond
def standaard():
    '''this here is the standard layout for '''
    #valkuilen
    global valkuilen, winkel, tunnels, vogels, events
    #valkuilen
    valkuilen = [4, 10, 18, 26, 28, 33, 38, 45, 48, 56, 62, 67, 70, 75, 78, 88, 90, 95]
    #winkel
    winkel = [11, 19, 23, 31, 53, 64, 72, 77, 89, 96]
    #tunnels
    tunnels = [12, 16, 29, 36, 51, 54, 68, 73]
    #geluksvogels
    vogels = [5, 13, 17, 27, 37, 52, 63, 76, 83, 91]
    #events
    events = [8, 15, 25, 34, 47, 55, 65, 74, 86, 92]
    
def generate():
    global valkuilen, winkel, tunnels, vogels, events
    Randomized = True
    
    #vakken waar pionnen in geplaatst mogen worden, alle vakken min de stop en overgang vakken.
    land = range(4,19)
    rivier = range(22,39)
    jungle = range(42, 59)
    woestijn = range(62,79)
    gletsjer = range(82,99)


    # willekeurige plaatsing door random method
    # valkuilen
    valkuilen = random.sample(land,2)
    valkuilen += random.sample(rivier,3)
    valkuilen += random.sample(jungle,5)
    valkuilen += random.sample(woestijn,5)
    valkuilen += random.sample(gletsjer,3)
    valkuilen.sort()

    # dubbele voorkomen
    land = list(set(land) - set(valkuilen))
    rivier = list(set(rivier) - set(valkuilen))
    jungle = list(set(jungle) - set(valkuilen))
    woestijn = list(set(woestijn) - set(valkuilen))
    gletsjer = list(set(gletsjer) - set(valkuilen))

    #winkel
    winkel = random.sample(land,2)
    winkel += random.sample(rivier,2)
    winkel += random.sample(jungle,3)
    winkel += random.sample(woestijn,2)
    winkel += random.sample(gletsjer,1)
    winkel.sort()

    # dubbele voorkomen 
    land = list(set(land) - set(winkel))
    rivier = list(set(rivier) - set(winkel))
    jungle = list(set(jungle) - set(winkel))
    woestijn = list(set(woestijn) - set(winkel))
    gletsjer = list(set(gletsjer) - set(winkel))

    #tunnel
    tunnels = random.sample(land,2)
    tunnels += random.sample(rivier,2)
    tunnels += random.sample(jungle,2)
    tunnels += random.sample(woestijn,2)
    tunnels += random.sample(gletsjer,2)
    tunnels.sort()

    # dubbele voorkomen 
    land = list(set(land) - set(tunnels))
    rivier = list(set(rivier) - set(tunnels))
    jungle = list(set(jungle) - set(tunnels))
    woestijn = list(set(woestijn) - set(tunnels))
    gletsjer = list(set(gletsjer) - set(tunnels))

    #geluksvogel
    vogels = random.sample(land,2)
    vogels += random.sample(rivier,2)
    vogels += random.sample(jungle,3)
    vogels += random.sample(woestijn,1)
    vogels += random.sample(gletsjer,2)
    vogels.sort()

    # dubbele voorkomen 
    land = list(set(land) - set(vogels))
    rivier = list(set(rivier) - set(vogels))
    jungle = list(set(jungle) - set(vogels))
    woestijn = list(set(woestijn) - set(vogels))
    gletsjer = list(set(gletsjer) - set(vogels))

    # event vak
    events = random.sample(land,2)
    events += random.sample(rivier,2)
    events += random.sample(jungle,2)
    events += random.sample(woestijn,2)
    events += random.sample(gletsjer,2)
    events.sort()
    
def opstellingMenu():
    '''keuze opstelling'''
    #menu keuzes
    setBackground()
    fill(255)
    rect(width / 4 - 300, height / 2 - 100, 400, 100, 50)
    rect(width / 4 - 300, height / 2 + 100, 400, 100, 50)
    fill(0)
    textAlign(CENTER)
    textSize(40)
    text('Standaard', width / 5, height / 2 - 35)
    text('Randomized', width / 5, height / 2 + 165)
    
    #terug knop
    fill(255, 0, 0)
    rect(20, height - 100, 200, 75, 50)
    textAlign(CENTER)
    textSize(30)
    fill(0)
    text('Terug', 120, height - 50)
    
def printData():
    '''opstelling tonen'''
    global valkuilen, winkel, tunnels, vogels, events, toeristenWinkel
    setBackground()
    fill(255)
    rect(340,380,1190,350)
    #terug knop
    fill(255, 0, 0)
    rect(20, height - 100, 200, 75, 50)
    textAlign(CENTER)
    textSize(30)
    fill(0)
    text('Terug', 120, height - 50)
    #data van de speciale vakken
    fill(255)
    fill(0)
    textSize(25)
    textAlign(LEFT)
    text('valkuilen: ',450,455)
    text( ', '.join(map(str, valkuilen)),660,455)
    text('winkels: ',450,495)
    text( ', '.join(map(str, winkel)),660,495)
    text('tunnels: ',450,535)
    text( ', '.join(map(str, tunnels)),660,535)
    text('geluksvolgels: ',450,575)
    text( ', '.join(map(str, vogels)),660,575)
    text('events: ',450,615)
    text( ', '.join(map(str, events)),660,615)
    text('toeristenwinkel: ',450,655)
    text( ', '.join(map(str, toeristenWinkel)),660,655)
    
def mouseJan():
    '''all mouse functionality for jan'''
    global opstelling, showOpstelling, menu, jan, nathan
    if opstelling:
        if width / 4 - 300 < mouseX < width / 4 + 300 and height / 2 - 100 < mouseY < height / 2:
            standaard()
            opstelling = False
            showOpstelling = True
        if width / 4 - 300 < mouseX < width / 4 + 300 and height / 2 + 100 < mouseY < height / 2 + 200:
            generate()
            opstelling = False
            showOpstelling = True
        if 20 < mouseX < 220 and height - 100 < mouseY < height - 25:
            opstelling = False
            menu = True
            jan = False
            nathan = True
    elif showOpstelling:
        if 20 < mouseX < 220 and height - 100 < mouseY < height - 25:
            opstelling = True
            showOpstelling = False
    
#main game || screen calling || button functionality
def allScreens():
    '''all our screens calling will happen here'''
    global nathan, titel, menu, jan, opstelling, toonData
    if nathan:
        if titel:
            title()
        elif menu:
            meNu()
    elif jan:
        if opstelling:
            opstellingMenu()
        elif showOpstelling:
            printData()
        
def allMouseAreas():
    '''this is the collective function where the buttons getfunctionality'''
    global nathan, jan
    if nathan:
        mouseNathan()
    elif jan:
        mouseJan()
