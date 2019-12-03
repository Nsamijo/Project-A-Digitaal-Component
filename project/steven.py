#geeft kleur aan spelers kiezen aantal en beurten indicator
import nathan
import random
players = []

def drawTurn():
    '''indicate which option has been selected'''
    global number1, number2, number3, number4
        
    def draw2():
        fill(0,220,0)
        rect(950,400,1050,500)
        fill(0) 
        text('2',990,463)
        
    def draw3():
        fill(0,220,0)
        rect(1100,400,1200,500) 
        fill(0) 
        text('3',1140,463)
    
    def draw4():
        fill(0,220,0) 
        rect(1250,400,1350,500) 
        fill(0) 
        text('4',1290,463)
    
    if number2:
        draw2()
    if number3:
        draw3()
    if number4:
        draw4()

def drawCurrentTurn():
    '''show whose turn it is with name and color indication'''
    global turn, players,playername1,playername2,playername3,playername4
    
    def drawt1():
        fill(0,200,0)
        rect(210,310,490,410) 
        fill(0)
        textSize(25)
        text(playername1,350,360)
    def drawt2():
        fill(0,200,0)
        rect(210,420,490,520)
        fill(0)
        textSize(25)
        text(playername2,350,470)
    def drawt3():
        fill(0,200,0)
        rect(210,530,490,630)
        fill(0)
        textSize(25)
        text(playername3,350,580)
    def drawt4():
        fill(0,200,0)
        rect(210,640,490,740)
        fill(0)
        textSize(25)
        text(playername4,350,690)
        
    drawFunctions = [drawt1, drawt2, drawt3, drawt4] #de drawfunctions in een list
    function = drawFunctions[turn - 1] # function = list index aanvragen waardoor die function word opgeroepen
    function() #roept function aan
    fill(0)
    textAlign(LEFT)
    textSize(40)
    text(players[turn - 1], 1105, 250) 

def name(): #voor invoer van namen: limiet van karakters voor namen = 15 / backspace om 1 karakter te deleten
    global currentname, startgame
    if startgame:
        if namecomplete == False:#wanneer alle namen zijn ingetikt, kan je ook niet meer tikken
            if key != CODED and key!= ENTER and len(currentname)<15:
                currentname = currentname + key
            if key == BACKSPACE:
                currentname = currentname[:len(currentname)-2]
            

def mouseGame():
    global number1,number2,number3,number4,startgame,amountofplayers,currentname,players,currentplayername,playeramount2,namecomplete,playername1,playername2,playername3,playername4,endgame,turn,paytext
    if endgame: #alle buttons hieronder gelden voor scherm 3/dit is als alle spelers een naam hebben
        if 1440 < mouseX < 1590 and 640 < mouseY < 740:#button om naar volgende beurt te gaan
            fill(0) 
            rect(1440,640,1590,740)
            if turn<playeramount:
                turn = turn + 1
                paytext=False
            elif turn == playeramount:
                turn = turn+1 - playeramount
                paytext=True
    else:
        if startgame: #voor als spelers zijn gekozen, deze buttons gelden voor scherm 2
            if 200 < mouseX < 500 and 760< mouseY < 860: #button om terug naar scherm 1 te gaan / scherm om aantal spelers te kiezen
                fill(0)
                rect(200,760,500,860) 
                startgame = False
                currentname = currentname[:len(currentname)-len(currentname)]
                number1 = False
                number2 = False
                number3 = False
                number4 = False
                textAlign(BASELINE)
                namecomplete = False
                players = []
                amountofplayers = 0
                playeramount2 = 0
                currentplayername =1
                playername1 = ''
                playername2 = ''
                playername3 = ''
                playername4 = ''
            if 610 < mouseX < 760 and 680 < mouseY < 740:#button om een speler naam te adden
                fill(0)
                rect(610,680,760,740)
                if playeramount2<amountofplayers and currentname!= '':#checkt of je naam niet blank is en het checkt of het limiet voor namen al bereikt is
                    players.append(currentname) 
                    currentname = currentname[:len(currentname)-len(currentname)]
                    playeramount2+=1
                    currentplayername+=1 
                if currentplayername-1 == amountofplayers: #als limiet bereikt is, dan is de button om naar scherm 3 te gaan tevoorschijn gekomen
                    namecomplete = True
            if 1240 < mouseX < 1390 and 680 < mouseY <740:#als alle spelers een naam hebben, buttom om naar volgende scherm te gaan scherm 3
                if namecomplete == True:
                    fill(0)
                    rect(1240,680,1390,740)
                    endgame = True
                    currentplayername = 1
                    turn = 1
                    nathan.getPositions(players)
        else: # voor als spelers nog niet zijn gekozen, deze buttons gelden voor scherm 1
            if 950 < mouseX < 1050 and 400 < mouseY < 500: #Kies 2 spelers
                fill(0)
                rect(950,400,1050,500)
                number1 = False
                number2 = True
                number3 = False
                number4 = False
                amountofplayers = 2 
            if 1100 < mouseX < 1200 and 400 < mouseY < 500: #Kies 3 spelers
                fill(0)
                rect(1100,400,1200,500)
                number1 = False
                number2 = False
                number3 = True
                number4 = False
                amountofplayers = 3
            if 1250 < mouseX < 1350 and 400 < mouseY < 500: #Kies 4 spelers
                fill(0)
                rect(1250,400,1350,500) 
                number1 = False
                number2 = False
                number3 = False
                number4 = True 
                amountofplayers = 4
            if 1400 < mouseX < 1600 and 400 < mouseY < 500: #Druk op de start button om naar scherm 2 te gaan
                if number1 == True or number2 == True or number3 == True or number4 == True:#checkt of 1 van de opties wel gekozen is of niet
                    fill(0)
                    rect(1400,400,1600,500) 
                    startgame = True

                
def setup():
    global currentname,font,amountofplayers,number1,number2,number3,number4,startgame,playeramount,currentplayername,addplayer,players,playeramount2,namecomplete,playername1,playername2,playername3,playername4,endgame,turn,paytext,blackarrow
    nathan.setup()
    font = createFont('Arial',20,True)
    blackarrow = loadImage('blackarrow.png')
    blackarrow.resize(100,100)
    amountofplayers = 0
    playeramount2 = 0
    playeramount = 0
    currentname = ''
    number1 = False
    number2 = False
    number3 = False
    number4 = False
    startgame = False
    currentplayername = 1
    namecomplete = False
    playername1 = ''
    playername2 = ''
    playername3 = ''
    playername4 = ''
    endgame = False
    turn = 0
    paytext=False
    

def game():
    global currentname,font,amountofplayers,playeramount,currentplayername,players,playeramount2,namecomplete,playername1,playername2,playername3,playername4,endgame,turn,paytext,blackarrow
    if endgame == False:#om te zorgen dat scherm 3 nog niet active is
        if startgame == False:
            #scherm 2 is nog niet active hieronder is scherm 1 active
            nathan.setBackground()
            textFont(font)
            
            rectMode(CORNERS)
            fill(255)
            #rect(800,400,900,500)
            rect(950,400,1050,500)
            rect(1100,400,1200,500)
            rect(1250,400,1350,500) 
            rect(1400,400,1600,500)
            rect(450,400,750,500)
            
            fill(0)
            textAlign(LEFT)
            text('Kies het aantal spelers',500,455)
            text('Volgende',1460,455)
            textSize(40)
            #text('1',840,463)
            text('2',990,463)
            text('3',1140,463)
            text('4',1290,463)
            
            #kleur van wie aan de beurt is
            drawTurn()
                
        if startgame: 
            #scherm 2 is nu active
            nathan.setBackground()
            textAlign(CENTER)
            playeramount = amountofplayers
            
            fill(255)
            rect(200,190,500,290) #players
            noFill()
            rect(200,300,500,750) #onder players cover
            fill(255)
            rect(600,190,1400,290) #type speler naam cover 
            rect(600,300,1400,750) #naast players cover rechts / onder type speler naam
            rect(610,680,760,740) #toevoegen 
            rect(200,760,500,860) #return to player select
            
            fill(0)
            textSize(40)
            text(currentname,1000,300+450/2)
            noFill()
            textSize(40) 
            text('Spelers',350,250)
            text('Terug',350,820) 
            textSize(20)
            text('Toevoegen',685,715)
            if namecomplete == False and frameCount%20==0: #voor blinking arrow
                image(blackarrow,950,365) 
                
            if namecomplete==True:
                rect(1240,680,1390,740)
                fill(0)
                text('Start',1315,715)
                noFill() 
                
            #return to playerselect
            #up above, panels
            #rect(210,310,490,410) 
            #rect(210,420,490,520) 
            #rect(210,530,490,630) 
            #rect(210,640,490,740) 

            #draw rectagles base on amount of layers
            startY = 310
            startHeight = 410
            for x in range(playeramount):
                fill(255)
                rect(210, startY, 490, startHeight)
                startY += 110
                startHeight += 110
            fill(0)
                
            if namecomplete:
                #als alle namen zijn ingevuld
                textSize(40)
                text('Compleet',1000,250)
            else:
                #als nog niet alle namen zijn ingevuld
                textSize(40) 
                text('Type de naam van speler',1000,250)
                text(currentplayername,1250,250)
                
            if len(players) != 0:#functie om namen te adden aan de spelers
                if playeramount==1:
                    playername1 = players[0]
                if playeramount==2:
                    playername1 = players[0]
                    if len(players) != 1:
                        playername2 = players[1] 
                if playeramount==3:
                    playername1 = players[0]
                    if len(players) !=1:
                        playername2 = players[1]
                        if len(players) !=2:
                            playername3 = players[2]
                if playeramount==4:
                    playername1 = players[0]
                    if len(players) != 1:
                        playername2 = players[1]
                        if len(players) != 2:
                            playername3 = players[2] 
                            if len(players) !=3:
                                playername4 = players[3] 
            textSize(25)
            text(playername1,350,360)
            text(playername2,350,470)
            text(playername3,350,580)
            text(playername4,350,690)
            
    if endgame == True:#scherm 3 is nu active
        nathan.setBackground()
        
        fill(255)
        rect(200,190,500,290) #players
        noFill()
        rect(200,300,500,750) #onder players cover
        fill(255)
        rect(510,300,810,750) #naast players cover
        rect(510,190,810,290) #naast players
        rect(820,190,1600,290) #het is player turn cover
        rect(820,300,1600,750) #onder het is player turn
        rect(1440,640,1590,740) #volgende knop
        rect(510,80,1600,180) #laatste beurt is geweest cover
        
        fill(0)
        textAlign(CENTER)
        textSize(25)
        text(playername1,350,360)
        text(playername2,350,470)
        text(playername3,350,580)
        text(playername4,350,690)
        textSize(20) 
        text('Volgende beurt', 1515,694) 
        textSize(40)
        text('Spelers',350,250)
        text('Info',660,250)
        #show position
        displayStats(turn)
        text('Beurt van',1010,250)
        #textAlign(LEFT)
        #text(players[0],1105,250) 
        noFill()
        
        if paytext:
            text('Laatste beurt is geweest deel nu geld uit',1055,140)
            
        #shows the amount of players chosen
        startY = 310
        startY2 = 410
        for x in range(playeramount):
            rect(210, startY, 490, startY2)
            startY += 110
            startY2 += 110
        
        #current turn
        drawCurrentTurn()
        
def displayStats(player, throw=0):
    '''display the stats of the player: nathan'''
    con = nathan.getDebuff(player, throw)
    pos = nathan.getPosition(player)
    lvl = nathan.getLevel(player)
    textAlign(LEFT)
    text('Level: ' + lvl, 520, 350)
    text('Positie: ' + pos, 520, 400)
    text('Condition: ', 520, 450)
    text
    textAlign(CENTER)
