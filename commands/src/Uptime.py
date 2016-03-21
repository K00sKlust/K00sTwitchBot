import time

need_whitelist = False
command_name = "!uptime"


def main(pars, bot_class):
    time_s = int(time.time() - bot_class.start_time)
    readable_time = '{:02}:{:02}:{:02}'.format(time_s / 3600, time_s / 60 % 60, time_s % 60)
    return "Bot's uptime = " + readable_time
