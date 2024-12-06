# JokeArmy Telegram Bot

A Telegram bot for managing the JokeArmy ($JOKE) community group on Solana.

## Features

- Welcomes new members with custom message and buy button
- Prevents sharing of unauthorized invite links
- Auto-moderates forbidden words and FUD
- Sends periodic reminders about buying $JKC
- Secure configuration using environment variables

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.template` to `.env` and fill in your credentials:
   - BOT_TOKEN: Your Telegram bot token
   - WEBHOOK_URL: Your webhook URL
   - GROUP_ID: Your Telegram group ID

4. Run the bot:
   ```bash
   python bot.py
   ```

## Deployment

This bot is configured for deployment on Render. Make sure to:
1. Set up environment variables in Render dashboard
2. Configure the webhook URL
3. Set up SSL certificates

## License

MIT
