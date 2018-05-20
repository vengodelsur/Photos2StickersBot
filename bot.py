# encoding: utf-8
import telebot


access_token = '615690891:AAGoQ8B1Q-4saF0dhyV6vJ8Syku3whOwBrQ'
# Создание бота с указанным токеном доступа
bot = telebot.TeleBot(access_token)


# Бот будет отвечать только на текстовые сообщения
@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)

