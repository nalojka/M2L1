import os
import telebot
import requests
from config import BOT_TOKEN
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['mem'])
def send_mem(message):
    img_name = os.listdir('images/memes')
    with open(f'images/memes/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 

@bot.message_handler(commands=['cat'])
def send_mem(message):
    img_name = os.listdir('images/cats')
    with open(f'images/cats/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
    
    
@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)

bot.infinity.polling()
