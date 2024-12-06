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

def send_buy_button(chat_id, message_text):
    """Create and send message with buy button"""
    markup = types.InlineKeyboardMarkup()
    buy_button = types.InlineKeyboardButton(text="🛍 Buy Now", url=BUY_URL)
    markup.add(buy_button)
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

@app.route('/webhook', methods=['POST'])
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
        welcome_text = f"Welcome {new_member.first_name} to the official JokeCon community! 🎉\n\n🚀 JokeCon is now LIVE on Solana!\n💎 Trade on PumpFun\n🔒 Liquidity Locked\n\nClick below to buy $JKC!"
        send_buy_button(message.chat.id, welcome_text)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    """Handle all messages"""
    # Check if sender is admin
    chat_member = bot.get_chat_member(message.chat.id, message.from_user.id)
    is_admin = chat_member.status in ['creator', 'administrator']

    # Check for invite links
    if contains_link(message) and not is_admin:
        bot.delete_message(message.chat.id, message.message_id)
        warning = bot.send_message(
            message.chat.id,
            f"⚠️ {message.from_user.first_name}, for security reasons, only admins can share invite links! Join our official channels only."
        )
        # Delete warning after 30 seconds
        threading.Timer(30, bot.delete_message, args=[message.chat.id, warning.message_id]).start()
        return

    # Check for forbidden words
    if contains_forbidden_words(message):
        bot.delete_message(message.chat.id, message.message_id)
        bot.ban_chat_member(message.chat.id, message.from_user.id)
        bot.send_message(
            message.chat.id,
            f"🚫 {message.from_user.first_name} has been banned for FUD or harmful behavior. JokeCoin maintains a positive community!"
        )

def send_reminder():
    """Send buy reminder to group"""
    current_hour = datetime.now().hour
    reminder_index = (current_hour // 8) % 3  # Divide day into 3 periods
    send_buy_button(GROUP_ID, REMINDER_MESSAGES[reminder_index])

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
    bot.set_webhook(url=WEBHOOK_URL)
    
    # Start Flask app
    app.run(host='0.0.0.0', port=8443, ssl_context=('cert.pem', 'key.pem'))

if __name__ == '__main__':
    main()
