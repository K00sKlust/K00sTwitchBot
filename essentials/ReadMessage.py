def get_user(line):
    separate = line.split(":", 2)
    user = separate[1].split("!", 1)[0]
    return user


def get_message(line):
    separate = line.split(":", 2)
    try:
        message = separate[2]
        return message
    except:
        print("Unable to read line: %s" % line)
        return


def get_user_and_message(line):
    return get_user(line), get_message(line)