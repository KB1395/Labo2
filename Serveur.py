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
     # First routine in server makes him listen continuously to incoming connections.
        while True:
            self.__s.listen(20)
            client, addr = self.__s.accept()
            try:
                self._receive(client)
                self._ret(client)
                client.close()
                print('Data sent')

            except OSError:
                print(' Reception failed')



    def _receive(self, client):
    #Server receives IP addrese and pseudo from client and puts it into addresse list.
        data=client.recv(100)
        addresse=pickle.loads(data)
        self.__addresse=addresse



    def _ret(self,client):
    #Checks every element in addresse and adds separatly pseudo's and addresses to available dictionnary.
        for key in self.__addresse:

            Pseudo=key
            print('Connection from:',self.__addresse)
            status=self.__addresse[key].split(' ')
            if len(status)>1 and status[1]=='out':
                print('logoff detected')
                available.pop(Pseudo,None)
                logoff=('disconnected')
                baviable=logoff.encode()
            else:
                ip=self.__addresse[key]
                available[Pseudo]=ip
            #Converting availables dictionnary into bites.
                baviable=pickle.dumps(available,protocol=2)
        #Sends all available contacts back to clients.
        client.send(baviable)





class EchoClient():
    def __init__(self):
        self.__s = socket.socket()
        clientaddr=socket.gethostbyname(socket.gethostname())
        self.__s.bind((clientaddr,5000))
        self.__message = clientaddr

    def prepa(self):
    #First step is to precise the IP addresse of the wanted server and to connect to him.
        address={}
        self.__ip=input('Please enter server\'s ip address:')
        self.__SERVER=(self.__ip,6000)
        try:
            self.__s.connect(self.__SERVER)
            clientip = socket.gethostbyname(socket.gethostname())
            print(clientip)
            print('Choose your pseudo: ')
            nameke = input()
            self.__pseudo=nameke
        #Creating a dictionnary with client's pseudo as key and his IP as value.
            address[nameke]=clientip
        #".dumps()" converts address into binary values.
        #As our programme had to work between MacBooks and Windows computers, we had to use a protocol 2 to dump.
            self.__message = pickle.dumps(address,protocol=2)
            self._join()
        #Client gets back the dictionnary of connected people.
            data=self.__s.recv(1000)
        #".loads" converts the recieved bites into dictionnary.
            decodata=pickle.loads(data)
            print('Connected people:')
            for key in decodata:
                print(key)
            self.__s.close()
        #When you know who's connected to chat you're good and you can get started =) .
            self._chat(decodata)
        except:
            print('Serveur introuvable')


    def _join(self):
    #Bypass.
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
    #We choose to propose a few commands to clients to make communication easy while keeping it basic.
        print('Enter command (or /help for command list):')
        handlers = {
            '/exit': self._exit,
            '/quit': self._quit,
            '/send': self._sendchat,
            '/connect': self._connection,
            '/help':self._help,
            '/refresh':self._refresh
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

                
    #When you're done talking and you wanna leave your address goes to "None" and the programme stops running.
    def _exit(self):
        self.__running = False
        self.__address = None
        self._disconnect()
        self.__c.close()


        
    def _help(self):
        print('/connect #to join someone (No parameter needed)')
        print("/quit #to quit discution")
        print("/exit #to exit program")
        print("/send #to send your message")
        print("/refresh #to refresh the list of connected people")



    def _quit(self):
        self.__destinataire = None




    #Connecting to someone happens in 2 steps: first saying you want to connect someone, then sayins to who you want to talk.
    def _connection(self):
        try:
            who=input('Who do you want to talk to?')
            self.__s = socket.socket()
            clientaddr=socket.gethostbyname(socket.gethostname())
            self.__s.bind((clientaddr,5000))
            address={}
            self.__s.connect(self.__SERVER)
            clientip = socket.gethostbyname(socket.gethostname())
            address[self.__pseudo]=clientip
            self.__message = pickle.dumps(address,protocol=2)
            self._join()
            data=self.__s.recv(1000)
            decodata=pickle.loads(data)
            self.__people=decodata
            self.__s.close()

            if who in self.__people:
                destinataire=self.__people[who]
                self.__receveur=who
                port=5000
                self.__destinataire=(destinataire,port)
                print('Connected to',who)
            else:
                print("Asked person not found")
        except:
            print('This person is disconnected')



            
    def _sendchat(self,param):
        try:
            tokens=param.split(' ')
            self.__s = socket.socket()
            clientaddr=socket.gethostbyname(socket.gethostname())
            self.__s.bind((clientaddr,5000))
            address={}
            self.__s.connect(self.__SERVER)
            clientip = socket.gethostbyname(socket.gethostname())
            address[self.__pseudo]=clientip
            self.__message = pickle.dumps(address,protocol=2)
            self._join()
            data=self.__s.recv(1000)
            decodata=pickle.loads(data)
            self.__people=decodata
            self.__s.close()

            if self.__destinataire is not None and self.__receveur in self.__people:
                try:
                    string = " ".join(tokens[0:])
                    message=(self.__pseudo+' says: '+string).encode()

                    totalsent = 0
                    while totalsent < len(message):
                        sent = self.__c.sendto(message[totalsent:], self.__destinataire)
                        totalsent += sent
                except OSError:
                    print('Message reception failed.')
            else:
                print('Person disconnected')
        except:
            print('Person disconnected')



    def _receive(self):
        while self.__running:
            try:
                data, self.__address = self.__c.recvfrom(1024)
                print(data.decode())
            except socket.timeout:
                pass
            except OSError:
                return

    #If someone connects to the server after you established your connection, you will not see him.
    #The refresh command allows you to checks who's connected at any time.
    def _refresh(self):
        self.__s = socket.socket()
        clientaddr=socket.gethostbyname(socket.gethostname())
        self.__s.bind((clientaddr,5000))
        address={}
        self.__s.connect(self.__SERVER)
        clientip = socket.gethostbyname(socket.gethostname())
        address[self.__pseudo]=clientip
        print(address[self.__pseudo])
        self.__message = pickle.dumps(address,protocol=2)
        self._join()
        data=self.__s.recv(1000)
        decodata=pickle.loads(data)
        print('Connected people:')
        for key in decodata:
            print(key)
        self.__people=decodata
        self.__s.close()


    #Disconnect allows you to get out of the available dictionnary.
    def _disconnect(self):
        self.__s = socket.socket()
        clientaddr=socket.gethostbyname(socket.gethostname())
        self.__s.bind((clientaddr,5000))
        self.__message = clientaddr
        address={}
        self.__s.connect(self.__SERVER)
        clientip = socket.gethostbyname(socket.gethostname())
        address[self.__pseudo]=clientip+' out'
        self.__message = pickle.dumps(address,protocol=2)
        self._join()
        print('Logoff request sent')
        self.__s.close()



#When running this code on Bash you need to specify is you want to be server or client.
#Herefor you simply need to say "server" or "client" after "python Serveur.py".

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'server':
        print('going server')
        EchoServer().listen()
    elif len(sys.argv) == 2 and sys.argv[1] == 'client':
        print('going client')
        EchoClient().prepa()
