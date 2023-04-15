import telebot

bot = telebot.TeleBot("6245178048:AAFecsyw8XrPYbjAZsTzLfO7WMU5rw1lDEY")
@bot.message_handler(commands=["help", "start"])

def enviar(message):
    bot.reply_to(message,"hola, soy ImitaBot, respondo con el mismo mensaje que tú envías, pruébame")

@bot.message_handler(func=lambda message:True)

def mensaje(message):
    bot.reply_to(message, message.text)

bot.polling()