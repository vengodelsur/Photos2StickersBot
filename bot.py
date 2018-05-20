# encoding: utf-8
import telebot


access_token = '615690891:AAGoQ8B1Q-4saF0dhyV6vJ8Syku3whOwBrQ'
# Создание бота с указанным токеном доступа
bot = telebot.TeleBot(access_token)


@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.send_photo(message.chat.id, message.photo[-1].file_id)


if __name__ == '__main__':
    bot.polling(none_stop=True)

