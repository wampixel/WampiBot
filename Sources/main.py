#!/usr/bin/env python3
# permet de creer un bot qui se connecte et qui renvoi en message prive a MASTER tous les messages lus sur le chat

import socket


HOST = "irc.langochat.net"
CHAN = "wampixelandco"
PORT = 6667

NICK = "wampixelBot"
IDENT = "wampixelBot"
REALNAME = "wampixelBot"
MASTER = "Wampixel"

buff = ""

IRC=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IRC.connect((HOST, PORT))

IRC.send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
IRC.send(bytes("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME), "UTF-8"))
IRC.send(bytes("JOIN #%s\r\n" % CHAN, "UTF-8"))

IRC.send(bytes("PRIVMSG %s :Hello Master _o_\r\n" % MASTER, "UTF-8"))
print(IRC.recv(4096).decode("UTF-8"))

while True :
    buff = IRC.recv(1024).decode("UTF-8")

    IRC.send(bytes("PRIVMSG %s :%s\r\n" % (MASTER, buff), "UTF-8"))
