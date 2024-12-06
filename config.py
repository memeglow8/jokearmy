import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot configuration
BOT_TOKEN = os.getenv('BOT_TOKEN')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')
GROUP_ID = os.getenv('GROUP_ID')
PROJECT_NAME = os.getenv('PROJECT_NAME', 'JokeCoin')
BUY_URL = os.getenv('BUY_URL', 'https://pumpfun.com/trade/jokecoin')
CLAIM_URL = os.getenv('CLAIM_URL', 'https://claim.jokecoin.com')
WELCOME_IMAGE_URL = os.getenv('WELCOME_IMAGE_URL')
WARNING_IMAGE_URL = os.getenv('WARNING_IMAGE_URL')
BAN_IMAGE_URL = os.getenv('BAN_IMAGE_URL')
REMINDER_IMAGE_URL = os.getenv('REMINDER_IMAGE_URL')

# Forbidden words that will result in ban
FORBIDDEN_WORDS = [
    "scam",
    "rug",
    "fake",
    "honeypot",
    "rugpull",
    "pump and dump",
    "ponzi",
    "fud"
]

# Reminder messages
REMINDER_MESSAGES = [
    f"🚀 {PROJECT_NAME} ($JOKE) is now LIVE on Solana! Buy now: {BUY_URL} 🔥\n\n💎 Low Market Cap Gem\n✅ Liquidity Locked\n🔒 Contract Renounced",
    f"💫 Join the {PROJECT_NAME} ($JOKE) revolution! Trade now!\n\n📈 Chart looking bullish\n💎 Diamond hands community\n🌟 Next 100x Solana Gem",
    f"🎯 Don't miss out on {PROJECT_NAME} ($JOKE)!\n\n🚀 The most entertaining token on Solana\n💎 Strong community\n💰 Buy now before we moon! 🌙"
]
