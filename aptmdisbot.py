import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '-------')

#tm ally sign #711211043212492880
#red ally sign #711210923192352840

@client.event
async def on_message(message):

    if message.channel.id == 701673305647743006:
        #if msg from tm, send to red sign in channel or whatever tm sign in channel they will have.
        #tm ally sign in channel #711211043212492880
        channel = client.get_channel(711211043212492880)
        await channel.send(str(message.content))
    if message.channel.id == 692990720113639434:
        channel = client.get_channel(711210923192352840)
        await channel.send(str(message.content))

client.run('NzEwOTM4ODQwOTIzMjQyNTI3.Xr7xzw.rlIQdTmKnifHE4Se2kd_pHOMwzU')