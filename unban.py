import discord

# Replace TOKEN with your Discord bot's token
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    # Get the server object for the server you want to unban all users in
    server = client.get_guild(server id)

    # Get a list of all banned users in the server
    async for ban_entry in server.bans():
        user = ban_entry.user
        await server.unban(user)

client.run('token')
