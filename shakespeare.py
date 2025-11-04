### MIT ASSIGNMENT 3 ###
# BY BORIS ALZAMORA
## SHAKESPEARE REWRITER DISCORD AGENT
# Objetive> Rewrite any text you send into a Shakespeare style redacted text

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import discord
import os

load_dotenv()

llm = ChatOllama(model="llama3.2")

def call_ollama(question):
    systemprompt = """
    you are a helpful assistant who rewrites any piece of text into a formal manner taking styles of
      shakespeare and the ancient english books
    """ 
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", systemprompt),
            ("user", "{question}")
        ]
    )

    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser
    response = chain.invoke({"question": question})

    return response

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

    if message.content.startswith("$rewrite"):
        print(f"Message:{message.content}")
        message_content = message.content.split("$rewrite")[1]
        print(f"Query> {message_content}")
        response = call_ollama(message_content)
        print(f"Assistant: {response}")
        print("----")
        await message.channel.send(response)

client.run(os.getenv("DISCORDBOT_KEY"))