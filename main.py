import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if not message.author == self.user:
            message.content = message.content.lower()
            if message.content.startswith("sbw "):
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
        await profile_commands(command[2::], message)
    else:
        response = f"Unknown command `{command[1]}`, try `sbw help` for a list of all commands"
        await message.channel.send(response)
        print(f"[LOG]: returned '{response}'")


async def profile_commands(command, message):
    return command, message


client = MyClient()
with open(file="./token") as f:
    client.run(f.readlines()[0])
