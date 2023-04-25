import telebot
from telebot import types



token = '6250415313:AAFMLEKYknk4uc7k63ijkP2zl7OBi_53ogo'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Добавить контакт')
    btn2 = types.KeyboardButton('Показать контакты')
    btn3 = types.KeyboardButton('Найти контакт')
    btn4 = types.KeyboardButton('Удалить контакт') 
    markup.add(btn1, btn2, btn3, btn4)
    msg = bot.send_message(message.chat.id, 'Воспользуйтесь панелью', reply_markup=markup)
    bot.register_next_step_handler(msg, choice)

def choice(message):
    if message.text == 'Добавить контакт':
        add_contact(message)
    elif message.text == 'Показать контакты':
        show_contacts(message)
    elif message.text == 'Найти контакт':
        search_contact(message)
    elif message.text == 'Удалить контакт':
        rename_contact_first(message)
    else:
        menu(message)




def add_contact(message):
    msg = bot.send_message(message.chat.id, f'Введите имя контакта')
    bot.register_next_step_handler(msg, add_contact_name)
def add_contact_name(message):
    name = message.text
    with open('file_contact.txt', 'a', encoding='utf-8') as f:
        f.write(f'{name} ')
    msg = bot.send_message(message.chat.id, f'Введите фамилию')
    bot.register_next_step_handler(msg, add_contact_surname)
def add_contact_surname(message):
    surname = message.text
    with open('file_contact.txt', 'a', encoding='utf-8') as f:
        f.write(f'{surname} ') 
    msg = bot.send_message(message.chat.id, f'Введите номер')
    bot.register_next_step_handler(msg, add_contact_phone)
def add_contact_phone(message):
    phone = message.text
    with open('file_contact.txt', 'a', encoding='utf-8') as f:
        f.write(f'{phone}\n')
    bot.send_message(message.chat.id, 'ваш контакт создан')
    menu(message)



def show_contacts(message):
    with open('file_contact.txt', 'rb') as f:
      contents = f.read() 
    bot.reply_to(message, contents)
    menu(message)

def search_contact(message):
    msg = bot.send_message(message.chat.id, f'Введите номер контакта')
    bot.register_next_step_handler(msg, add_search_contact)
def add_search_contact(message):
    search_key = message.text
    with open('file_contact.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if search_key in line:
                bot.reply_to(message,line.strip())
    menu(message)


def rename_contact_first(message):
    msg = bot.send_message(message.chat.id, f'Введите номер контакта')
    bot.register_next_step_handler(msg, rename_contact_second)
def rename_contact_second(message):
    search_key = message.text
    with open('file_contact.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if search_key in line:
                j = line.strip()
    with open('file_contact.txt', 'r', encoding='utf-8') as fr:
        lines = fr.readlines()
        with open('file_contact.txt', 'w', encoding='utf-8') as fw:
            for line in lines:
                if line.strip('\n') != j:
                    fw.write(line)
    bot.reply_to(message, f'Контакт удален')
    menu(message)

bot.polling(none_stop=True)
