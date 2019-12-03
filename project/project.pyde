add_library('minim')
import nathan
import steven

music = 'suspense.mp3'

title = True
menu = False
game = False
opstelling = False

def setup():
    global music, position
    fullScreen()
    nathan.setup()
    steven.setup()
    minim = Minim(this)
    path = sketchPath(music)
    player = minim.loadFile(path, 2048)
    player.loop()
    
def draw():
    if title:
        if nathan.getHeight():
            nathan.title()
        else:
            nathan.titleText()
    if menu:
        nathan.setBackground()
        nathan.menu()
    if game:
        steven.game()
            
def keyTyped():
    steven.name()
            
def setFrame(tit, gam, opst, men):
    global title, game, opstelling, menu
    title = tit
    game = gam
    opstelling = opst
    menu = men
            
def mousePressed():
    global title, game, menu
    if title:
        title = False
        menu = True
    elif not title and menu:
        if (width / 2 - 300 < mouseX < width / 2 + 300):
            if(height / 2 - 100 < mouseY < height / 2):
                setFrame(False, True, False, False)
            elif(height / 2 + 100 < mouseY < height / 2 + 200):
                setFrame(False, False, True, False)
    elif game:
        steven.mouseGame()
        
