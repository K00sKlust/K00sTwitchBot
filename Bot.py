import threading
import string
import socket
import time

from Settings import \
    HOST, PORT, PASS,\
    IDENTITY, CHANNEL,\
    CHECK_LINKS, WHITELIST

import essentials
import commands

class Bot(threading.Thread):
    def __init__(self, channel=CHANNEL):
        self.s_channel = socket.socket()
        self.s_channel.connect((HOST, PORT))
        self.s_channel.send("PASS " + PASS + "\r\n")
        self.s_channel.send("NICK " + IDENTITY + "\r\n")
        self.s_channel.send("JOIN #" + channel + "\r\n")
        self.start_time = time.time()
        self.last_sent = time.time()
        self.WHITELIST = WHITELIST
        self.user = ""
        essentials.join_room(self.s_channel)
        print("")

        super(Bot, self).__init__()

    def send_message(self, message):
        if time.time() - self.last_sent >= 2.0:
            pass
        else:
            wait = 2.0 - (time.time() - self.last_sent)
            print("sleeping for %s seconds" % wait)
            time.sleep(wait)

        message_temp = "PRIVMSG #" + CHANNEL + " :" + message
        self.last_sent = time.time()
        self.s_channel.send(message_temp + "\r\n")
        print("Sent: " + message_temp)

    def run(self):
        while True:
            readbuffer = self.s_channel.recv(1024).decode("UTF-8", errors="ignore")
            temp = string.split(readbuffer, "\n")
            readbuffer = temp.pop()

            for line in temp:
                if "PING" in line:
                    print("Pong back")
                    self.s_channel.send(line.replace("PING", "PONG"))
                    break

                self.user, message = essentials.get_user_and_message(line)
                print(self.user + " typed :" + message)

                if CHECK_LINKS and self.user != IDENTITY:
                    urls = essentials.get_links(message)
                    if urls:
                        print urls
                        self.send_message(essentials.get_site_ratings(urls) + " (myWOT.com)")

                if message.startswith("!"):
                    result = commands.execute(message.split()[0],
                                              message.split()[1:],
                                              bot_class=self,
                                              whitelisted=self.user in WHITELIST,
                                              )
                    if result:
                        self.send_message(result)


if __name__ == "__main__":
    myBot = Bot()
    myBot.start()
