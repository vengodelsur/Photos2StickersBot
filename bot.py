# encoding: utf-8
import telebot
import requests
import skimage
access_token = '615690891:AAGoQ8B1Q-4saF0dhyV6vJ8Syku3whOwBrQ'
# Создание бота с указанным токеном доступа
bot = telebot.TeleBot(access_token)

import neural_net
from PIL import Image





@bot.message_handler(content_types=['photo'])
def photo(message):
    
    file_id = message.photo[-1].file_id
    #bot.send_photo(message.chat.id, file_id)
    photo_file = bot.get_file(file_id)
    photo_file_path = photo_file.file_path
    url = 'https://api.telegram.org/file/bot' + access_token + '/' + photo_file_path
    r = requests.get(url, allow_redirects=True)
    print('connected')
    open('img.jpg', 'wb').write(r.content)
    
    image = skimage.io.imread('img.jpg')
    result = neural_net.predict_by_image(image)
    pil_image = neural_net.apply_mask(image, result)
    
    pil_image.save('img.webp')
    object_number = 0
    y1, x1, y2, x2 = result['rois'][object_number]
    
    process_image('img.webp', (x1 + x2)/2, (y1 + y2)/2) 
     
    with open('img.webp', 'rb') as f:
        bot.send_document(message.chat.id, f)  

def process_image(image_file_name, w_center, h_center):
    img = Image.open(image_file_name)
    w, h = img.size
    area = (w_center - 512/2, h_center - 512/2, w_center + 512/2, h_center + 512/2)
    cropped_img = img.crop(area)
    cropped_img.save(image_file_name)

if __name__ == '__main__':
    #photo('')
    bot.polling(none_stop=True)


