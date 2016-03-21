import os

commands_dict = {}

for module_name in os.listdir(os.path.dirname(__file__)):
    if module_name == '__init__.py' or module_name[-3:] != '.py':
        pass
    else:
        try:
            module_name = module_name[:-3]
            print("Registering command '%s'" % module_name)
            __import__(module_name, locals(), globals())

            command_name = eval(compile(module_name + ".command_name", '<string>', 'eval'))
            command_main = eval(compile(module_name + ".main", '<string>', 'eval'))
            need_whitelist = eval(compile(module_name + ".need_whitelist", '<string>', 'eval'))
            module = eval(compile(module_name, '<string>', 'eval'))

            commands_dict[command_name] = [command_main, need_whitelist]

        except AttributeError:
            print("%s was NOT imported" % module_name)
            print("Please add the variables 'need_whitelist' and 'command_name' to command '%s'" % module_name)

print("\n")

del module
del module_name
del os
