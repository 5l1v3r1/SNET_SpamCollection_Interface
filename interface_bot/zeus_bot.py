import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import httplib2

BOT_API_TOKEN = ''
zeus_bot = Updater(BOT_API_TOKEN)
API_ENDPOINT_URL = ''

def watchMessages(bot, update):
    group_name = update.message.chat.username
    username = update.message.from_user.username 
    text_content = update.message.text
    json_dir = {"group_name": group_name, "username": username, "chat": text_content}
    json_obj = json.dumps(json_dir)
    http = httplib2.Http()
    resp, content = http.request(
        uri=API_ENDPOINT_URL,
        method='POST',
        headers={'Content-Type': 'application/json'},
        body=json_obj
    )


zeus_bot.dispatcher.add_handler(MessageHandler(Filters.text, watchMessages))

zeus_bot.start_polling()
zeus_bot.idle()