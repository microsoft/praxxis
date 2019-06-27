def display_delete_env(name):
    """ the display function for deleted environments"""
    print(f"{name} deleted")

    
def display_list_env(envs):
    """the display function for listing environments"""
    print(f"Environment Variables: ")
    if envs == []:
        print("\tNone Set")
        return
    i = 0
    for env in envs:
        i += 1
        print(f"\t{i}.\t{env[0]} = {env[1]}")


def display_set_env(name, value):
    """the display function for set environments"""
    print(f"Set environment for scene:\n\t{name} = {value}")


def display_view_env(envs, set_envs):
    from colorama import init, Fore, Style
    init()
    if envs == []:
        print("No parameters")
    else:
        set_envs = dict(set_envs)
        envs = dict(envs)
        counter = 0
        for name in envs:
            counter += 1
            print(f"\t{counter}.\t{name} = ", end="")
            if name in set_envs:
                print(f"{Fore.BLUE}{set_envs[name]}{Style.RESET_ALL}" )
            else:
                print(name)



