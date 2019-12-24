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
steven = False

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

#Steven globals

'''player select screen'''
amountPlayers = 0

'''name select screen''' 
#usernames = []
currentname = ''
nameholder = '__________'
currentplayername = 1

'''game screen'''
diceImages = []
start = 0
runTime = 0
#turn = 0
rolled = False
paytext = False
numberrolled = 3

#screen booleans
playerselect = False
nameselect = False 
gamescreen = False

#button booleans
namecomplete = False
playercomplete = False

#Nathan Samijo #Nathan Samijo
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
        background(backgrounds[0])
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
    global titel, menu, opstelling, nathan, jan, steven, playerselect
    if titel:
        menu = True
        titel = False
    elif menu:
        if width / 2 - 300 < mouseX < width / 2 + 300 and height / 2 + 100 < mouseY <  height / 2 + 200:
            menu = False
            opstelling = True
            nathan = False
            jan = True
        if width/2 - 300 < mouseX < width / 2 + 300 and height / 2 - 100 < mouseY < height /2 + 200:
            menu = False
            nathan = False
            steven = True
            playerselect = True
        
        
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
            
#Steven Ren

#voor dice animation
def check():
    '''Current framecount word start frameCount'''
    global runTime, start
    start = frameCount 
    
#load de dice images in
def stevenSetup():
    '''load dice images in'''
    global diceImages
    for x in range(6):
        diceImages.append(loadImage('dice' + str(x+1) + '.png'))
    for x in diceImages:
        x.resize(150, 150)     
 
#voor de dice animatie
def rollingDice():
    '''random dice'''
    global diceImages
    image(diceImages[random.randint(0,5)], 1230,310)
   
   
#voor de random dicenumber 
def randomizer():
    '''for random dicenumber'''
    dicenumbers = ['1','2','3','4','5','6']
    dicerolled = dicenumbers[random.randint(0,len(dicenumbers)-1)]
    return dicerolled

#voor invoer van namen: limiet van karakters voor namen = 10 / backspace om 1 karakter te deleten
def keySteven():
    '''naam invoer functie'''
    global currentname, nameselect,currentplayername,amountPlayers,namecomplete,nameholder
    if nameselect:
        if namecomplete == False:#wanneer alle namen zijn ingetikt, kan je ook niet meer tikken
            if key != CODED and key != ENTER and len(currentname)<10 and key != BACKSPACE:
                currentname = currentname + key
                nameholder = nameholder[:-1]
            if key == BACKSPACE and len(nameholder)<10:
                currentname = currentname[:-1]
                nameholder = nameholder + '_'
            if key == ENTER and currentplayername-1<amountPlayers and currentname!='':
                usernames.append(currentname)
                currentname = currentname[:len(currentname)-len(currentname)]
                nameholder = '__________'
                currentplayername+=1 
                if currentplayername-1 == amountPlayers: #als limiet bereikt is, dan is de button om naar scherm 3 te gaan tevoorschijn gekomen
                    namecomplete = True
                    
#indicator for how many players have been selected
def drawamountPlayers():
    '''Indicated which option form the player has been selected'''
    fill(0,220,0)
    options = [760, 910, 1060]
    x = options[amountPlayers - 2]
    rect(x, 400, x + 100, 500,50)
    fill(0)
    text(str(amountPlayers), x + 40, 463)
    
#kleur voor of iemand aan de beurt is of niet
def drawturn():
    '''Color indication if it's your turn or not'''
    global turn, usernames, rolled
    if rolled == False:
        def drawt1():
            fill(0,200,0)
            rect(210,310,490,410) 
            fill(0)
            textSize(25)
            text(usernames[0],350,365)
        def drawt2():
            fill(0,200,0)
            rect(210,420,490,520)
            fill(0)
            textSize(25)
            text(usernames[1],350,475)
        def drawt3():
            fill(0,200,0)
            rect(210,530,490,630)
            fill(0)
            textSize(25)
            text(usernames[2],350,585)
        def drawt4():
            fill(0,200,0)
            rect(210,640,490,740)
            fill(0)
            textSize(25)
            text(usernames[3],350,695)
            
    if rolled == True:
        def drawt1():
            fill(200,0,0)
            rect(210,310,490,410) 
            fill(0)
            textSize(25)
            text(usernames[0],350,365)
        def drawt2():
            fill(200,0,0)
            rect(210,420,490,520)
            fill(0)
            textSize(25)
            text(usernames[1],350,475)
        def drawt3():
            fill(200,0,0)
            rect(210,530,490,630)
            fill(0)
            textSize(25)
            text(usernames[2],350,585)
        def drawt4():
            fill(200,0,0)
            rect(210,640,490,740)
            fill(0)
            textSize(25)
            text(usernames[3],350,695)
            
    drawFunctions = [drawt1, drawt2, drawt3, drawt4] #de drawfunctions in een list
    function = drawFunctions[turn] # function = list index aanvragen waardoor die function word opgeroepen
    function() #roept function aan
    fill(0)
    textAlign(LEFT)
    textSize(40)
    text(usernames[turn], 1450, 250) #toont aan bij beurt van (naam)
    
#knoppen voor playerselect,nameselect en gamescreen scherm
def mouseSteven():
    '''mouse functionality for all screens'''
    global playerselect, amountPlayers, playercomplete, nameselect, namecomplete, nameholder, usernames, currentplayername, currentname, gamescreen, rolled, turn, paytext, numberrolled, menu, nathan
    #playerselect scherm buttons, nameselect scherm buttons en gamescreen scherm buttons
    if playerselect:
        if 760 < mouseX < 860 and 400 < mouseY < 500:
            fill(0)
            rect(760,400,860,500,50)
            amountPlayers=2
            playercomplete = True
        elif 910 < mouseX < 1010 and 400 < mouseY < 500:
            fill(0)
            rect(910,400,1010,500,50)
            amountPlayers=3
            playercomplete = True
        elif 1060 < mouseX < 1160 and 400 < mouseY < 500:
            fill(0)
            rect(1060,400,1160,500,50)
            amountPlayers=4
            playercomplete = True
        elif 0 < mouseX < 150 and 980 < mouseY < 1080:
            fill(0)    
            rect(0,980,150,1080,50)
            playerselect = False
            menu = True
            steven = False
            nathan = True
            amountPlayers = 0
            playercomplete = False
        elif playercomplete:
            if 1720 < mouseX < 1920 and 980 < mouseY < 1080:
                fill(0)
                rect(1720,980,1920,1080,50)
                nameselect = True
                playerselect = False
    if nameselect:
        if 610 < mouseX < 760 and 680 < mouseY < 740:#button om een speler naam te adden
            if namecomplete == False:
                fill(0)
                rect(610,680,760,740)
            if currentplayername-1<amountPlayers and currentname!= '':#checkt of je naam niet blank is en het checkt of het limiet voor namen al bereikt is
                usernames.append(currentname) 
                currentname = currentname[:len(currentname)-len(currentname)]
                currentplayername+=1 
                nameholder = '__________'
            if currentplayername-1 == amountPlayers: #als limiet bereikt is, dan is de button om naar scherm 3 te gaan tevoorschijn gekomen
                namecomplete = True
        if 200 < mouseX < 500 and 760 < mouseY < 860:#terug button
            fill(0)
            rect(200,760,500,860,50)
            currentname = ''
            currentplayername = 1
            usernames = []
            nameselect = False
            playerselect = True
            amountPlayers = 0
            playercomplete = False
            namecomplete = False
        if 1240 < mouseX < 1390 and 680 < mouseY < 740:
            fill(0)
            rect(1240,680,1390,740)
            nameselect = False
            gamescreen = True
    if gamescreen:
        if paytext==False:
            if 1640 < mouseX < 1790 and 640 < mouseY < 740 and rolled == True:#button om naar volgende beurt te gaan
                fill(0) 
                rect(1640,640,1790,740)
                if turn<amountPlayers-1:
                    turn = turn + 1
                    paytext=False
                elif turn == amountPlayers-1:
                    turn = turn - (amountPlayers-1)
                    paytext=True
                rolled = False
            if 1530 < mouseX < 1630 and 640 < mouseY < 740 and rolled == False:#button om te rollen
                rolled = True
                numberrolled = randomizer()
                check() 
                fill(0)
                rect(1530,640,1630,740)
        else:
            if 900 < mouseX < 1100 and 570 < mouseY < 670:
                paytext = False

def playerselect1():
    '''Player select screen'''
    setBackground()
    rectMode(CORNERS)
    
    #player option rectangles 2,3,4 -------------------------------------------------
    fill(255)
    for x in [760, 910, 1060]:
        rect(x, 400, x + 100, 500,50)
    
    #Terug,Kies het aantal spelers, Volgende RECT in die order  -------------------------------------------
    fill(200,0,0)
    rect(0,980,150,1080,50)
    fill(200,200,0)
    rect(760,250,1160,350) 
    if playercomplete:
        fill(0,200,0)
        rect(1720,980,1920,1080,50) 
        drawamountPlayers()

    #text for player select screen -------------------------------------------------------
    fill(0)
    textAlign(LEFT) 
    textSize(20)
    text('Kies het aantal spelers',850,305)
    text('Terug',50,1035)
    if playercomplete:
        text('Volgende',1780,1035) 
        
    #options text 2,3,4 ---------------------------------------------------------
    textSize(40)
    y = 800
    for x in ['2','3','4']:
        text(x,y,463)
        y += 150
    
    #laat zien wanneer je muis over een button is -------------------------------------------------
    if 760 < mouseX < 860 and 400 < mouseY < 500:
        fill(0,255,0)
        rect(760,400,860,500,50)
        fill(0)
        text('2',800,463)
    elif 910 < mouseX < 1010 and 400 < mouseY < 500:
        fill(0,255,0)
        rect(910,400,1010,500,50)
        fill(0)
        text('3',950,463)
    elif 1060 < mouseX < 1160 and 400 < mouseY < 500:
        fill(0,255,0)
        rect(1060,400,1160,500,50)
        fill(0)
        text('4',1100,463)
    elif 0 < mouseX < 150 and 980 < mouseY < 1080:
        fill(200)
        rect(0,980,150,1080,50)
        fill(0)
        textSize(20)
        text('Terug',50,1035)
        textSize(40)
    if playercomplete:
        if 1720 < mouseX < 1980 and 980 < mouseY < 1080:
            fill(200)
            rect(1720,980,1920,1080,50)
            fill(0)
            textSize(20)
            text('Volgende',1780,1035)
            textSize(40)
        
def nameselect1():
    '''Name select screen'''
    global namecomplete, usernames
    setBackground()
    rectMode(CORNERS)
    textAlign(CENTER)
    
    #PLAYERS RECT, ONDER PLAYERS RECT ----------------------------------------------------
    fill(255)
    rect(200,190,500,290) 
    fill(0)
    rect(200,300,500,750) 
    
    #TYPE SPELER NAAM RECT, INVOER VAN JE KEYTYPE RECT -----------------------------------------------
    fill(255)
    rect(600,190,1400,290) 
    rect(600,300,1400,750) 
    
    #RETURN TO PLAYER SELECT RECT, START RECT, TOEVOEGEN RECT EN NAAM INVOER RECT IN DIE ORDER! ---------------------------------------------------
    rect(200,760,500,860,50)
    if namecomplete:
        rect(1240,680,1390,740) 
    else:
        rect(610,680,760,740)
        fill(225,225,0)
        rect(800,475,1200,550)
                
    #rect voor amountPlayers ---------------------------------------------------------
    startY = 310
    startHeight = 410
    for x in range(amountPlayers):
        fill(255)
        rect(210, startY, 490, startHeight)
        startY += 110
        startHeight += 110
    
    #text for name select screen ----------------------------------------
    fill(0)            
    textSize(40)
    text(currentname,1000,525)
    noFill()
    textSize(40) 
    text('Spelers',350,250)
    text('Terug',350,820) 
    textSize(20)
    fill(0)
    if namecomplete:
        textSize(40)
        text('Compleet',1000,250)
        text('Druk nu op start om het spel te starten',1000,415)
        textSize(20)
        text('Start',1315,715)
            
    else:
        textSize(40) 
        text('Type hier je naam',1000,415)
        text('Druk daarna op toevoegen',1000,625)
        textSize(20)
        text('Toevoegen',685,715)
        textSize(40)
        text('Naam voor speler',1000,250)
        text(currentplayername,1190,250)
        text(nameholder,1000,527)
        
    #functie om namen van de spelers te laten zien in rect en ook de rects groen maken  -------------------------------------------------
    if len(usernames) > 0:
        textSize(25)
        startY = 365
        startY2 = 310
        startHeight = 410
        for x in usernames:
            fill(0,150,0)
            rect(210, startY2, 490, startHeight)
            startY2 += 110
            startHeight += 110
            fill(0)
            text(x, 350, startY)
            startY += 110
        
    #kleur indicatie wanneer iets ready is / button, toevoegen en start-----------------------------------------------------------
    if currentname!= '' and namecomplete == False:
        fill(0,200,0)
        rect(610,680,760,740)
        fill(0)
        textSize(20)
        text('Toevoegen',685,715)
    if namecomplete:
        fill(0,200,0)
        rect(1240,680,1390,740)
        fill(0)
        textSize(20)
        text('Start',1315,715)
        
    #laat zien wanneer je muis over een button is, toevoegen, terug en start------------------------------------------------
    if 610 < mouseX < 760 and 680 < mouseY < 740:
        if namecomplete == False:
            fill(200)
            rect(610,680,760,740)
            fill(0)
            textSize(20)
            text('Toevoegen',685,715)
    if 200 < mouseX < 500 and 760 < mouseY < 860:
        fill(200)
        rect(200,760,500,860,50) 
        fill(0)
        textSize(40)
        text('Terug',350,820)
    if 1240 < mouseX < 1390 and 680 < mouseY < 740:
        if namecomplete:
            fill(200)
            rect(1240,680,1390,740)
            fill(0)
            textSize(20) 
            text('Start',1315,715)
            
def gamescreen1():
    '''game screen'''
    global amountPlayers, usernames, numberrolled, paytext
    setBackground() 
    rectMode(CORNERS)
    textAlign(CENTER)
    rollthedice = loadImage('rollthedice.png')
    rollthedice.resize(99,99)
    
    #PLAYERS RECT, ONDER PLAYERS RECT en text bij de rect van players ----------------------------------------------------
    fill(255)
    rect(200,190,500,290) 
    fill(0)
    rect(200,300,500,750) 
    textSize(25)
    startY = 365
    startY2 = 310
    startHeight = 410
    for x in usernames:
        fill(255)
        rect(210, startY2, 490, startHeight)
        startY2 += 110
        startHeight += 110
        fill(0)
        textSize(25)
        text(x, 350, startY)
        startY += 110
    
    #rect waar posities informatie komt en rect waar positie staat ---------------------------------------------------
    fill(255)
    rect(510,300,1210,750)
    rect(510,190,1210,290)
    
    #beurt van rect en onder beurt van rect -------------------------------------------------
    rect(1220,190,1800,290)
    rect(1220,300,1800,750)
    
    #volgende knop rect ------------------------------------------------------------
    fill(200,0,0)
    rect(1640,640,1790,740) 
    
    #vak waar dobbelsteen in zit en de nummer/ niet de dobbelsteen knop ------------------------------------------------------
    fill(255)
    rect(1230,310,1380,460)
    rect(1390,310,1540,460)
    
    #text for game screen -------------------------------------------------------------
    textAlign(CENTER)
    fill(0)
    textSize(20) 
    text('Volgende beurt', 1715,694) 
    textSize(40)
    text('Spelers',350,250)
    text('Positie',860,250)
    text('Beurt van',1350,250)
    
    #shows whose turn it is ---------------------------------------------------------
    drawturn()

    
    #runtime = framecount die constant doorgaat (wanneer start de huidige framecount word gereset alles als het ware -----------------------------------------------
    runTime = frameCount - start 
    
    #wanneer framecount reset door de button te klikken laat dit de soort van animatie zien van dobbelsteen -------------------------------------------------------
    if runTime < 40: 
        rollingDice()
        
    #om te zien welke nummer je heb gerollt ------------------------------------------------------------
    else:
        for x in [1,2,3,4,5,6]:
            if x == int(numberrolled):
                image(diceImages[x-1],1230,310)
        if rolled == True:
            textSize(90)
            textAlign(CENTER)
            text(numberrolled,1465,414) 
            
    #als er al gerollt is dan wordt volgende beurt knop groen ----------------------------------------------------
    if rolled:
        fill(0,200,0)
        rect(1640,640,1790,740)
        fill(0)
        textSize(20)
        textAlign(CENTER)
        text('Volgende beurt', 1715,694)
        
    #als er nog niet gerollt is -------------------------------------------------
    else:
        rect(1530,640,1630,740) #rollen knop
        image(rollthedice,1531,641) 
        
    #als iedereen is geweest
    if paytext:
        fill(255)
        rect(200,190,1800,750)
        rect(900,570,1100,670)
        fill(0)
        textAlign(CENTER)
        textSize(50)
        text('Deel nu geld uit!',1000,470)
        textSize(25)
        text('Gedaan',1000,625)
        if 900 < mouseX < 1100 and 570 < mouseY < 670:
            fill(200)
            rect(900,570,1100,670)
            fill(0)
            textSize(25)
            text('Gedaan',1000,625)
        
    else:    
        #laat zien wanneer je muis over een button is -------------------------------------------------
        if 1640 < mouseX < 1790 and 640 < mouseY < 740 and rolled == True:#button om naar volgende beurt te gaan
            fill(200)
            rect(1640,640,1790,740)
            fill(0)
            textSize(20)
            textAlign(CENTER)
            text('Volgende beurt', 1715,694)
        if 1530 < mouseX < 1630 and 640 < mouseY < 740 and rolled == False:#button om te rollen
            tint(200)
            image(rollthedice,1531,641)  
            noTint()
        else:
            noTint()
    
#main game || screen calling || button functionality
def allScreens():
    '''all our screens calling will happen here'''
    global nathan, titel, menu, jan, opstelling, toonData, steven, playerselect,nameselect,gamescreen
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
    elif steven:
        if playerselect:
            playerselect1()
        elif nameselect:
            nameselect1()
        elif gamescreen:
            gamescreen1()
        
def allMouseAreas():
    '''this is the collective function where the buttons getfunctionality'''
    global nathan, jan, steven
    if nathan:
        mouseNathan()
    elif jan:
        mouseJan()
    elif steven:
        mouseSteven()
        
def allKeyAreas():
    global steven, nameselect
    if steven:
        if nameselect:
            keySteven()
