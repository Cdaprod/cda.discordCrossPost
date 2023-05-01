import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

from social_handlers import (
    post_to_facebook,
    post_to_twitter,
    post_to_instagram,
    post_to_linkedin,
    post_to_pinterest,
    # post_to_youtube,  # Add this once you implement the YouTube handler
)

load_dotenv()

bot = commands.Bot(command_prefix="//")

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready.")

@bot.command(name="facebook")
async def facebook(ctx, *, message):
    post_to_facebook(message)
    await ctx.send("Posted to Facebook!")

@bot.command(name="twitter")
async def twitter(ctx, *, message):
    post_to_twitter(message)
    await ctx.send("Posted to Twitter!")

@bot.command(name="instagram")
async def instagram(ctx, message, image_url):
    post_to_instagram(message, image_url)
    await ctx.send("Posted to Instagram!")

@bot.command(name="linkedin")
async def linkedin(ctx, *, message):
    post_to_linkedin(message)
    await ctx.send("Posted to LinkedIn!")

@bot.command(name="pinterest")
async def pinterest(ctx, message, image_url):
    post_to_pinterest(message, image_url)
    await ctx.send("Posted to Pinterest!")

# Add a YouTube command once you implement the YouTube handler

bot.run("your_discord_bot_token")
