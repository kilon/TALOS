import socket
import time

server = "adams.freenode.net"
channel = "#Ephestos" 
nick = "Ephestos" 
port = 6667 
symbol = "$"
blank = ""


def quitIRC():
    print("quiting")
    con.send(bytes("QUIT "+ CHANNEL +"\n","utf-8"))

def fail():
    con.send(bytes("PRIVMSG "+ CHANNEL +" :Either you do not have the permission to do that, or that is not a valid command.\n","utf-8"))

con = socket.socket( )
con.connect((server, port))
con.send(bytes("USER "+ nick +" "+ nick +" "+ nick +" "+nick+"\r\n","utf-8"))
con.send(bytes("NICK "+ nick +"\r\n","utf-8"))
con.send(bytes("JOIN "+ channel +"\r\n","utf-8"))

while 1:
  line = str(con.recv(2048))
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
        
       
          if "$quit\\r\\n'"==cmd:
              quitIRC()
            
          elif symbol in cmd:
              fail()
