import random

def generate_passwords(start_len, end_len):
    charn = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    passwords = []
    for i in range(start_len, end_len + 1):
        while len(passwords) < 1000:
            password = ""
            for j in range(i):
                password += random.choice(charn)
            if password not in passwords:
                passwords.append(password)
            if len(passwords) == 1000:
                print(f'{i} символьные пароли сгенерированы.')
                with open(f'passwords.txt', 'a') as f:
                    for password in passwords:
                        f.write(password + '\n')
                passwords = []
                break
    print('Все пароли сгенерированы.')

if __name__ == '__main__':
    start_len = int(input('Введите минимальную длину пароля: '))
    end_len = int(input('Введите максимальную длину пароля: '))
    generate_passwords(start_len, end_len)
