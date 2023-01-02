import turtle
from turtle import Screen, Turtle
import math
import numpy as np
import time


#Piirretään pelilauta
def drawBoard():
    #Piirretään vaakaviivat
    for i in range(2):
        drawer.penup()
        drawer.goto(-300, 100 - 200 * i)
        drawer.pendown()
        drawer.forward(600)
    
    drawer.right(90)

    #Piirretään pystyviivat
    for i in range(2):
        drawer.penup()
        drawer.goto(-100 + 200 * i, 300)
        drawer.pendown()
        drawer.forward(600)


#Numerot ruutujen nurkkiin
    num = 1
    for i in range(3):
        for j in range(3):
            drawer.penup()
            drawer.goto(-290 + j * 200, 280 - i * 200)
            drawer.pendown()

            drawer.write(num, font = ("Arial", 12))
            num += 1




#Piirretään 'X' oikeaan ruutuun
def drawX(x, y):
    #Liikkuu oikeaan paikkaan
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()

    drawer.setheading(60)

    #Piirretään X:än viivat
    for i in range(2):
        drawer.forward(75)
        drawer.backward(150)
        drawer.forward(75)
        drawer.left(60)

    #Päivitetään ruutu
    screen.update()

#Piirretään 'O' oikeaan ruutuun
def drawO(x, y):
    #Liikkuu oikeaan paikkaan
    drawer.penup()
    drawer.goto(x, y + 75)
    drawer.pendown()

    drawer.setheading(0)

    #Piirretään ympyrä
    for i in range(180):
        drawer.forward((150 * math.pi)/180)
        drawer.right(2)

    #Päivitetään ruutu
    screen.update()

#Tämä funktio tarkistaa onko jompikumpi voittanut
def checkWon():
    letterX = (1)
    letterO = (2)
    #Tarkistetaan onko vaakatasossa tai pystyyn kolmea peräkanaa
    #for i in range(3):
    if gameBoard[0] == gameBoard[1] and gameBoard[1] == gameBoard[2] and gameBoard[0] == letterX:
        return True
    elif gameBoard[0] == gameBoard[1] and gameBoard[1] == gameBoard[2] and gameBoard[0] == letterO:
        return True

    if gameBoard[3] == gameBoard[4] and gameBoard[4] == gameBoard[5] and gameBoard[3] == letterX:
        return True
    elif gameBoard[3] == gameBoard[4] and gameBoard[4] == gameBoard[5] and gameBoard[3] == letterO:
        return True

    if gameBoard[6] == gameBoard[7] and gameBoard[7] == gameBoard[8] and gameBoard[6] == letterX:
        return True
    elif gameBoard[6] == gameBoard[7] and gameBoard[7] == gameBoard[8] and gameBoard[6] == letterO:
        return True

    #Tarkistetaan onko vinottain kolmea peräkanaa alaspäin
    if gameBoard[0] == gameBoard[4] and gameBoard[4] == gameBoard[8] and gameBoard[0] == letterX:
        return True
    elif gameBoard[0] == gameBoard[4] and gameBoard[4] == gameBoard[8] and gameBoard[0] == letterO:
        return True

    #Tarkistetaan onko vinottain kolmea peräkanaa ylöspäin
    if gameBoard[6] == gameBoard[4] and gameBoard[4] == gameBoard[2] and gameBoard[6] == letterX:
        return True
    elif gameBoard[6] == gameBoard[4] and gameBoard[4] == gameBoard[2] and gameBoard[6] == letterO:
        return True

    #Jos nyt annettu viesti ei ole voittanut
    return False


global gameBoard 
gameBoard = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])



def laskeRuutu(siirretty):
    ruutu = [0,0]
    row = ()
    column = ()
    if siirretty == (1) or siirretty == (2) or siirretty == (3):
        row = (0)
    if siirretty == (4) or siirretty == (5) or siirretty == (6):
        row = (1)
    if siirretty == (7) or siirretty == (8) or siirretty == (9):
        row = (2)
    if siirretty == (1) or siirretty == (4) or siirretty == (7):
        column = (0)
    if siirretty == (2) or siirretty == (5) or siirretty == (8):
        column = (1)
    if siirretty == (3) or siirretty == (6) or siirretty == (9):
        column = (2)
    ruutu[0] = (row)
    ruutu[1] = (column)
    return (ruutu)



#Tämä funktio yrittää lisätä x:än syötettyyn paikkaan
def addX(siirretty):
    #Poistetaan kaikki ilmoitukset ruudulta
    announcer.clear()
    ruutu = laskeRuutu(siirretty)
    row = ruutu[0]
    column = ruutu[1]
    #Tarkistaa onko paikka, johon halutaan syöttää, tyhjä
    if board[row][column] == "x" or board[row][column] == "o":
        #Kerrotaan että paikka on jo otettu
        announcer.write("That spot is taken!", font = ("Arial", 36))
        screen.update
    else:
        #Piirrä x oikeaan paikkaan
        drawX(-200 + 200 * column, 200 - 200 * row, )

#Tämä funktio yrittää lisätä x:än syötettyyn paikkaan
def addO(siirretty):
    #Poistetaan kaikki ilmoitukset ruudulta
    announcer.clear()
    ruutu = laskeRuutu(siirretty)
    row = ruutu[0]
    column = ruutu[1]
    #Tarkistaa onko paikka, johon halutaan syöttää, tyhjä
    if board[row][column] == "x" or board[row][column] == "o":
        #Kerrotaan että paikka on jo otettu
        announcer.write("That spot is taken!", font = ("Arial", 36))
        screen.update
    else:
        #Piirrä x oikeaan paikkaan
        drawO(-200 + 200 * column, 200 - 200 * row, )
    






#Lisätään tietokonepelaaja nro:1
def playerX():
    siirto = (0)
    time.sleep(0.5)
    if gameBoard[4] == (0):
        siirto = (5)
    elif gameBoard[0] == (0):
        siirto = (1)
    elif gameBoard[2] == (0):
        siirto = (3)
    elif gameBoard[6] == (0):
        siirto = (7)
    elif gameBoard[8] == (0):
        siirto = (9)
    elif gameBoard[1] == (0):
        siirto = (2)
    elif gameBoard[5] == (0):
        siirto = (6)
    elif gameBoard[7] == (0):
        siirto = (8)
    elif gameBoard[3] == (0):
        siirto = (4)
    gameBoard[siirto - (1)] = (1)
    return siirto


#Lisätään tietokonepelaaja nro:2
def playerO():
    siirto = (0)
    time.sleep(0.5)
    if gameBoard[0] == (0):
        siirto = (1)
    elif gameBoard[1] == (0):
        siirto = (2)
    elif gameBoard[2] == (0):
        siirto = (3)
    elif gameBoard[3] == (0):
        siirto = (4)
    elif gameBoard[4] == (0):
        siirto = (5)
    elif gameBoard[5] == (0):
        siirto = (6)
    elif gameBoard[6] == (0):
        siirto = (7)
    elif gameBoard[7] == (0):
        siirto = (8)
    elif gameBoard[8] == (0):
        siirto = (9)
    gameBoard[siirto - (1)] = (2)
    return siirto




#Luo turtle
drawer = turtle.Turtle()
announcer = turtle.Turtle()

drawer.pensize(10)
drawer.ht()

announcer.penup()
announcer.ht()
announcer.goto(-200, 0)
announcer.color("red")

#Luo ruutu
screen = turtle.Screen()
screen.tracer(0)

#Piirrä lauta
drawBoard()

#Luodaan lauta

global board
board = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(" ")
    board.append(row)


siirretty = ()
aikaMs = str(time.time())
pituus = int(0)
pituus = int(len(aikaMs)- (1))
#print ("aikaMs:" + aikaMs)
arpa = int(aikaMs[pituus])
siirtaja = (0)
if (arpa) <= 5:
    siirtaja = (1)
else:
    siirtaja = (2)

#print ("arpa:" + arpa)

for i in range(9):
    if siirtaja == (1):
        siirretty = playerX()
        addX(siirretty)
        siirtaja = 2
        #print (2)
    else:
        siirretty = playerO()
        addO(siirretty)
        siirtaja = 1
        #print (3)

        #Tarkistetaan onko loppuiko peli
    if checkWon():
        #Kerrotaan pelaajalle voitosta
        announcer.goto(-90, 0)
        announcer.write("Peli päättyi!", font = ("Arial", 40))

        #Päivitetään ruutu ja kytketään event listenerit pois
        screen.update()
        break
        

turtle.done()
