# Discord Cross-Post Bot

This bot automatically cross-posts messages from Discord channels to a Facebook group and Twitter account. It's a simple solution to keep your social media platforms in sync with your Discord community.

## Features

Listens to messages in all channels it has access to
Cross-posts messages to a specified Facebook group
Cross-posts messages to a connected Twitter account
Usage

## Clone the repository or download the source code.

Set up your environment variables in a .env file.
Install the necessary dependencies.
Run the bot.
Configuration

## Make sure to set the following environment variables in the .env file:

``` dotenv
DISCORD_BOT_TOKEN=<your_discord_bot_token>
TWITTER_CONSUMER_KEY=<your_twitter_consumer_key>
TWITTER_CONSUMER_SECRET=<your_twitter_consumer_secret>
TWITTER_ACCESS_TOKEN=<your_twitter_access_token>
TWITTER_ACCESS_TOKEN_SECRET=<your_twitter_access_token_secret>
FB_ACCESS_TOKEN=<your_facebook_access_token>
FB_GROUP_ID=<your_facebook_group_id>
```


## Important Notes

Ensure the bot has the proper permissions in your Discord server.
Keep in mind the API rate limits for Facebook and Twitter while using this bot.
Adjust the bot's functionality as needed to fit your specific use case.

## License

This project is released under the MIT License. See the LICENSE file for more information.