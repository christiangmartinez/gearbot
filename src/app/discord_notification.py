"""
Logic for discord notification for gear matches
"""
import os

import discord
from dotenv import load_dotenv


def main():
    load_dotenv()
    token = os.environ.get("DISCORD_TOKEN")

    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"Logged in as {client.user}")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content.startswith("hello"):
            await message.channel.send("Hello!")

    client.run(token)

if __name__ == "__main__":
    main()
