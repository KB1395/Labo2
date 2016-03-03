# PCLB
The meaning of this app is to communicate with friends using TCP (server/client)in the "Serveur.py" program and also in UDP using the chat part of this same program.

#Connection Procedure Server Mode:

1) Launch the cmd console inside the folder.

2) Start the server by typing "py Serveur.py server".

3)You'll directly get "going server" printed on your screen and receive your IP address.

4) You'll get a message with the IP address and pseudo of the client each time someone connects or leaves your server. You also get a message when the list of connected people is sent to them.

#Connection Procedure Client Mode:
1) Launch the cmd console inside the folder. For Mac users start 'Terminal' and get to the folder 'pclb'.

2) Start the server by typing "py Serveur.py client".

3) You'll be asked to enter the IP address of the server you want to join (this address is showed at the startup of the server). If you're working on a MacBook this step might fail if you don't enter the IP between quotes.
    E.g.:
    "172.12.67.3"

4) The second step is the most difficult, find yourself a nice pseudo! Be aware to enter your pseudo the same way you did for the IP in step 3 if you're working on MacBooks. E.g.:"Me"

5)The server will now send you a list of connected people you can chat with and ask for a command. By typing '/help' you'll receive a list of commands you can use with a description of their utility.
!There is no need of a special way of enter for macs ;) !

  We encourage you to try them all to get used with the way of using our program ;).

6) If you want to talk to someone type '/connect'. The server will ask you who you want to talk to. Simply enter the pseudo of that person and press enter (MacBook users will have to use "" as before to enter the name of the target person).The sever will tell you you're connected and you can start chatting! Don't forget to type '/send' before the message you want to send. You can talk to different people at the same time but you'll have to '/connect' each time you want to talk to a different person. If you want to talk at the same person twice '/connect' isn't necessary between each message. Mac users don't have to write their message in "".
Therefore, if the person you were connected with disconnected, you'll see that with your next send that he/she's gone. it's the same if you want to connect with somebody gone.

7) You might not get the person you want to talk to in the list the server sends you if the person connects the server after you did. Simply type '/refresh' to be sent back the list. This time you should see him. More, a "whosthere" is automatically run when you want to connect or send to make sure the person still there.

8) When you're done talking simply type '/quit' to exit the conversation and '/exit' to close to program.

Caution: If you quit the brutal way (whitout /exit) You won't be removed from the list of connected people
