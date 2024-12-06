import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot configuration
BOT_TOKEN = os.getenv('BOT_TOKEN')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')
GROUP_ID = os.getenv('GROUP_ID')

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

# Buy button URL
BUY_URL = "https://pumpfun.com/trade/jokearmy"

# Reminder messages
REMINDER_MESSAGES = [
    "🚀 JokeArmy ($JOKE) is now LIVE on Solana! Buy on PumpFun: pumpfun.com/trade/jokearmy 🔥\n\n💎 Low Market Cap Gem\n✅ Liquidity Locked\n🔒 Contract Renounced",
    "💫 Join the JokeArmy ($JOKE) revolution! Trade now on PumpFun!\n\n📈 Chart looking bullish\n💎 Diamond hands community\n🌟 Next 100x Solana Gem",
    "🎯 Don't miss out on JokeArmy ($JOKE)!\n\n🚀 The most entertaining token on Solana\n💎 Strong community\n💰 Buy now on PumpFun before we moon! 🌙"
]
