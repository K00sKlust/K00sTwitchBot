from . import commands_dict


need_whitelist = False
command_name = "!help"


def get_commands_on_auth(whitelisted):
    if not whitelisted:
        return [i for i in commands_dict if not commands_dict[i][1]]
    else:
        return list(commands_dict)


def main(pars, bot_class):
    commands = get_commands_on_auth(bot_class.user in bot_class.WHITELIST)
    return "Commands you can use: " + ", ".join(commands)
