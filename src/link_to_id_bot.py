#!/usr/bin/python3
import telebot, os

if os.environ.get('__BOT_TOKEN') == None:
    print("Please load token environment vars, try \"source .env\" or create this before using bot using \"./suggs create-env <TOKEN>\".")
    exit()

TOKEN = os.environ.get('__BOT_TOKEN')

bot = telebot.TeleBot(TOKEN, parse_mode='MarkdownV2')

@bot.message_handler(commands=['help', 'start', 'hello'])
def help_command(message):
    bot.reply_to(message, "generate link to user with ID:\n \/genUsernameLinkId \<NUMBER\-OF\-USER\-ACCOUNT\-ID\> \<DISPLAYED\-NAME\>\ngenerate link to Telegram URI:\n\/genLinkUrl \<TELEGRAM\-URI\> \<LINK\-LABEL\>")

@bot.message_handler(commands=['genUsernameLinkId'])
def send_msg_link_to_id(message):
    msg_arr = message.text.split() # /id is 0 pos
    if len(msg_arr) < 3:
        arguments_dump = ', '.join(msg_arr)
        print(f'Error, insufficient arguments for command execution. ARGS: {arguments_dump}')
        bot.reply_to(message, 'Error, insufficient arguments for command execution')
    else:
        user_id = ''.join(msg_arr[1])
        name = ' '.join(msg_arr[2::])
        msg_content = f'[{name}](tg://user?id={user_id})'
        bot.reply_to(message, msg_content)
        print(msg_content)

@bot.message_handler(commands=['genLinkUrl'])
def send_msg_link_to_uri(message):
    msg_arr = message.text.split() # /id is 0 pos
    if len(msg_arr) < 3:
        arguments_dump = ', '.join(msg_arr)
        print(f'Error, insufficient arguments for command execution. ARGS: {arguments_dump}')
        bot.reply_to(message, 'Error, insufficient arguments for command execution')
    else:
        __uri = ''.join(msg_arr[1])
        link_text = ' '.join(msg_arr[2::])
        bot.reply_to(message, f'[{link_text}]({__uri})')
try:
    bot.infinity_polling()
except KeyboardInterrupt:
    print("Killing bot process.")
    exit()
except Exception as err:
    print("ERROR: " + err)
    exit()