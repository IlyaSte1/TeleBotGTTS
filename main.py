from telebot import TeleBot
from telebot.types import Message
import data
from gtts import gTTS
import gtts.lang


bot = TeleBot(data.TOKEN)
lang = 'ru'


@bot.message_handler(commands=['start', 'switchlang'])
def send_welcome(message: Message):
    if message.text == '/start':
        bot.send_message(chat_id=message.chat.id, text=f'Привет, {message.from_user.first_name}, давай знакомиться! Меня зовут TextToVoiceBot, я могу перевести текст в аудио-файл. просто введи сообщение, а дальше я всё сделаю сам!')


@bot.message_handler(content_types=['text'])
def text_to_voice(message: Message):
    gTTS(text=message.text, lang=lang).save('123.mp3')
    bot.send_voice(chat_id=message.chat.id, voice=open('123.mp3', 'rb'))


if __name__ == "__main__":
    bot.infinity_polling()
