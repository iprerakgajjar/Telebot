import os
import telebot

bot = telebot.TeleBot(os.getenv('ask'))

@bot.message_handler(func=lambda msg: msg.text[0] != '/') 
def get_id(message):
    #print(message.text)
    if message.text[0:10] == 'ytdownload':
        # print(message.text[19:27])
        if message.text[19:24] == 'youtu':
            lnk1 = message.text[28:]
            lnk2 = ('https://y2mate.com/youtube/' + lnk1)
            bot.reply_to(message, lnk2)
        else:
            arch = message.text[11:]
            split_arch1 = arch[0:15]
            joined_arch = split_arch1 + 'magic'
            split_arch2 = arch[15:]
            main_join = joined_arch + split_arch2
            bot.reply_to(message, main_join)

    elif message.text[0:8] == 'unsplash':
        # print(message.text)
        splited1 = message.text[9:]
        # print(message.text[9:13])

        if message.text[9:13] == 'http':
            bot.reply_to(message, "you can't use any type of link for unsplash")
        else:
            unsplash_link = ('https://unsplash.com/s/photos/' + splited1)
            bot.reply_to(message, unsplash_link)

    else:
        bot.reply_to(message, '❌ Invalid command ❌')

bot.polling() 
