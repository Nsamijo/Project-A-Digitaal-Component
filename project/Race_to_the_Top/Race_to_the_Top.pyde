add_library('minim')
# Project A
# Groep 4
# Authors:
# - Nathan Samijo
# - Steven Ren
# - Audrius Paulaitis
# - Jan Roozemond

import groep4
play = None


def setup():
    global play
    fullScreen()
    minim = Minim(this)
    play = minim.loadFile( 'suspense.mp3', 2048 )
    play.loop()
    groep4.nathanSetup()
    groep4.stevenSetup()
    
def draw():
    groep4.allScreens()
    
def mousePressed():
    groep4.allMouseAreas()
    
def keyTyped():
    groep4.allKeyAreas()
