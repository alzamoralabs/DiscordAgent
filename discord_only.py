from dotenv import load_dotenv
import discord
import os

load_dotenv()

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  #Ensure that your bot canr ead message content

# Create a Client instance with the specified intents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('Bot is ready!')

@client.event
async def on_message(message: discord.Message):
    print(message.content)
    if message.author == client.user:
        return
    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

client.run(os.getenv("DISCORDBOT_KEY"))