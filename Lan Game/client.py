from random import random
import socket
from tkinter import *
from threading import Thread
from PIL import ImageTk, Image
from matplotlib import image

screen_width = None
screen_height = None

SERVER = None
PORT = None
IP_ADDRESS = None


canvas1 = None
canvas2 = None

gameWindow = None
dice = None
rollButton = None
playerType = None
playerTurn = None


playerName = None
nameEntry = None
nameWindow = None

leftBoxes = []
rightBoxes = []

finishing_box = None


# Teacher write code here for askPlayerName()

def askPlayerName():
    global screen_height, screen_width, canvas1, playerName, nameEntry, nameWindow

    nameWindow = Tk()
    nameWindow.title("Ludo Ladder")
    nameWindow.attributes('-fullscreen', True)

    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file="./assets/background.png")

    canvas1 = Canvas(nameWindow, width=500, height=500)
    canvas1.pack(fill="both", expand=True)

    canvas1.create_image(0, 0, image=bg, anchor="nw")

    canvas1.create_text(screen_width/2, screen_height/5,
                        text="Enter Name", font=("Chalkboard SE", 100), fill="white")

    nameEntry = Entry(nameWindow, width=15, justify="center",
                      font=("Chalkboard SE", 50), bd=5, bg="white")
    nameEntry.place(x=screen_width/2-220, y=screen_height/4+100)

    button = Button(nameWindow, text="Save", font=(
        "Chalkboard SE", 30), command=saveName, width=15, height=2, bg="darkblue", bd=3)
    button.place(x=screen_width/2-130, y=screen_height/2-30)

    nameWindow.resizable(True, True)
    nameWindow.mainloop()


def gameWindow():
    global gameWindow, canvas2, screen_height, screen_width, dice, rollButton

    gameWindow = Tk()
    gameWindow.title("Ludo Ladder")
    gameWindow.attributes('-fullscreen', True)

    screen_width = gameWindow.winfo_screenwidth()
    screen_height = gameWindow.winfo_screenheight()

    canvas2 = Canvas(gameWindow, width=500, height=500)
    canvas2.pack(fill="both", expand=True)

    bg = ImageTk.PhotoImage(file="./assets/background.png")

    canvas2.create_image(0, 0, image=bg, anchor="nw")

    canvas2.create_text(screen_width/2, screen_height/5,
                        text="Ludo Ladder", font=("Chalkboard SE", 100), fill="white")

    gameWindow.resizable(True, True)

    leftBoard()
    rightBoard()
    finishingBox()

    dice = canvas2.create_text(screen_width/2+10, screen_height/2 +
                               250, text="\u2680", font=("Chalkboard SE", 250), fill="white")

    rollButton = Button(gameWindow, text="Roll Dice", fg="black", font=(
        "Chalkboard SE", 15), bg="grey", command=rollDice, width=20, height=5)

    global playerTurn
    global playerType
    global playerName


    if(playerType == 'player1' and playerTurn):
        rollButton.place(x=screen_width / 2 - 80, y=screen_height/2  + 250)
    else:
        rollButton.pack_forget()

    gameWindow.mainloop()


def leftBoard():
    global gameWindow, leftBoxes, screen_height

    xPos = 30

    for box in range(0, 11):
        if box == 0:
            boxLabel = Label(gameWindow, font=(
                "Helvetica", 30), width=2, height=1, relief="ridge", borderwidth=1, bg="red")
            boxLabel.place(x=xPos, y=screen_height/2-88)

            leftBoxes.append(boxLabel)

            xPos += 50

        else:
            boxLabel = Label(gameWindow, font=(
                "Helvetica", 55), width=2, height=1, relief="ridge", borderwidth=1, bg="white")
            boxLabel.place(x=xPos, y=screen_height/2-100)

            leftBoxes.append(boxLabel)

            xPos += 85


def rightBoard():
    global gameWindow, rightBoxes, screen_height

    xPos = 988

    for box in range(0, 11):
        if box == 10:
            boxLabel = Label(gameWindow, font=(
                "Helvetica", 30), width=2, height=1, relief="ridge", borderwidth=1, bg="yellow")
            boxLabel.place(x=xPos, y=screen_height/2-88)

            rightBoxes.append(boxLabel)

            xPos += 50

        else:
            boxLabel = Label(gameWindow, font=(
                "Helvetica", 55), width=2, height=1, relief="ridge", borderwidth=1, bg="white")
            boxLabel.place(x=xPos, y=screen_height/2-100)

            rightBoxes.append(boxLabel)

            xPos += 85


def finishingBox():
    global gameWindow, finishing_box, screen_width, screen_height

    finishing_box = Label(gameWindow, text="Home", font=(
        "Chalkboard SE", 32), width=8, height=4, borderwidth=0, bg="green", fg="white")
    finishing_box.place(x=screen_width/2-68, y=screen_height/2-160)


def saveName():
    global SERVER, playerName, nameWindow, nameEntry

    playerName = nameEntry.get()
    nameEntry.delete(0, END)
    nameWindow.destroy()

    SERVER.send(playerName.encode())

    gameWindow()


def rollDice():
    global SERVER
    diceChoices = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']

    value = random.choice(diceChoices)

    rollButton.destroy()
    playerTurn = False

    if(playerType == 'player1'):
        SERVER.send(f'{value}player2Turn'.encode())

    if(playerType == 'player2'):
        SERVER.send(f'{value}player1Turn'.encode())


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT = 5000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    # Creating First Window
    askPlayerName()


setup()
