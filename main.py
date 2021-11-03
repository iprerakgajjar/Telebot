# Before using this code Make sure to read readme file to understand command for this bot.
import os # importing os.
import telebot #importing  telebot library.

bot = telebot.TeleBot(os.getenv('ask')) # here you are saving your api into bot variable.

@bot.message_handler(func=lambda msg: msg.text[0] != '/')  # here you are input command and checking you doesn't using '/' for command.
def get_id(message): # created function.
    #print(message.text)
    if message.text[0:10] == 'ytdownload': # this is checking string for command you are enetered a valid command.
        # print(message.text[19:27])
        if message.text[19:24] == 'youtu': # this is checking for a link of Youtube Mobile appliction because youtube mobile link will be like https://youtu.be/.....
            lnk1 = message.text[28:] # getting string after ../fsffhaskfhkasfakshasfjasf
            lnk2 = ('https://y2mate.com/youtube/' + lnk1) # concatinating two string.
            bot.reply_to(message, lnk2) # this is using for send reply to the user.
        else:       # in else condiotion works for youtube browser link.
            arch = message.text[11:] # storing particular lengh of string.
            split_arch1 = arch[0:15]
            joined_arch = split_arch1 + 'magic' # concating two string.
            split_arch2 = arch[15:]
            main_join = joined_arch + split_arch2
            bot.reply_to(message, main_join) # this is using for send reply to the user.

    elif message.text[0:8] == 'unsplash': # this is checking string for command you are enetered a valid command.
        # print(message.text)
        splited1 = message.text[9:]
        # print(message.text[9:13])

        if message.text[9:13] == 'http': # here this condition make sure that input wouldn't be a url.
            bot.reply_to(message, "you can't use any type of link for unsplash") # if input will be url bot sends this message .
        else:
            unsplash_link = ('https://unsplash.com/s/photos/' + splited1) # concate two string.
            bot.reply_to(message, unsplash_link) # sending reply to the user.

    else:
        bot.reply_to(message, '❌ Invalid command ❌') # this else condtion sends reply to the user that your command is invalid.

bot.polling() # Upon calling this function, TeleBot starts polling the Telegram servers for new messages.
