from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import socket as sc 
"""
global variables 
"""
clients = {}
addresses = {}

def initServer():
        HOST = sc.gethostbyname(sc.gethostname()) #input("Enter server ipV4: ")
        PORT = 33000
        BUFSIZ = 1024
        ADDR = (HOST, PORT)
        s = socket(AF_INET, SOCK_STREAM)
        s.bind(ADDR)
        s.listen(6)
        print("server created and it's ADDR is : ",ADDR)
        return s , BUFSIZ

def accept_conn():

    while True:
        client , client_add = s.accept()
        print("%s:%s has connected." % client_add)
        client.send(bytes("Welcome to our chat.\nplease Enter your Name: ","utf8"))
        addresses[client] = client_add
        Thread(target = handle_client,args=(client,)).start()

def handle_client(client):
    name = client.recv(BUFSIZ).decode("utf8")
    welcome_msg = "You joined chat\nwhen you want to quit chat enter --quit ."
    client.send(welcome_msg.encode("utf8"))
    joined_msg = "%s Has joined to chat" % name
    send_msg(bytes(joined_msg,"utf8"),c=client)
    clients[client] = name

    while True:
        get_msg = client.recv(BUFSIZ)
        if get_msg != "--quit".encode(): #bytes("{quit}","utf8"):
            send_msg(get_msg,name+": ",c = client)
        else:
            #client.send(bytes("{leaving chat..}","utf8"))
            client.close()
            del clients[client]
            send_msg(bytes("%s has left the chat." % name,"utf8"))
            break

def send_msg(msg,name="",c=""):
    for s in clients:
        if   s != c :
                s.send(bytes(name,"utf8")+msg)

if __name__ == "__main__":
        s , BUFSIZ = initServer()
        print("waiting for connections..")
        #ACCEPT_THREAD = Thread(target=accept_conn)
        #ACCEPT_THREAD.start()
        #ACCEPT_THREAD.join()
        accept_conn()
        s.close()
