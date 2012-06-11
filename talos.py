import socket
import time

server = "adams.freenode.net"
channel = "#Ephestos"
nick = "Ephestos"
port = 6667
symbol = "$"
blank = ""
running = True

def quit():
    global running
    running = False
    print("quiting")
    irc.send(bytes("QUIT "+ CHANNEL +"\n","utf-8"))

def ping(msg):
    irc.send("PONG :"+ msg +"\r\n")

def error():
    irc.send(bytes("PRIVMSG "+ CHANNEL +" :No idea what you talking about.\n","utf-8"))

irc = socket.socket( )
irc.connect((server, port))
irc.send(bytes("USER "+ nick +" "+ nick +" "+ nick +" "+nick+"\r\n","utf-8"))
irc.send(bytes("NICK "+ nick +"\r\n","utf-8"))
irc.send(bytes("JOIN "+ channel +"\r\n","utf-8"))

while running:
  line = str(irc.recv(2048))
  line = line.strip("\r\n")
  print(line)
  stoperror = line.split(" ")
  if ("PING :" in line):
        pingcmd = line.split(":", 1)
        pingmsg = pingcmd[1]
        ping(pingmsg)
  elif "PRIVMSG" in line:

      if len(line) < 30:
          print( blank )
      elif len(stoperror) < 4:
          print( blank )
      else:
          complete = line.split(":", 2)
          info = complete[1]
          msg = line.split(":", 2)[2] ##the thing that was said
          cmd = msg.split(" ")[0]

          print("cmd : ",cmd)
          CHANNEL = info.split(" ")[2] ##channel from which it was said
          print("CHANNEL: ",CHANNEL)
          user = line.split(":")[1].split("!")[0] ## the person that said the thing
          print("user : ",user)
          arg = msg.split(" ")
          print("arg : ",arg)


          if "$quit" in cmd:
              quit()

          elif symbol in cmd:
              error()
