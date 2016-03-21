import string


def join_room(s):
    readbuffer = ""
    loading = True
    while loading:
        readbuffer = readbuffer + s.recv(1024)
        temp = string.split(readbuffer, "\n")
        readbuffer = temp.pop()

        for line in temp:
            print(line)
            loading = loading_complete(line)
    print("Succesfully joined chat.\n")


def loading_complete(line):
    if "End of /NAMES list" in line:
        return False
    else:
        return True
