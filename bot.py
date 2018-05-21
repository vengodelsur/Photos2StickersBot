# encoding: utf-8
import telebot
import requests
import neural_net
from PIL import Image

access_token = '615690891:AAGoQ8B1Q-4saF0dhyV6vJ8Syku3whOwBrQ'
# Создание бота с указанным токеном доступа
bot = telebot.TeleBot(access_token)


@bot.message_handler(content_types=['photo'])
def photo(message):
    file_id = message.photo[-1].file_id
    bot.send_photo(message.chat.id, file_id)
    photo_file = bot.get_file(file_id)
    photo_file_path = photo_file.file_path
    url = 'https://api.telegram.org/file/bot' + access_token + '/' + photo_file_path
    r = requests.get(url, allow_redirects=True)
    open('img.jpg', 'wb').write(r.content)
    process_image('img.jpg')    

def process_image(image_file_name):
    img = Image.open(image_file_name)
    w, h = img.size
    area = (w/2 - 512/2, h/2 - 512/2, w/2 + 512/2, h/2 + 512/2)
    cropped_img = img.crop(area)
    cropped_img.save(image_file_name)

if __name__ == '__main__':
    bot.polling(none_stop=True)

