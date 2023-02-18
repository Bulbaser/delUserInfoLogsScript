import os, shutil, time

path = input('Введи путь до логов: ')
UserInfo = 0
Screen = 0
Wallet = 0
a = list(filter(os.path.isdir, [f'{path}/' + x for x in os.listdir(path)]))
for i in a:
    file = os.listdir(i)
    if 'UserInformation.txt' in file:
        with open(f"{i}/UserInformation.txt", 'r', encoding='utf-8') as f:
            with open(f"{i}/UserInfo.txt", 'w', encoding='utf-8') as w:
                for line in f:
                    if line.startswith('Build ID:'):
                        pass
                    else:
                        w.write(line)
        os.remove(f"{i}/UserInformation.txt")
        UserInfo += 1
    if 'Screenshot.jpg' in file:
        os.remove(f'{i}/Screenshot.jpg')
        Screen += 1
    if 'Wallet' in file:
        shutil.rmtree(f'{i}/Wallets')
        Wallet += 1
    else:
        pass
print(f'Всего было удалено: UserInformation : {UserInfo}, Screenshot.jpg : {Screen}, Wallet : {Wallet}')
time.sleep(100)
