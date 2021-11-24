import discord
import modules.commands as cmds

authorized = ["227483302833946626",
              "337138327549509632"]


class MyClient(discord.Client):
    async def on_ready(self):
        print("_"*54 + "\n"
              " ___  ___       __      __ _      _     _  _      _   \n"
              "/ __|| _ )      \\ \\    / /(_) ___| |_  | |(_) ___| |_ \n"
              "\\__ \\| _ \\       \\ \\/\\/ / | |(_-/|   \\ | || |(_-/|  _|\n"
              "|___/|___/        \\_/\\_/  |_|/__/|_||_||_||_|/__/ \\__|\n"
              + "_"*16 + " By tedzards509#3737  " + "_"*16 + "\n")
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        message.content = message.content.lower()
        if not message.author == self.user and message.content.startswith("sbw "):
            command = message.content.split(" ")
            command = normalize(command)
            print(f"[LOG]: {message.author} tried to execute '{command}'")
            await exec_cmd(command, message)


def normalize(commands):
    return commands


async def exec_cmd(command, message):
    if command[1] == "ping":
        response = cmds.ping(client)
        await message.channel.send(response)
        print(f"[LOG]: returned '{response}'")
    elif command[1] == "test":
        response = cmds.test(command[2::])
        await message.channel.send(response)
        print(f"[LOG]: returned '{response}'")
    elif command[1] == "command_name":
        response = cmds.command_name()
        await message.channel.send(response)
        print(f"[LOG]: returned '{response}'")
    elif command[1] == "help":
        response = cmds.sbw_help(command[2::])
        await message.channel.send(response)
        print(f"[LOG]: returned '{response}'")
    elif command[1] == "profile":
        response = cmds.profile(command[2::])
        await message.channel.send(response)
    elif command[1] == "item":
        if str(message.author.id) in authorized:
            response = cmds.item(command[2::])
        else:
            response = "You are not authorized to add items to the repository\n" \
                       "Please dm `tedzards509#3737` for permissions"
        await message.channel.send(response)
        print(f"[LOG]: returned '{response}'")
    else:
        response = f"Unknown command `{command[1]}`, try `sbw help` for a list of all commands"
        await message.channel.send(response)
        print(f"[LOG]: returned '{response}'")


client = MyClient()
with open(file="./token") as token:
    client.run(token.readlines()[0])
