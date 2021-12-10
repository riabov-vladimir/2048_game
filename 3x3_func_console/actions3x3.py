from os import system, name


def clear_console():
    """
    Clears console output for 3 main OS types
    :return:
    """
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')
