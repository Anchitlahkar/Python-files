import socket
from threading import Thread

# Address family-
# IPv4 and IPv6
# AF_INET represents IPv4 while AF_INET6 represents IPv6.

# Socket type-SOCK_STREAM(TCP Socket) and SOCK_DGRAM(UDP Socket)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()

list_of_clients = []
nicknames = []

print("Server is running....")


def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)


def broadcast(message, connection):
    for client in list_of_clients:
        if client != connection:
            try:
                client.send(message.encode("utf-8"))

            except:
                remove(client)


def remove_nickname(nickname):
    if nickname in nicknames:
        nicknames.remove(nickname)


def clientthread(conn, nickname):
    conn.send("Welcome to this chat room !!!!".encode('utf-8'))
    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            if message:
                print(message)
                broadcast(message, conn)
            else:
                remove(conn)
                remove_nickname(nickname)
        except:
            continue


while True:
    conn, addr = server.accept()

    conn.send('NICKNAME'.encode("utf-8"))
    nickname = conn.recv(2048).decode("utf-8")
    nicknames.append(nickname)
    message = '{} joined'.format(nickname)

    list_of_clients.append(conn)

    print(message)
    broadcast(message, conn)

    #  target and args.

    new_thread = Thread(target=clientthread, args=(conn, nickname))
    new_thread.start()
