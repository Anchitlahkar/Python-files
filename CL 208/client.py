# -----------Bolierplate Code Start -----
from cProfile import label
from lib2to3.pgen2.token import NAME
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk, filedialog


PORT = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096
name = None
listbox = None
textArea = None
labelChat = None
text_message = None


def openChatWindow():
    print("\n\t\t\t\t\t\tIP MESSENGER\n")

    global name, listbox, text_message

    window = Tk()
    window.title('Messenger')
    window.geometry("500x350")

    nameLabel = Label(window, text="Enter Your Name", font=("Calibri", 10))
    nameLabel.place(x=10, y=8)

    name = Entry(window, width=30, font=("Calibri", 10))
    name.place(x=120, y=8)
    name.focus()

    connectServer = Button(
        window, text="Connect To Chat Server", bd=1, font=("Calibri", 10))
    connectServer.place(x=350, y=6)

    separator = ttk.Separator(window, orient="horizontal")
    separator.place(x=0, y=35, relwidth=1, height=0.1)

    labelUsers = Label(window, text="Active Users", font=("Calibri", 10))
    labelUsers.place(x=10, y=50)

    listbox = Listbox(window, height=5, width=67,
                      activestyle="dotbox", font=("Calibri", 10))
    listbox.place(x=10, y=70)

    scrollBar1 = Scrollbar(listbox)
    scrollBar1.place(relheight=1, relx=1)
    scrollBar1.config(command=listbox.yview)

    connectButton = Button(window, text="Connect", bd=1, font=("Calibri", 10))
    connectButton.place(x=282, y=160)

    disconnectButton = Button(
        window, text="Disconnect", bd=1, font=("Calibri", 10))
    disconnectButton.place(x=350, y=160)

    refresh = Button(window, text="Refresh", bd=1, font=("Calibri", 10))
    refresh.place(x=435, y=160)

    labelChat = Label(window, text="Chat Window", font=("Calibri", 10))
    labelChat.place(x=10, y=180)

    textArea = Text(window, width=67, height=6, font=("Calibri", 10))
    textArea.place(x=10, y=200)

    scrollBar2 = Scrollbar(textArea)
    scrollBar2.place(relheight=1, relx=1)
    scrollBar2.config(command=textArea.yview)

    text_message = Entry(window, width=43,  font=("Calibri", 12))
    text_message.pack()
    text_message.place(x=98, y=306)

    send = Button(window, text="Send", bd=1, font=("Calibri", 10))
    send.place(x=450, y=305)

    attach = Button(window, text="Attach and Send", bd=1, font=("Calibri", 10))
    attach.place(x=10, y=305)

    filePathLabel = Label(window, text="", fg="blue", font=("Calibri", 8))
    filePathLabel.place(x=10, y=330)

    window.mainloop()


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    openChatWindow()


setup()


# -----------Bolierplate Code Start -----
