# Project A
# Groep 4
# Authors:
# - Nathan Samijo
# - Steven Ren
# - Audrius Paulaitis
# - Jan Roozemond

import groep4

def setup():
    fullScreen()
    groep4.nathanSetup()
    groep4.stevenSetup()
    
def draw():
    groep4.allScreens()
    
def mousePressed():
    groep4.allMouseAreas()
    
def keyTyped():
    groep4.allKeyAreas()
