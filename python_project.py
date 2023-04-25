

def add_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone = input('Введите номер телефона: ')
    with open('file_contact.txt', 'a') as f:
        f.write(f'{surname} {name}  {phone}\n')
    print('Контакт успешно сохранен')

def show_contacts():
    with open('file_contact.txt', 'r') as f:
        for line in f:
            print(line.strip())

def search_contact():
    search_key = input('Введите номер контакта: ')
    with open('file_contact.txt', 'r') as f:
        for line in f:
            if search_key in line:
                print(line.strip())

def delete_contact():
    search_key = input('Введите номер контакта: ')
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
def main():
    while True:
        print('1. Добавить контакт')
        print('2. Показать контакт')
        print('3. Найти контакт')
        print('4. Выход')
        choice = input('Введите свой выбор: ')
        if choice == '1':
            add_contact()
        elif choice == '2':
            show_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            break
        else:
            print('Неверный выбор!')

if __name__ == '__main__':
    main()


    