# PCLB
The meaning of this app is to communicate with friendsusing TCP (server/client)in the "Serveur.py" progam and also in UDP usingthe chat part of this same program.

#Connection Procedure Server Mode:

1) Lauch the cmd console inside the folder.

2) Start the server by typing "py Serveur.py server".

3)You'll immediatly get "going server" printed on your screen and receive your IP address.

4) You'll get a message with the IP address and pseudo of your client each time someone connects to you or leaves your server. You also get a message when the list of connected people is sent to them.

#Connection Procedure Client Mode:
1) Launch the cmd console inside the folder. For Mac users start 'Terminal' and get to the folder 'pclb'.

2) Start the server by typing "py Serveur.py client".

3) You'll be asked to enter the IP address of the server you want to join. If you're working on a MacBook this step might fail if you don't enter the IP address in "".
    Ex:
    "172.12.67.3"

4) The second step is the most difficult, find yourself a nice pseudo! Be aware to enter your pseudo the same way you did in step 3 if you're working on MacBooks.

5)The server will now send you a list of connected people you can chat with and ask for a command.By tipping '/help' you'll receive a list of commands you can use with a description of their utility.
!There is no need of a special way of enter for macs ;) !

  We encourage you to try them all to get used with the way of using our programm ;).

6) If you want to talk to someone tippe '/connect'. The serve will ask you who you want to talk to. Simply enter the pseudo of that personne and press enter (MacBook users will have to use "" as before to enter the name of the target personne).The sever will tell you you're connected and you can start chatting! Don't forget to tippe '/send' before the message you want to send. You can talk to different people at the same time but you'll have to '/connect' each time you talk to a different personne. If you want to talk at the same personne twice '/connect' isn't necessary between each message. Mac users don't have to write their message in "".

7) You might not get the personne you want to talk to in the list the server sends you if the personne connects the server after you did. Simply tippe '/refresh' to be sent back the list. This time you should see him.

8) When you're done talking simply tippe '/quit' to exit the conversation and '/exit' to close to program.
