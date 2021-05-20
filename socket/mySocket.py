import socket
import threading
import pickle

def doNothing(s):
    pass

class myServer(threading.Thread):
    def __init__(self, port, acceptCallBack=doNothing):
        self.acceptCallBack = acceptCallBack
        threading.Thread.__init__(self)
        self.port = port
        self.clients = [] # array of Clients
        self.clients_sockets = [] # array of socket
        self.listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listen_socket.bind(("", port))
        self.listen_socket.listen(16)
        self.go = True


    def run(self):
        print("Starting server on port  " + str(self.port))

        while self.go:
            s = self.listen_socket.accept()
            if (not self.go):
                return
            print(s[1])
            s = s[0]
            print("connection to "+ str(s))
            c = mySocket(s)
            #self.acceptCallBack(c)
            threading.Thread(target=self.acceptCallBack, args=[c]).start()
            self.clients.append(c)

    def stop(self):
        self.go = False
        for client in self.clients:
            client.close()
        self.listen_socket.settimeout(0.1)
        s = mySocket()
        s.connect("127.0.0.1", self.port)
        print("stop server")



class mySocket():
    def __init__(self, s=0):
        if s == 0:
            self.s = socket.socket()
            self.s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
        else:
            self.s = s

    def connect(self, ip, port):
        self.s.connect((ip, port))
    
    def sendObject(self, data):
        data = pickle.dumps(data)

        self.s.sendall(bytes(f'{len(data):<10}', "utf-8") + data)

    def recvObject(self):
        msg_sys = self.s.recv(10)
        while len(msg_sys) < 10:
            msg_sys += self.s.recv(10-len(msg_sys))
        size = int(msg_sys)
        msg_sys = self.s.recv(size)
        while len(msg_sys) < size:
            msg_sys += self.s.recv(size - len(msg_sys))
        return pickle.loads(msg_sys)

    def close(self):
        self.s.close()