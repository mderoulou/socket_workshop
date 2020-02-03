#!/bin/python3
import socket
import threading
import pickle

client_list = []
class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket, client_list):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        self.prepare = ""
        self.size = ""
        self.msg = ""

    def run(self):
        try:
            print("Connexion de %s %s" % (self.ip, self.port, ))
            while (1):
                self.size = self.clientsocket.recv(10)
                self.prepare = self.clientsocket.recv(int(self.size))
                self.msg = pickle.loads(self.prepare)
                if (self.msg.find("exit") != -1):
                    break
                print("Message reçu de " + str(self.msg))
                for x in client_list:
                    if (self.clientsocket != x):
                        x.send(self.size + self.prepare)
            client_list.remove(self.clientsocket)
            self.msg = pickle.dumps("exit")
            self.prepare = str(len(self.msg))
            while (len(self.prepare) < 10):
                self.prepare += " "
            self.clientsocket.send(bytes(self.prepare, "utf-8") + self.msg)
            print("Client %s %s disconnected" % (self.ip, self.port, ))
        except:
            print("Client %s %s disconnected" % (self.ip, self.port, ))
            client_list.remove(self.clientsocket)

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("",1111))

while True:
    tcpsock.listen(10)
    print("Prêt pour la reception...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    client_list.append(clientsocket)
    newthread = ClientThread(ip, port, clientsocket, client_list)
    newthread.start()
