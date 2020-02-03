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
                print(self.msg)
            except:
                print("Disconnected")
                self._is_running = False
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
                self._is_running = False
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


"""
class socket_serveur(Thread):
    def __init__(self, port = 4242):
        Thread.__init__(self)
        self.port = port
        self.player = []
        self.player_com = []
        self.connect_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect_socket.bind(("", port))
        self.connect_socket.listen(16)

    def run(self):
        self.n = 0
        self.player_com = []
        self.player = []
        while True:
            self.player.append(self.connect_socket.accept())
            print("connection to "+ str(self.player[self.n]))
            print("-"*10)
            print(self.player[self.n])

            self.player_com.append(socket_flox.open_communication(self.player[self.n][0], continu = True))
            self.player_com[self.n].start()
            print("player_come : "+str(self.player_com[0]))
            self.n+=1


    class open_communication(Thread):
        def __init__(self, socket, continu = True):
            Thread.__init__(self)
            self.continu = continu
            self.s = socket
            self.msg = ""

        def run(self):
            Thread.__init__(self)
            print("start")
            global db_con, c
            db_con = sqlite3.connect("db.db")
            c = db_con.cursor()
            while self.continu:
                self.msg_sys = self.s.recv(10)
                self.msg_sys = self.s.recv(int(self.msg_sys))
                self.msg = pickle.loads(self.msg_sys)
                request_read(self.msg,self.s)
                self.ok = True

        def sending(self, msg_send):
            Thread.__init__(self)
            self.msg_send = pickle.dumps(msg_send)
            self.a = str(len(self.msg_send))
            while len(self.a)< 10:
                self.a += " "
            self.s.send(bytes(self.a,"utf-8") + self.msg_send)

        def receive(self):
            self.msg_sys = self.s.recv(10)
            self.msg_sys = self.s.recv(int(self.msg_sys))
            self.msg = pickle.loads(self.msg_sys)
            return (msg)
"""
