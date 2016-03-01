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
            print('accepted')
            try:
                self._receive(client)
                client.close()
                print('recieved')
                self._ret()

            except OSError:
                print(' Reception failed')

    def _receive(self, client):

        print('decoding')
        data=client.recv(100)
        addresse=pickle.loads(data)
        print(addresse)
        self.__addresse=addresse

    def _ret(self):
        print("connecting ?")
        print(self.__addresse)
        for key in self.__addresse:

            Pseudo=key
            ip=self.__addresse[key]
        print('attempting connection to', ip)

        self.__s.connect((ip,5000))

        print('connected')
        available[Pseudo]=ip
        baviable=pickle.dumps(available)
        self.__s.sendall(baviable)
        last.delete(all)
        self.__s.quit()





class EchoClient():
    def __init__(self,me):
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
        print(nameke)
        address[nameke]=ip
        self.__message = pickle.dumps(address)
        self._join()
        self.__s.listen()
        server,addr=self.__s.accept()

    def _join(self):
        try:
            print('join entering')
            self._send()
            print('sent done ')
            self.__s.close()
            print('close done')
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

    def _hear(self):
        self.__s.listen()




if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'server':
        print('going server')
        EchoServer().listen()
    elif len(sys.argv) == 2 and sys.argv[1] == 'client':
        print('going client')
        EchoClient(sys.argv[1].encode()).prepa()