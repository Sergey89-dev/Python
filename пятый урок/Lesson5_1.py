#Задание 1
user_text = input('Введите данные через пробел:').split()
with open('test_file.txt', 'w') as my_file:
    for line in user_text:
        my_file.write(line + '\n')

with open('test_file.txt', 'r') as files:
    for content in files:
        print(content)



