import socket


HOST = "irc.langochat.net"
CHAN = "middleEarth"
PORT = 6667

NICK = "wampiBot"
MDP  = "wampixBot"
IDENT = "wampiBot"
REALNAME = "wampiBot"
MASTER = "Wampixel"

buff = ""
i = 0

IRC=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IRC.connect((HOST, PORT))

IRC.send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
IRC.send(bytes("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME), "UTF-8"))


print(IRC.recv(4096).decode("UTF-8"), " :: 1\n")
print(IRC.recv(4096).decode("UTF-8"), " :: 2\n")
print(IRC.recv(4096).decode("UTF-8"), " :: 3\n")
print(IRC.recv(4096).decode("UTF-8"), " :: 4\n")
print(IRC.recv(4096).decode("UTF-8"), " :: 5\n")

print(IRC.recv(4096).decode("UTF-8"), " :: 6\n")
print(IRC.recv(4096).decode("UTF-8"), " :: 7\n")