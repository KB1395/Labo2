import socket
import sys
import pickle
import threading
SERVER = (socket.gethostbyname(socket.gethostname()), 6000)
me = {}
last = {}
available = {}

class EchoServer():


    def __init__(self):
        self.__s = socket.socket()
        self.__s.bind(SERVER)
        print(SERVER)



    def listen(self):

        while True:
            self.__s.listen(20)
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
        baviable=pickle.dumps(available,protocol=2)
        client.send(baviable)





class EchoClient():
    def __init__(self):
        self.__s = socket.socket()
        clientaddr=socket.gethostbyname(socket.gethostname())
        self.__s.bind((clientaddr,5000))
        self.__message = clientaddr

    def prepa(self):
        address={}
        ip=input('Please enter server\'s ip address:')
        SERVER=(ip,6000)
        self.__s.connect(SERVER)
        clientip = socket.gethostbyname(socket.gethostname())
        print(clientip)
        print('Choose your pseudo: ')
        nameke = input()
        self.__pseudo=nameke
        address[nameke]=clientip
        self.__message = pickle.dumps(address,protocol=2)
        self._join()
        data=self.__s.recv(1000)
        decodata=pickle.loads(data)
        print('Connected people:')
        for key in decodata:
            print(key)
        self.__s.close()
        self._chat(decodata)

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
    def _chat(self,decodata):
        self.__people=decodata
        host=socket.gethostbyname(socket.gethostname())
        port=5000
        s = socket.socket(type=socket.SOCK_DGRAM)
        s.settimeout(0.5)
        s.bind((host, port))
        self.__c = s
        print('Listening on {}:{}'.format(host, port))
        print('Enter command (or /help for command list):')
        handlers = {
            '/exit': self._exit,
            '/quit': self._quit,
            '/send': self._sendchat,
            '/connect': self._connection,
            '/help':self._help
        }
        self.__running = True
        self.__address = None
        threading.Thread(target=self._receive).start()
        while self.__running:
            line = sys.stdin.readline().rstrip() + ' '
            # Extract the command and the param
            command = line[:line.index(' ')]
            param = line[line.index(' ')+1:].rstrip()
            # Call the command handler
            if command in handlers:
                try:
                    handlers[command]() if param == '' else handlers[command](param)
                except:
                    print("Command execution failed.")
            else:
                print('Unknown command:', command)

    def _exit(self):
        self.__running = False
        self.__address = None
        self.__c.close()
    def _help(self):
        print('/connect #to join someone (No parameter needed)')
        print("/quit #to quit discution")
        print("/exit #to exit program")
        print("/send #to send your message")

    def _quit(self):
        self.__address = None
    def _connection(self):
        who=input('Who do you wanna talk to?')
        if who in self.__people:
            destinataire=self.__people[who]
            port=5000
            self.__destinataire=(destinataire,port)
            print('connected to',who)
        else:
            print("Asked person not found")
    def _sendchat(self,param):
        tokens=param.split(' ')

        if self.__destinataire is not None:
            try:
                string = " ".join(tokens[0:])
                message=(self.__pseudo+' says: '+string).encode()

                totalsent = 0
                while totalsent < len(message):
                    sent = self.__c.sendto(message[totalsent:], self.__destinataire)
                    totalsent += sent
            except OSError:
                print('Message reception failed.')

    def _receive(self):
        while self.__running:
            try:
                data, self.__address = self.__c.recvfrom(1024)
                print(data.decode())
            except socket.timeout:
                pass
            except OSError:
                return





if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'server':
        print('going server')
        EchoServer().listen()
    elif len(sys.argv) == 2 and sys.argv[1] == 'client':
        print('going client')
        EchoClient().prepa()
