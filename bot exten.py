import discord
import os
import requests
import json
import random
from replit import db

client = discord.Client()
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements = [
    "Cheer up!",
    "Hang in there.",
    "You are a great person / bot!"
]


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)

    def update_encouragements(encouraging_message):
        if "encouragement" in db.key():
            encouragements = db["encouragements"]
            encouragements.append(encouraging_message)
            db["encouragements"] = encouragements
        else:
            db["encouragements"] = [encouraging_message]


def delete_encouragement(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del encouragements[index]
        db["encouragements"] = encouragements


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$inspire'):
            quote = get_quote()
        await message.channel.send(quote)

        options = starter_encouragements
        if "encouragements" in db.key

        if any(word in message.content for word in sad_words):
            await message.channel.send(random.choice(starter_encouragements))


client.run(os.environ['TOKEN'])

