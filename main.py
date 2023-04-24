import requests
from bs4 import BeautifulSoup
from random import choice, randint
import telebot
from telebot import types


url = 'https://povar.ru'
headers = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

req = requests.get(url, headers)
# print(req.text)

with open('projects.html', "w") as file:
    file.write(req.text)

with open('projects.html') as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
recepts = soup.find_all("a", class_= "fmHead")
# print(recepts)
recepts_url = []
for i in recepts:
    rec_url = i.get("href")
    # print(rec_url)
    recepts_url.append(rec_url)
# print(recepts_url)

# Горячие блюда:
random_page = randint(1, 50)
url2 = f'https://povar.ru/{recepts_url[0]}/{random_page}'
r = requests.get(url2)
soup2 = BeautifulSoup(r.text, 'html.parser')
all_recepts = soup2.find_all('a', class_='listRecipieTitle')
# print(all_recepts)
recepts_url1 = []
for i in all_recepts:
    rec_url1 = i.get("href")
    recepts_url1.append(rec_url1)
# print(recepts_url1)
choice(recepts_url1)

# Салаты:
random_page_salad = randint(1, 50)
url_salad = f'https://povar.ru/{recepts_url[1]}/{random_page_salad}'
r_salad = requests.get(url_salad)
soup_salad = BeautifulSoup(r_salad.text, 'html.parser')
all_recepts_salad = soup_salad.find_all('a', class_='listRecipieTitle')
recepts_url_salad = []
for i in all_recepts_salad:
    rec_url_salad = i.get("href")
    recepts_url_salad.append(rec_url_salad)
choice(recepts_url_salad)

# Закуски
random_page_snack = randint(1, 50)
url_snack = f'https://povar.ru/{recepts_url[2]}/{random_page_snack}'
r_snack = requests.get(url_snack)
soup_snack = BeautifulSoup(r_snack.text, 'html.parser')
all_recepts_snack = soup_snack.find_all('a', class_='listRecipieTitle')
recepts_url_snack = []
for i in all_recepts_snack:
    rec_url_snack = i.get("href")
    recepts_url_snack.append(rec_url_snack)
choice(recepts_url_snack)

# Супы
random_page_soup = randint(1, 50)
url_soup = f'https://povar.ru/{recepts_url[3]}/{random_page_soup}'
r_soup = requests.get(url_soup)
soup_soup = BeautifulSoup(r_soup.text, 'html.parser')
all_recepts_soup = soup_soup.find_all('a', class_='listRecipieTitle')
recepts_url_soup = []
for i in all_recepts_soup:
    rec_url_soup = i.get("href")
    recepts_url_soup.append(rec_url_soup)
choice(recepts_url_soup)

# Выпечка
random_page_bakery = randint(1, 50)
url_bakery = f'https://povar.ru/{recepts_url[4]}/{random_page_bakery}'
r_bakery = requests.get(url_bakery)
soup_bakery = BeautifulSoup(r_bakery.text, 'html.parser')
all_recepts_bakery = soup_bakery.find_all('a', class_='listRecipieTitle')
recepts_url_bakery = []
for i in all_recepts_bakery:
    rec_url_bakery = i.get("href")
    recepts_url_bakery.append(rec_url_bakery)
choice(recepts_url_bakery)

# Десерты
random_page_dessert = randint(1, 50)
url_dessert = f'https://povar.ru/{recepts_url[5]}/{random_page_dessert}'
r_dessert = requests.get(url_dessert)
soup_dessert = BeautifulSoup(r_dessert.text, 'html.parser')
all_recepts_dessert = soup_dessert.find_all('a', class_='listRecipieTitle')
recepts_url_dessert = []
for i in all_recepts_dessert:
    rec_url_dessert = i.get("href")
    recepts_url_dessert.append(rec_url_dessert)
choice(recepts_url_dessert)

# Напитки
random_page_drink = randint(1, 50)
url_drink = f'https://povar.ru/{recepts_url[6]}/{random_page_drink}'
r_drink = requests.get(url_drink)
soup_drink = BeautifulSoup(r_drink.text, 'html.parser')
all_recepts_drink = soup_drink.find_all('a', class_='listRecipieTitle')
recepts_url_drink = []
for i in all_recepts_drink:
    rec_url_drink = i.get("href")
    recepts_url_drink.append(rec_url_drink)
choice(recepts_url_drink)

# Соусы
random_page_sauce = randint(1, 50)
url_sauce = f'https://povar.ru/{recepts_url[7]}/{random_page_sauce}'
r_sauce = requests.get(url_sauce)
soup_sauce = BeautifulSoup(r_sauce.text, 'html.parser')
all_recepts_sauce = soup_sauce.find_all('a', class_='listRecipieTitle')
recepts_url_sauce = []
for i in all_recepts_sauce:
    rec_url_sauce = i.get("href")
    recepts_url_sauce.append(rec_url_sauce)
choice(recepts_url_sauce)

# Заготовки
random_page_blanks = randint(1, 50)
url_blanks = f'https://povar.ru/{recepts_url[8]}/{random_page_blanks}'
r_blanks = requests.get(url_blanks)
soup_blanks = BeautifulSoup(r_blanks.text, 'html.parser')
all_recepts_blanks = soup_blanks.find_all('a', class_='listRecipieTitle')
recepts_url_blanks = []
for i in all_recepts_blanks:
    rec_url_blanks = i.get("href")
    recepts_url_blanks.append(rec_url_blanks)
choice(recepts_url_blanks)

# Telebot
bot = telebot.TeleBot('6005076421:AAERLnKaORZKbQowlAARID1AOcgaEhz0LYA')
@bot.message_handler(commands=['start_cook'])

def cook(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    item1 = types.InlineKeyboardButton('Горячие блюда', callback_data='the_first')
    item2 = types.InlineKeyboardButton('Салаты', callback_data='the_second')
    item3 = types.InlineKeyboardButton('Закуски', callback_data='the_third')
    item4 = types.InlineKeyboardButton('Супы', callback_data='the_fourth')
    item5 = types.InlineKeyboardButton('Выпечка', callback_data='the_fifth')
    item6 = types.InlineKeyboardButton('Десерты', callback_data='the_sixth')
    item7 = types.InlineKeyboardButton('Напитки', callback_data='the_seventh')
    item8 = types.InlineKeyboardButton('Соусы', callback_data='the_eighth')
    item9 = types.InlineKeyboardButton('Заготовки', callback_data='the_ninth')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
    bot.send_message(message.chat.id, 'Доброго дня! Давай приготовим что-нибудь вкусненькое. Выбирай желаемую категорию: ', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'the_first':
            bot.send_message(call.message.chat.id, f'https://povar.ru/{recepts_url1[0]}')
            del recepts_url1[0]
        elif call.data == 'the_second':
            bot.send_message(call.message.chat.id, f'https://povar.ru/{recepts_url_salad[0]}')
            del recepts_url_salad[0]
        elif call.data == 'the_third':
            bot.send_message(call.message.chat.id, f'https://povar.ru/{recepts_url_snack[0]}')
            del recepts_url_snack[0]
        elif call.data == 'the_fourth':
            bot.send_message(call.message.chat.id, f'https://povar.ru/{recepts_url_soup[0]}')
            del recepts_url_soup[0]
        elif call.data == 'the_fifth':
            bot.send_message(call.message.chat.id, f'https://povar.ru/{recepts_url_bakery[0]}')
            del recepts_url_bakery[0]
        elif call.data == 'the_sixth':
            bot.send_message(call.message.chat.id, f'https://povar.ru/{recepts_url_dessert[0]}')
            del recepts_url_dessert[0]
        elif call.data == 'the_seventh':
            bot.send_message(call.message.chat.id, f'https://povar.ru/{recepts_url_drink[0]}')
            del recepts_url_drink[0]
        elif call.data == 'the_eighth':
            bot.send_message(call.message.chat.id, f'https://povar.ru/{recepts_url_sauce[0]}')
            del recepts_url_sauce[0]
        elif call.data == 'the_ninth':
            bot.send_message(call.message.chat.id, f'https://povar.ru/{recepts_url_blanks[0]}')
            del recepts_url_blanks[0]
bot.polling()



