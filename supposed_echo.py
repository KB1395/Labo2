import socket
import sys
import pickle

SERVER = (socket.gethostbyname(socket.gethostname()), 6000)
me = {}
last = {}
available = {}

class EchoServer():


    def __init__(self):
        self.__s = socket.socket()
        self.__s.bind(SERVER)



    def listen(self):
        self.__s.listen(20)
        while True:
            client, addr = self.__s.accept()
            try:
                self._receive(client)
                self._ret(client)
                client.close()
                print('data sent')

            except OSError:
                print(' Reception failed')

    def _receive(self, client):
        data=client.recv(100)
        addresse=pickle.loads(data)
        self.__addresse=addresse

    def _ret(self,client):
        for key in self.__addresse:

            Pseudo=key
            ip=self.__addresse[key]
        print('attempting connection to', ip)
        available[Pseudo]=ip
        baviable=pickle.dumps(available)
        client.send(baviable)





class EchoClient():
    def __init__(self):
        self.__s = socket.socket()
        clientaddr=socket.gethostbyname(socket.gethostname())
        self.__s.bind((clientaddr,5000))
        self.__message = clientaddr

    def prepa(self):
        address={}
        self.__s.connect(SERVER)
        ip = socket.gethostbyname(socket.gethostname())
        print(ip)
        print('Choisissez un pseudo: ')
        nameke = input()
        address[nameke]=ip
        self.__message = pickle.dumps(address)
        self._join()
        data=self.__s.recv(1000)
        decodata=pickle.loads(data)
        print(decodata)
        self.__s.close()

    def _join(self):
        try:
            self._send()
        except OSError:
            print('Unfindable server')

    def _send(self):
        message = self.__message
        totalsent = 0
        try:
            while totalsent < len(message):
                sent = self.__s.send(message[totalsent:])
                if sent !=None:
                    totalsent += sent
        except OSError:
            print("Sending failed")




if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'server':
        print('going server')
        EchoServer().listen()
    elif len(sys.argv) == 2 and sys.argv[1] == 'client':
        print('going client')
        EchoClient().prepa()