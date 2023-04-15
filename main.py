import telebot

bot = telebot.TeleBot("6245178048:AAFecsyw8XrPYbjAZsTzLfO7WMU5rw1lDEY")
@bot.message_handler(commands=["help", "start"])

def enviar(message):
    bot.reply_to(message,"hola, soy TestBot")

bot.polling()