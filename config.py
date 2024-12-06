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
    f"🔥 BREAKING: {PROJECT_NAME} ($JKC) is giving away up to $50,000 in airdrops!\n\n💎 For Holders Only:\n✨ Fresh Launch\n🔒 Liquidity Locked\n💰 Massive Growth Potential\n\nBuy now to qualify! 🚀",
    f"⚡️ Don't Miss Out: {PROJECT_NAME} ($JKC) Airdrop Alert!\n\n🎁 Up to $50,000 for lucky holders\n😊 Join our joyful community\n💫 Early bird advantages\n\nSecure your tokens now! 🌟",
    f"🚨 Attention Solana Traders! {PROJECT_NAME} ($JKC) is taking off!\n\n💰 $50,000 Airdrop Campaign LIVE\n🎯 Perfect entry point\n🔥 Rapidly growing community\n\nBuy & hold to participate! 🎉",
    f"💎 {PROJECT_NAME} ($JKC) - Your Next Solana Gem!\n\n🎁 Massive Airdrop Program\n🚀 Fresh Launch Phase\n✨ Growing Organically\n\nDon't wait - Buy now! 🌙",
    f"🌟 The Secret is Out: {PROJECT_NAME} ($JKC)!\n\n💸 $50,000 Airdrop Pool\n🎯 Limited Time Opportunity\n🔒 Secure Investment\n\nJoin before it's too late! 💫",
    f"💫 {PROJECT_NAME} ($JKC) is Making Waves!\n\n🎁 $50,000 Airdrop Event\n🚀 Early Stage Opportunity\n💪 Strong Community Backing\n\nGet in now! 🔥",
    f"🎯 Smart Money is Moving to {PROJECT_NAME} ($JKC)!\n\n💰 Massive Airdrop Worth $50,000\n✨ Perfect Timing\n🌟 Unlimited Potential\n\nDon't miss out! 🚀",
    f"⚡️ {PROJECT_NAME} ($JKC) - The Next Big Thing!\n\n🎁 $50,000 Airdrop Running\n💎 Gem Alert\n🔒 Safe Investment\n\nBuy now or regret later! 🌙",
    f"🚀 {PROJECT_NAME} ($JKC) is Trending!\n\n💸 Huge $50,000 Airdrop\n✨ Growing Fast\n💪 Active Community\n\nJoin the movement! 🔥",
    f"🌟 Last Chance: {PROJECT_NAME} ($JKC)!\n\n🎁 $50,000 Airdrop Campaign\n💎 Hidden Gem\n🚀 Ready to Moon\n\nBuy now before takeoff! ⚡️"
]
