import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.content.startswith('핑'):
        await message.channel.send('퐁!')

client.run("")
