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


def test(param):
    """
    Returns your input as you wrote it
    """
    if not param:
        output = "Test erfolgreich"
    else:
        output = param
    return output


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
        output = sbw_help.__doc__
    elif param[0] == "ping":
        output = ping.__doc__
    else:
        output = f"Unknown command `{param[0]}`, \n{availaible_commands}"
    return output
