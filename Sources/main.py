#!/usr/bin/python3

# permet de creer un bot qui se connecte et qui renvoi en message privé a MASTER en arrivant sur le chat CHAN
# Tous les 5 messages, ce bot envoi un message sur le chan "trop de message BORDEL
# source : https://linuxacademy.com/blog/geek/creating-an-irc-bot-with-python3/

import socket


HOST = "irc.langochat.net"
CHAN = "middleEarth"
PORT = 6667

NICK = "wampixelBot"
IDENT = "wampixelBot"
REALNAME = "wampixelBot"
MASTER = "Wampixel"

buff = ""
i = 0

IRC=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IRC.connect((HOST, PORT))

IRC.send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
IRC.send(bytes("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME), "UTF-8"))
IRC.send(bytes("JOIN #%s\r\n" % CHAN, "UTF-8"))

IRC.send(bytes("PRIVMSG #%s :Hello Master _o_\r\n" % CHAN, "UTF-8"))
print(IRC.recv(4096).decode("UTF-8"), "\n")

while True :
    if 'PING :' in buff :
        IRC.send(bytes("PRIVMSG #%s :I'M BACK BABY !!\r\n" % CHAN, "UTF-8"))
        IRC.send(bytes("PONG :cenedra.langochat.net\r\n", "UTF-8"))
        i -= 1
    if i == 5:
        IRC.send(bytes("PRIVMSG #%s :Trop de message BORDEL\r\n" % CHAN, "UTF-8"))
        i = 0
    buff = IRC.recv(1024).decode("UTF-8")
    if 'oh mon dieu' in buff.lower() :
        IRC.send(bytes("PRIVMSG #%s :Oui?\r\n" % CHAN, "UTF-8"))
        i -= 1
    i += 1
    bufs = buff.split("{} :".format(CHAN))
    print("i = {}: {}".format(i, bufs ))