from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter


def connecnt():
    HOST = (input("HOST IP IS : "))
    PORT = 33000
    ADDR = (HOST,PORT)
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(ADDR)
    return client

def receive():
    BUFSIZ = 1024
    while True:
        try:
            msg = client.recv(BUFSIZ).decode("utf8")                
            print(msg)

        except OSError:
            
            break
        
def send():
    while True:
        msg = input()
        print("[ME]: ",msg)
        client.send(msg.encode("utf8"))
        if msg =="--quit":
            print("leaving chat..")
            client.close()
            break




if  __name__ == "__main__":
    client = connecnt()
    
    
    receive_thread = Thread(target=receive)
    send_thread = Thread(target=send)
    receive_thread.start()
    send_thread.start()
    
