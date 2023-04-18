import os
import discord
import tweepy
import facebook
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file in the parent directory 📦
dotenv_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path)

# Set up Twitter API🤝
auth = tweepy.OAuthHandler(os.getenv('TWITTER_CONSUMER_KEY'), os.getenv('TWITTER_CONSUMER_SECRET'))
auth.set_access_token(os.getenv('TWITTER_ACCESS_TOKEN'), os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))
twitter_api = tweepy.API(auth)

# Set up Facebook API🤝
fb_access_token = os.getenv('FB_ACCESS_TOKEN')
fb_group_id = os.getenv('FB_GROUP_ID')
fb_graph = facebook.GraphAPI(access_token=fb_access_token, version="3.0")

# Set up Discord bot👏
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord! 😎🥳')

# Functionality starts below 👇
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Truncate message for Twitter if it exceeds 277 characters✂️
    twitter_content = message.content[:277] + '...' if len(message.content) > 277 else message.content

    # Cross-post message to Twitter📦
    try:
        twitter_api.update_status(twitter_content)
    except tweepy.TweepError as e:
        print(f"Error... 🙀 Posting to Twitter: {e}")


    # Cross-post message to Facebook group📦
    try:
        fb_graph.put_object(parent_object=fb_group_id, connection_name='feed', message=message.content)
    except facebook.GraphAPIError as e:
        print(f"Error 😭 Posting to Facebook: {e}")

client.run(os.getenv('DISCORD_BOT_TOKEN'))
