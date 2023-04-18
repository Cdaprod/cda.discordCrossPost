import os
import discord
import openai
import requests
import json
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
import twitter
import facebook

# Load API keys from environment variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET_KEY = os.getenv("TWITTER_API_SECRET_KEY")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
FACEBOOK_ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN")
LINKEDIN_CLIENT_ID = os.getenv("LINKEDIN_CLIENT_ID")
LINKEDIN_CLIENT_SECRET = os.getenv("LINKEDIN_CLIENT_SECRET")
LINKEDIN_ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")

# Initialize OpenAI, Twitter, and Facebook clients
openai.api_key = OPENAI_API_KEY
twitter_api = twitter.Api(consumer_key=TWITTER_API_KEY, consumer_secret=TWITTER_API_SECRET_KEY, access_token_key=TWITTER_ACCESS_TOKEN, access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)
facebook_graph = facebook.GraphAPI(access_token=FACEBOOK_ACCESS_TOKEN, version="3.0")

# Function to create LinkedIn client
def create_linkedin_client():
    credentials = service_account.Credentials.from_service_account_info(
        LINKEDIN_CLIENT_ID, LINKEDIN_CLIENT_SECRET, LINKEDIN_ACCESS_TOKEN)
    service = build('linkedin', 'v1', credentials=credentials)
    return service

linkedin_client = create_linkedin_client()

# Function to generate original content using OpenAI ChatGPT
async def generate_original_content(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Function to post to different social media platforms
async def cross_post(message):
    prompt = f"Create 3 variations of this message: '{message}' for Facebook, LinkedIn, and Twitter."
    generated_messages = await generate_original_content(prompt)
    fb_message, linkedin_message, twitter_message = generated_messages.split('\n')

    # Post to Facebook
    fb_post_id = facebook_graph.put_object(parent_object="me", connection_name="feed", message=fb_message)["id"]

    # Post to LinkedIn
    linkedin_share = {
        "author": f"urn:li:person:{linkedin_client.get_profile()['id']}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": linkedin_message
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC
