import discord


client = discord.Client()
@client.event
async def on_ready():
    guild = client.guilds[0]
    print(guild.name, "is the name of the server")
    print(client.user, "has connected to the client")
client.run("OTA2MTY2MTQzNzAwNTg2NTI3.YYUq_A.vc4aP3ycGgrkL2DBI3nZTw8t8zo")

