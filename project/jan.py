import nathan
import random

randomized = False
opzet = None

def standaard():
    #valkuilen
    x = [4, 10, 18, 26, 28, 33, 38, 45, 48, 56, 62, 67, 70, 75, 78, 88, 90, 95]
    #winkel
    s = [11, 19, 23, 31, 53, 64, 72, 77, 89, 96]
    #tunnels
    t = [12, 16, 29, 36, 51, 54, 68, 73]
    #geluksvogels
    v = [5, 13, 17, 27, 37, 52, 63, 76, 83, 91]
    #events
    e = [8, 15, 25, 34, 47, 55, 65, 74, 86, 92]
    #toeristenwinkels
    w = [21, 41, 61, 81]    

    return x,s,t,v,e,w

def generate():
    global opzet
    Randomized = True
    
    #vakken waar pionnen in geplaatst mogen worden, alle vakken min de stop en overgang vakken.
    land = range(4,19)
    rivier = range(22,39)
    jungle = range(42, 59)
    woestijn = range(62,79)
    gletsjer = range(82,99)


    # willekeurige plaatsing door random method
    # valkuilen
    x = random.sample(land,2)
    x += random.sample(rivier,3)
    x += random.sample(jungle,5)
    x += random.sample(woestijn,5)
    x += random.sample(gletsjer,3)
    x.sort()

    # dubbele voorkomen
    land = list(set(land) - set(x))
    rivier = list(set(rivier) - set(x))
    jungle = list(set(jungle) - set(x))
    woestijn = list(set(woestijn) - set(x))
    gletsjer = list(set(gletsjer) - set(x))

    #winkel
    s = random.sample(land,2)
    s += random.sample(rivier,2)
    s += random.sample(jungle,3)
    s += random.sample(woestijn,2)
    s += random.sample(gletsjer,1)
    s.sort()

    # dubbele voorkomen 
    land = list(set(land) - set(s))
    rivier = list(set(rivier) - set(s))
    jungle = list(set(jungle) - set(s))
    woestijn = list(set(woestijn) - set(s))
    gletsjer = list(set(gletsjer) - set(s))

    #tunnel
    t = random.sample(land,2)
    t += random.sample(rivier,2)
    t += random.sample(jungle,2)
    t += random.sample(woestijn,2)
    t += random.sample(gletsjer,2)
    t.sort()

    # dubbele voorkomen 
    land = list(set(land) - set(t))
    rivier = list(set(rivier) - set(t))
    jungle = list(set(jungle) - set(t))
    woestijn = list(set(woestijn) - set(t))
    gletsjer = list(set(gletsjer) - set(t))

    #geluksvogel
    v = random.sample(land,2)
    v += random.sample(rivier,2)
    v += random.sample(jungle,3)
    v += random.sample(woestijn,1)
    v += random.sample(gletsjer,2)
    v.sort()

    # dubbele voorkomen 
    land = list(set(land) - set(v))
    rivier = list(set(rivier) - set(v))
    jungle = list(set(jungle) - set(v))
    woestijn = list(set(woestijn) - set(v))
    gletsjer = list(set(gletsjer) - set(v))

    # event vak
    e = random.sample(land,2)
    e += random.sample(rivier,2)
    e += random.sample(jungle,2)
    e += random.sample(woestijn,2)
    e += random.sample(gletsjer,2)
    e.sort()
    
    #toeristenwinkel
    w = [21, 41, 61, 81]
    
    return x,s,t,v,e,w

def setup():
    nathan.setBackground()
    fill(255)
    rect(width / 4 - 300, height / 2 - 100, 400, 100)
    rect(width / 4 - 300, height / 2 + 100, 400, 100)
    fill(0)
    textAlign(CENTER)
    textSize(40)
    text('Standaard', width / 5, height / 2 - 25)
    text('Randomized', width / 5, height / 2 + 170)
    if width / 4 - 300 < mouseX < width / 4 + 300 and height / 2 - 100 < mouseY < height / 2:
        opzet = standaard()
        printData(opzet)
    if width / 4 - 300 < mouseX < width / 4 + 300 and height / 2 + 100 < mouseY < height / 2 + 200:
        opzet = generate()
        printData(opzet)
        
def printData(opzet):
    x,s,t,v,e,w = opzet
    nathan.setBackground()
    fill(255)
    rect(340,380,1190,350)
    rect(width / 4 - 500, height / 2 - 550, 200, 75)
    textAlign(LEFT)
    fill(0)
    text('Terug', width /  4 - 450, height / 2 - 500)
    fill(255)
    fill(0)
    textSize(30)
    text('valkuilen: ',450,455)
    text( ', '.join(map(str, x)),660,455)
    text('winkels: ',450,495)
    text( ', '.join(map(str, s)),660,495)
    text('tunnels: ',450,535)
    text( ', '.join(map(str, t)),660,535)
    text('geluksvolgels: ',450,575)
    text( ', '.join(map(str, v)),660,575)
    text('events: ',450,615)
    text( ', '.join(map(str, e)),660,615)
    text('toeristenwinkel: ',450,655)
    text( ', '.join(map(str, w)),660,655)

def positieData():
    global opzet
    return opzet
    
