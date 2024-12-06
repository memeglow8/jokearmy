import os
from flask import Flask, request, Response
from telebot import TeleBot, types
import schedule
import time
import threading
from datetime import datetime
import re
from config import *

app = Flask(__name__)
bot = TeleBot(BOT_TOKEN)

def send_buy_button(chat_id, message_text, image_url=None):
    """Create and send message with buy and claim buttons"""
    markup = types.InlineKeyboardMarkup()
    buy_button = types.InlineKeyboardButton(text="🛍 Buy Now", url=BUY_URL)
    claim_button = types.InlineKeyboardButton(text="🎁 Claim Airdrop", url=CLAIM_URL)
    markup.add(buy_button, claim_button)
    
    if image_url:
        bot.send_photo(chat_id, image_url, caption=message_text, reply_markup=markup)
    else:
        bot.send_message(chat_id, message_text, reply_markup=markup)

def contains_link(message):
    """Check if message contains telegram invite link"""
    pattern = r't\.me/|telegram\.me/'
    return bool(re.search(pattern, message.text.lower()))

def contains_forbidden_words(message):
    """Check if message contains any forbidden words"""
    if message.text:
        return any(word.lower() in message.text.lower() for word in FORBIDDEN_WORDS)
    return False

@app.route('/', methods=['POST'])
def webhook():
    """Handle webhook requests from Telegram"""
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return Response('ok', status=200)
    else:
        return Response('error', status=403)

@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    """Welcome new members with buy button"""
    for new_member in message.new_chat_members:
        welcome_text = f"🎉 Welcome {new_member.first_name} to the official {PROJECT_NAME} community! 🚀\n\n🔥 HUGE NEWS: We just launched and we're spreading joy with massive airdrops!\n\n💰 Claim up to $50,000 in $JKC tokens if you're a holder!\n\n✨ Why Join Us:\n🎯 Fresh Launch\n😊 Putting smiles on faces\n💎 Massive airdrop potential\n🔒 Liquidity Locked\n\n🎁 Choose Your Path:\n• Buy Now to become eligible\n• Claim your airdrop if you're a holder"
        send_buy_button(message.chat.id, welcome_text, WELCOME_IMAGE_URL)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    """Handle all messages"""
    # Check if sender is admin
    chat_member = bot.get_chat_member(message.chat.id, message.from_user.id)
    is_admin = chat_member.status in ['creator', 'administrator']

    # Check for invite links
    if contains_link(message) and not is_admin:
        bot.delete_message(message.chat.id, message.message_id)
        warning_text = f"⚠️ {message.from_user.first_name}, for security reasons, only admins can share invite links! Join our official channels only."
        if WARNING_IMAGE_URL:
            warning = bot.send_photo(message.chat.id, WARNING_IMAGE_URL, caption=warning_text)
        else:
            warning = bot.send_message(message.chat.id, warning_text)
        # Delete warning after 30 seconds
        threading.Timer(30, bot.delete_message, args=[message.chat.id, warning.message_id]).start()
        return

    # Check for forbidden words
    if contains_forbidden_words(message):
        bot.delete_message(message.chat.id, message.message_id)
        bot.ban_chat_member(message.chat.id, message.from_user.id)
        ban_text = f"🚫 {message.from_user.first_name} has been banned for FUD or harmful behavior. {PROJECT_NAME} maintains a positive community!"
        if BAN_IMAGE_URL:
            bot.send_photo(message.chat.id, BAN_IMAGE_URL, caption=ban_text)
        else:
            bot.send_message(message.chat.id, ban_text)

def send_reminder():
    """Send buy reminder to group"""
    current_hour = datetime.now().hour
    reminder_index = (current_hour // 8) % 3  # Divide day into 3 periods
    send_buy_button(GROUP_ID, REMINDER_MESSAGES[reminder_index], REMINDER_IMAGE_URL)

def schedule_reminders():
    """Schedule reminder messages"""
    schedule.every().day.at("08:00").do(send_reminder)
    schedule.every().day.at("16:00").do(send_reminder)
    schedule.every().day.at("00:00").do(send_reminder)
    
    while True:
        schedule.run_pending()
        time.sleep(60)

def main():
    """Main function to start the bot"""
    # Start reminder scheduler in a separate thread
    reminder_thread = threading.Thread(target=schedule_reminders)
    reminder_thread.daemon = True
    reminder_thread.start()
    
    # Set webhook
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL + '/')
    
    # Start Flask app
    # In production (Render), the SSL is handled by the platform
    if os.environ.get('RENDER'):
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8443)))
    else:
        # Local development with SSL
        app.run(host='0.0.0.0', port=8443, ssl_context=('cert.pem', 'key.pem'))

if __name__ == '__main__':
    main()
