import socket
import sys

SERVER = (socket.gethostbyname(socket.gethostname()), 6000)
me = {}
last = {}
available = {}

class EchoServer():


    def __init__(self):
        self.__s = socket.socket()
        self.__s.bind(SERVER)



    def listen (self):
        self.__s.listen(20)
        while True:
            client, addr = self.__s.accept()
            try:
                print(self._receive(client).decode())
 #               client.close()
                for key in last:
                    self._ret()

            except OSError:
                print(' Reception failed')

    def _receive(self, client):
        word = []
        addresse = []
        bullshit = [b'-']

        pseudo = False
        nameke = False
        allin = False

        while not allin:
            data = client.recv(1)
            if data == b'+' or pseudo:
                 pseudo = True
            allin = data == b'/'
            if not pseudo:
                word.append(data)
            else:
                if not allin and data != b'+':
                    addresse.append(data)

        available[b''.join(word)] = b''.join(addresse)
        last[b''.join(word)] = b''.join(addresse)
        for value in last.items():

            print(value[1])
        truc=word+bullshit+addresse
        b''.join(truc)

        return truc

    def _ret(self):
        print("connecting ?")
 #       for value in last.items():
#            a= (value[1],6000)
#            self.__s.connect((a))



# Nécessite décorticage pour envoie, mais ça fait 5h qu'on est dessus donc ça sera pour demain
        print("Connected")
        self.__s.send(available)
        last.delete(all)
        self.__s.quit()




class EchoClient():


    def __init__(self,me):

        self.__s = socket.socket()
        self.__message = me

    def prepa(self):
        self.__s.connect(SERVER)
        ip = socket.gethostbyname(socket.gethostname())
        print(ip)
        print('Choisissez un pseudo: ')
        nameke = input()
        print(nameke)
        me[nameke] = ip
        self.__message = nameke
        self._join()

    def _join(self):
        try:
            print('join entering')
            self._send()
            print('sent done ')
#            self.__s.close()
            print('close done')
            self.__s.listen()
            print('listening')
        except OSError:
            print('Unfindable server')

    def _send(self):
        msg = self.__message
        print(msg)
        print('msg ')
        message=msg.encode()
        totalsent = 0
        try:
            while totalsent < len(message):
                print (totalsent)
                print(message)
                print (len(message))
                sent = self.__s.send(message[totalsent:])
 #               sent = self.__s.send('a')
                print(sent)
                totalsent += sent
        except OSError:
            print("Sending failed")


    def _listen(self):
        self.__s.listen(42)
        back = __s.recv(1024)
        print(back)



if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'server':
        print('going server')
        EchoServer().listen()
    elif len(sys.argv) == 2 and sys.argv[1] == 'client':
        print('going client')
        EchoClient(sys.argv[1].encode()).prepa()