
from transformers import pipeline

model = 'summervent/russian-spellchecking'
token='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'
speller = pipeline("text2text-generation", model=model, use_auth_token=token)

speller('Хоршо ж на свете жыть', num_beams=5, 
    early_stopping=True)

import telebot
# Создаем экземпляр бота
bot = telebot.TeleBot('6090756799:AAE4BInbW4DpCP0BWvfF-pS9qZXOMYsh_EA')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет! Напиши предложение, которое нужно исправить:')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(
        message.chat.id, 
        speller(message.text, num_beams=5, early_stopping=True)[0]['generated_text']
    )
# Запускаем бота
bot.polling(none_stop=True, interval=0)