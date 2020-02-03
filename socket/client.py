#!/bin/python3
import socket
import pickle
import threading
import sys

class ClientThread(threading.Thread):
    def __init__(self, my_socket):
        threading.Thread.__init__(self)
        self.s = my_socket
        self.msg = ""
        self.prepare = ""

    def run(self):
        while (1):
            try:
                self.prepare = self.s.recv(10)
                self.prepare = self.s.recv(int(self.prepare))
                self.msg = pickle.loads(self.prepare)
                if (self.msg.find("exit") != -1):
                    break
                print(self.msg)
            except:
                print("Disconnected")
                sys.exit(0)
        sys.exit(0)

class ClientSend(threading.Thread):
    def __init__(self, my_socket, user):
        threading.Thread.__init__(self)
        self.s = my_socket
        self.user = user
        self.raw = ""
        self.msg = ""
        self.prepare = ""

    def run(self):
        while (1):
            self.raw = input()
            self.msg = pickle.dumps(self.user + " : " + self.raw)
            self.prepare = str(len(self.msg))
            while (len(self.prepare) < 10):
                self.prepare += " "
            self.s.send(bytes(self.prepare, "utf-8") + self.msg)
            if (self.raw.find("exit") != -1):
                sys.exit(0)


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("", 1111))
    user = input("Votre pseudo : ")
    newthread = ClientThread(s)
    sendthread = ClientSend(s, user)
    newthread.start()
    sendthread.start()
except:
    print("Unable to connect to host.")
