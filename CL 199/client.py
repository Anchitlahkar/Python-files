import socket
from threading import Thread

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

nickname = input("Choose your Nickname:\t")

ip_address = "127.0.0.1"
port = 8000

client.connect((ip_address, port))

print("Connected with the Server...")


def receive():
    while True:
        try:
            msg = client.recv(2048).decode("utf-8")
            if msg == "NICKNAME":
                client.send(nickname.encode("utf-8"))

            else:
                print(msg)

        except:
            print("An error occurred")
            client.close()
            break


def write():
    while True:
        msg = '{}: {}'.format(nickname, input(''))
        client.send(msg.encode("utf-8"))


receive_thread = Thread(target=receive)
receive_thread.start()

write_thread = Thread(target=write)
write_thread.start()
