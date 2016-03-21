from .src import commands_dict


def execute(command, pars, bot_class, whitelisted=False):
    if command in commands_dict:
        if whitelisted or commands_dict[command][1] == False:  # Check if user is authorized
            try:
                return commands_dict[command][0](pars, bot_class=bot_class)
            except Exception as e:
                return 'Error: "' + str(e) + '" Is this a bug?'
        else:
            print "Not authorized to use that command.."
