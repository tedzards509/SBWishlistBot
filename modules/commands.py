import json


def load_json(path):
    with open(path) as item_file:
        item_json = json.load(item_file)
        return item_json


def command_name():
    """
    Template so I can copypasta.
    """
    output = "ayy you found my template"
    return output


def ping(client):
    """
    Idrk what to say. Its my ping not urs.
    """
    output = f"Pong! {round(client.latency * 1000)}ms"
    return output


def test_raw(param):
    """
    Returns your input as a list of strings
    """
    if not param:
        output = "Test erfolgreich"
    else:
        output = param
    return output


def profile(param):
    return param


def test(param):
    """
    Returns your input as you wrote it
    """
    if not param:
        output = "Test erfolgreich !"
    else:
        output = ""
        for element in param:
            output += f"{element} "
    return output


def item(param):
    """
    Availaible commands: 
    `sbw item add`
    `sbw item info`
    """
    if not param:
        output = item.__doc__
    elif param[0] == "add":
        if len(param) == 2:
            output = item_add(name=param[1], required=None)
        elif len(param) > 2:
            output = item_add(name=param[1], required=param[2::])
        else:
            output = "Something went wrong. Let me just.. <!227483302833946626>"
    else:
        output = item.__doc__
    return output


def item_add(name, required):
    """
    add an item to the repository
    """
    log = f"ayy: name:`{name}`, required:`{required}`"
    return log


def item_info(name):
    items = load_json("./modules/items.json")
    """
    displays info about an item in the repository
    """
    return items


def sbw_help(param):
    """
    Bruh I'm sacrificing my docstrings to make this not as ugly and you use it like this?!
    What do you assume this does?!
    """
    availaible_commands = "Availaible commands:\n" \
                          "`sbw help` - Displays this help message\n" \
                          "`sbw ping` - Returns my ping\n" \
                          "`sbw test` - really only exists for testing, ignore pls\n" \
                          "`sbw testraw` - also only for testing\n" \
                          "For more details use `sbw help [command]`"
    if not param:
        output = availaible_commands
    elif param[0] == "help":
        output = f"`{param[0]}`: {sbw_help.__doc__}"
    elif param[0] == "ping":
        output = f"`{param[0]}`: {ping.__doc__}"
    elif param[0] == "test":
        output = f"`{param[0]}`: {test.__doc__}"
    elif param[0] == "testraw":
        output = f"`{param[0]}`: {test_raw.__doc__}"
    else:
        output = f"Unknown command `{param[0]}`, \n{availaible_commands}"
    return output
