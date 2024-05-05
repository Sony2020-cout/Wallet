import mmap
def record(total):
    with open('wallet.txt', 'w') as txt:
        txt.write(str(total))
        print('Баланс обновлён: ', total)

def readd(operation):
    with open('wallet.txt', 'r') as txt:
        txt = txt.read()
        balance = str(txt)

        if operation == 'д' or operation == 'р' :
            howMany = input('Сумма:')
            category = input('Категория: ')
            description = input('Описание: ')
            date1 = input('Дата: ')
            record(str(txt) + '\n' +'Дата: ' +date1 + '\n' +'Категория: ' + category + '\n' + 'Сумма: '  + howMany + '\n' + 'Описание: ' +description)
        elif operation == 'п':
            with open('wallet.txt') as f:
                s = mmap.mmap(f.fileno(),0, access=mmap.ACCESS_READ)
                if s.find('кря') != -1:
                    print('true')
                elif s.find('Покупка гаджета') != -1:
                    print('true')

        elif operation == 'и':
            s = input('Введите текст для замены: ')
            f = open('wallet.txt', 'r+')
            f.truncate(0)
            f.write(s)
            f.close()
            print('Текст изменён')
        elif operation == 'в':
            quit()

while True:
    readd(1)
    readd(input('Доход/Расход\n Д/Р: ').lower())