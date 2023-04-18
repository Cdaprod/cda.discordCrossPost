require('dotenv').config({ path: require('path').join(__dirname, '..', '.env') });
const Discord = require('discord.js');
const Twit = require('twit');
const FB = require('fb');

// Set up Twitter API🤝
const T = new Twit({
  consumer_key: process.env.TWITTER_CONSUMER_KEY,
  consumer_secret: process.env.TWITTER_CONSUMER_SECRET,
  access_token: process.env.TWITTER_ACCESS_TOKEN,
  access_token_secret: process.env.TWITTER_ACCESS_TOKEN_SECRET,
  timeout_ms: 60 * 1000,
});

// Set up Facebook API🤝
FB.options({
  version: '3.0',
  accessToken: process.env.FB_ACCESS_TOKEN,
});

// Set up Discord bot👏
const client = new Discord.Client({ intents: ['GUILD_MESSAGES', 'GUILDS'] });

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}! 😎`);
});

client.on('messageCreate', async (message) => {
  if (message.author.bot) return;

  // Cross-post message to Twitter📦
  const twitterContent = message.content.length > 277 ? message.content.slice(0, 277) + '...' : message.content;
    T.post('statuses/update', { status: twitterContent }, (err, data, response) => {
      if (err) console.log(`Error posting to Twitter 😵‍💫: ${err}`);

  // Cross-post message to Facebook group📦
  FB.api(`${process.env.FB_GROUP_ID}/feed`, 'post', { message: message.content }, (res) => {
    if (!res || res.error) {
      console.log(!res ? 'Error occurred with cross-post to Facebook 😵' : res.error);
    }
  });
});

client.login(process.env.DISCORD_BOT_TOKEN);
